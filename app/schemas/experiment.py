from pydantic import BaseModel
from typing import Optional

class Resources(BaseModel):
    cpus: int
    memory: str
    gpu: bool

class Experiment(BaseModel):
    experiment_id: Optional[int] = None
    project_id: int
    name: str
    status: Optional[str] = "PENDING"
    resources: Resources
    dataset: Optional[str] = None
    code: Optional[str] = None
    created_at: Optional[str] = None
    job_id: Optional[int] = None