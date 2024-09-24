import vagrant 
import os

def get_available_boxes():
    v = vagrant.Vagrant()
    boxes = v.box_list()
    
    if not boxes:
        # Fallback to manual directory check
        vagrant_home = os.path.expanduser("~/.vagrant.d/boxes")
        if os.path.exists(vagrant_home):
            boxes = [{'name': box} for box in os.listdir(vagrant_home) if os.path.isdir(os.path.join(vagrant_home, box))]
    
    return boxes


import vagrant

def get_box_by_id(box_id):
    v = vagrant.Vagrant()
    boxes = v.box_list()
    
    if 0 <= box_id < len(boxes):
        box = boxes[box_id]
        return {
            'id': box_id,
            'name': box.name,
            'provider': box.provider,
            'version': box.version,
            'size': 0,  # You might need to implement a way to get the actual size
            'description': 'Description not available'  # You might need to implement a way to get the actual description
        }
    return None