from app.core.config import USE_MOCK
from app.mock.jobs_mock import JOBS_MOCK
from app.mock.nodes_mock import NODES_MOCK

async def obtener_jobs():
    return JOBS_MOCK

async def obtener_job_por_id(job_id: int):
    return next((j for j in JOBS_MOCK if j["job_id"] == job_id), None)

async def obtener_nodos():
    return NODES_MOCK