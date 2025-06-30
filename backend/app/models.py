# ~/Documents/labsbackery/backend/app/models.py

from pydantic import BaseModel
from typing import List, Optional

class VMNetwork(BaseModel):
    ip: Optional[str] = ""
    subnet: Optional[str] = ""
    gateway: Optional[str] = ""

class VMNode(BaseModel):
    id: int
    x: float
    y: float
    name: str
    icon: str
    os: str
    ram: str
    cpu: str
    disk: str
    scripts: str
    notes: str
    status: str
    network: List[VMNetwork]

class Connection(BaseModel):
    fromId: int
    toId: int

class LabSettings(BaseModel):
    title: str
    objectives: str
    walkthrough: str
    difficulty: str
    tags: str

class LabState(BaseModel):
    nodes: List[VMNode]
    lines: List[Connection]
    labSettings: LabSettings
    nodeIdCounter: int