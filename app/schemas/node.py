from pydantic import BaseModel

class Node(BaseModel):
    name: str
    cluster: str
    state: str
    cpus_total: int
    cpus_used: int
    memory_total: int
    memory_used: int