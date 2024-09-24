import os
import json

def scan_lab_projects(projects_dir='lab_projects'):
    projects = []
    for project in os.listdir(projects_dir):
        project_path = os.path.join(projects_dir, project)
        if os.path.isdir(project_path):
            with open(os.path.join(project_path, 'config.json'), 'r') as f:
                config = json.load(f)
            projects.append({
                'name': project,
                'description': config.get('description', ''),
                'boxes': config.get('boxes', []),
                'created_at': config.get('created_at', '')
            })
    return projects
