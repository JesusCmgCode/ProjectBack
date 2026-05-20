from pydantic import BaseModel
from typing import Optional

class Project(BaseModel):
    project_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    owner: str
    created_at: Optional[str] = None