
from flask import Blueprint, render_template
from app.vagrant_utils import get_available_boxes, get_box_by_id
from app.lab_utils import scan_lab_projects
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to Lab Management MVP"

@main.route('/vagrant-boxes')
def vagrant_boxes():
    boxes = get_available_boxes()
    projects = scan_lab_projects()
    return render_template('vagrant_boxes.html', boxes=boxes, projects=projects)
# Add more routes as needed

@main.route('/vagrant-box/<int:box_id>')
def vagrant_box_info(box_id):
    box = get_box_by_id(box_id)  # You'll need to implement this function
    return render_template('vagrant_box_info.html', box=box)

@main.route('/lab-projects')
def lab_projects():
    projects = scan_lab_projects()
    return render_template('lab_projects.html', projects=projects)
