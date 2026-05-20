from fastapi import APIRouter, HTTPException
from app.services import slurm_service

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/")
async def listar_jobs():
    jobs = await slurm_service.obtener_jobs()
    return {"total": len(jobs), "jobs": jobs}

@router.get("/{job_id}")
async def obtener_job(job_id: int):
    job = await slurm_service.obtener_job_por_id(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job no encontrado")
    return job