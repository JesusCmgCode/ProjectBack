from fastapi import APIRouter, HTTPException
from app.services import experiment_service
from app.schemas.experiment import Experiment

router = APIRouter(prefix="/experiments", tags=["Experimentos"])

@router.get("/")
async def listar_experimentos():
    experimentos = await experiment_service.obtener_experimentos()
    return {"total": len(experimentos), "experiments": experimentos}

@router.get("/{experiment_id}")
async def obtener_experimento(experiment_id: int):
    experimento = await experiment_service.obtener_experimento_por_id(experiment_id)
    if not experimento:
        raise HTTPException(status_code=404, detail="Experimento no encontrado")
    return experimento

@router.get("/by-project/{project_id}")
async def experimentos_por_proyecto(project_id: int):
    experimentos = await experiment_service.obtener_experimentos_por_proyecto(project_id)
    return {"project_id": project_id, "total": len(experimentos), "experiments": experimentos}

@router.post("/")
async def crear_experimento(experimento: Experiment):
    nuevo = await experiment_service.crear_experimento(experimento.dict())
    return {"mensaje": "Experimento creado", "experiment": nuevo}