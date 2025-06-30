import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import services, models

app = FastAPI(title="LabsBakery API")

origins = ["http://localhost", "http://localhost:5500", "http://127.0.0.1:5500", "null"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(): return {"message": "🥐 Welcome to the LabsBakery Backend!"}

@app.get("/projects")
def list_projects():
    base_dir = services.PROJECTS_BASE_DIR
    if not base_dir.exists(): return []
    return [d.name for d in base_dir.iterdir() if d.is_dir()]

@app.get("/projects/{project_name}")
def get_project_state(project_name: str):
    state_file = services.PROJECTS_BASE_DIR / project_name / "project.json"
    if not state_file.exists():
        return { "nodes": [], "lines": [], "labSettings": { "title": project_name.replace('-', ' ') }, "nodeIdCounter": 1 }
    return models.LabState.parse_file(state_file)

@app.post("/projects/{project_name}/bake")
def bake_lab(project_name: str, state: models.LabState):
    services.save_lab_state(project_name, state)
    services.generate_vagrantfile(project_name, state)
    return {"message": f"Lab '{project_name}' baked successfully!"}

@app.post("/projects/{project_name}/up", status_code=202)
def lab_up(project_name: str):
    code, _, stderr = services.run_vagrant_command(project_name, ["up"])
    if code != 0: raise HTTPException(500, f"Vagrant up failed: {stderr}")
    return {"message": f"Lab '{project_name}' starting up."}

@app.post("/projects/{project_name}/halt", status_code=202)
def lab_halt(project_name: str):
    code, _, stderr = services.run_vagrant_command(project_name, ["halt"])
    if code != 0: raise HTTPException(500, f"Vagrant halt failed: {stderr}")
    return {"message": f"Lab '{project_name}' shutting down."}

@app.get("/projects/{project_name}/status")
def lab_status(project_name: str):
    status = services.get_lab_status(project_name)
    if "error" in status: return status
    return status

@app.post("/projects/{project_name}/vms/{vm_name}/up", status_code=202)
def vm_up(project_name: str, vm_name: str):
    code, _, stderr = services.run_vagrant_command(project_name, ["up", vm_name])
    if code != 0: raise HTTPException(500, f"Vagrant up failed for {vm_name}: {stderr}")
    return {"message": f"VM '{vm_name}' is starting up."}

@app.post("/projects/{project_name}/vms/{vm_name}/halt", status_code=202)
def vm_halt(project_name: str, vm_name: str):
    code, _, stderr = services.run_vagrant_command(project_name, ["halt", vm_name])
    if code != 0: raise HTTPException(500, f"Vagrant halt failed for {vm_name}: {stderr}")
    return {"message": f"VM '{vm_name}' is shutting down."}

@app.post("/projects/{project_name}/vms/{vm_name}/terminal")
def vm_terminal(project_name: str, vm_name: str):
    result = services.start_terminal_session(project_name, vm_name)
    if "error" in result: raise HTTPException(500, result["error"])
    return result