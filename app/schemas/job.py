from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    job_id: int
    name: str
    user: str
    state: str
    node: Optional[str] = None
    time: str
    cpus: int
    memory: str