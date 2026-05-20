from fastapi import APIRouter
from app.services import slurm_service

router = APIRouter(prefix="/nodes", tags=["Nodos"])

@router.get("/")
async def listar_nodos():
    nodos = await slurm_service.obtener_nodos()
    return {"total": len(nodos), "nodes": nodos}