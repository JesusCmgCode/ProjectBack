from fastapi import APIRouter
from app.services import slurm_service

router = APIRouter(prefix="/stats", tags=["Estadísticas"])

@router.get("/resumen")
async def resumen():
    jobs = await slurm_service.obtener_jobs()
    nodos = await slurm_service.obtener_nodos()

    running = len([j for j in jobs if j["state"] == "RUNNING"])
    pending = len([j for j in jobs if j["state"] == "PENDING"])

    cpu_total = sum(n["cpus_total"] for n in nodos)
    cpu_usado = sum(n["cpus_used"] for n in nodos)

    return {
        "jobs_corriendo": running,
        "jobs_en_cola": pending,
        "cpu_total": cpu_total,
        "cpu_usado": cpu_usado,
        "cpu_disponible": cpu_total - cpu_usado
    }