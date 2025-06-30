from pathlib import Path
import jinja2
import subprocess
import socket
from collections import defaultdict
from .models import LabState

TERMINAL_SESSIONS = {} 

VAGRANT_BOX_MAP = {
    "Kali Linux": "kalilinux/rolling", "Parrot OS": "parrot/parrot-security",
    "Ubuntu": "ubuntu/jammy64", "Ubuntu 22.04": "ubuntu/jammy64",
    "Windows 10": "gusztavvargadr/windows-10", "Metasploitable": "rapid7/metasploitable3-ub1404",
    "Virtual Router": "corb/vyos", "Firewall": "generic/pfsense"
}
PROJECTS_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "projects"

def _get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def save_lab_state(project_name: str, state: LabState):
    project_dir = PROJECTS_BASE_DIR / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    file_path = project_dir / "project.json"
    json_data = state.model_dump_json(indent=2)
    file_path.write_text(json_data)
    print(f"✅ Lab state saved to: {file_path}")

def generate_vagrantfile(project_name: str, state: LabState):
    project_dir = PROJECTS_BASE_DIR / project_name
    template_dir = Path(__file__).resolve().parent / "templates"
    adj = defaultdict(list)
    for line in state.lines:
        adj[line.fromId].append(line.toId)
        adj[line.toId].append(line.fromId)
    visited, network_groups = set(), []
    for node in state.nodes:
        if node.id not in visited:
            component, stack = set(), [node.id]
            while stack:
                current_id = stack.pop()
                if current_id not in visited:
                    visited.add(current_id)
                    component.add(current_id)
                    stack.extend(adj[current_id])
            if len(component) > 1: network_groups.append(component)
    node_to_network = {}
    for i, group in enumerate(network_groups):
        network_name = f"bakery_net_{i}"
        for node_id in group: node_to_network[node_id] = network_name
    vms_for_template = []
    for node in state.nodes:
        hostname = node.name.replace(" ", "-").lower()
        ram_mb = 2048
        try:
            if "gb" in node.ram.lower(): ram_mb = int(float(node.ram.lower().replace("gb", "").strip()) * 1024)
            elif "mb" in node.ram.lower(): ram_mb = int(float(node.ram.lower().replace("mb", "").strip()))
        except (ValueError, AttributeError): pass
        vms_for_template.append({
            "name": node.name, "hostname": hostname,
            "box_name": VAGRANT_BOX_MAP.get(node.os, "hashicorp/bionic64"),
            "ram_mb": ram_mb, "cpu": node.cpu, "scripts": node.scripts,
            "private_network_name": node_to_network.get(node.id)
        })
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template("Vagrantfile.j2")
    rendered_content = template.render(vms=vms_for_template)
    vagrantfile_path = project_dir / "Vagrantfile"
    vagrantfile_path.write_text(rendered_content)
    print(f"✅ Vagrantfile generated at: {vagrantfile_path}")

def run_vagrant_command(project_name: str, command: list):
    project_dir = PROJECTS_BASE_DIR / project_name
    if not project_dir.exists() or not (project_dir / "Vagrantfile").exists():
        return (1, "", f"Project '{project_name}' or its Vagrantfile does not exist.")
    full_command = ["vagrant"] + command
    print(f"🎛️ Running command: `{' '.join(full_command)}` in `{project_dir}`")
    result = subprocess.run(full_command, cwd=project_dir, capture_output=True, text=True)
    if result.stdout: print(f"  - STDOUT:\n{result.stdout.strip()}")
    if result.stderr: print(f"  - STDERR:\n{result.stderr.strip()}")
    return (result.returncode, result.stdout, result.stderr)

def get_lab_status(project_name: str):
    code, stdout, stderr = run_vagrant_command(project_name, ["status", "--machine-readable"])
    if code != 0: return {"error": stderr}
    status_dict = {}
    for line in stdout.strip().split('\n'):
        parts = line.split(',')
        if len(parts) >= 4 and parts[2] == 'state':
            vm_name, status = parts[1], parts[3]
            status_dict[vm_name] = status
    return status_dict

def start_terminal_session(project_name: str, vm_name: str):
    session_key = f"{project_name}_{vm_name}"
    if session_key in TERMINAL_SESSIONS and TERMINAL_SESSIONS[session_key].poll() is None:
        port = TERMINAL_SESSIONS[session_key].port
        print(f"🔌 Found existing terminal for {vm_name} on port {port}")
        return {"url": f"http://127.0.0.1:{port}", "port": port}
    project_dir = PROJECTS_BASE_DIR / project_name
    port = _get_free_port()
    command = [ "ttyd", "-p", str(port), "--cwd", str(project_dir), "vagrant", "ssh", vm_name ]
    print(f"🚀 Launching terminal for {vm_name} on port {port}")
    process = subprocess.Popen(command)
    process.port = port
    TERMINAL_SESSIONS[session_key] = process
    return {"url": f"http://127.0.0.1:{port}", "port": port}