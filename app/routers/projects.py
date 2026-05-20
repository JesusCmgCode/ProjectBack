from fastapi import APIRouter, HTTPException
from app.services import project_service
from app.schemas.project import Project

router = APIRouter(prefix="/projects", tags=["Proyectos"])

@router.get("/")
async def listar_proyectos():
    proyectos = await project_service.obtener_proyectos()
    return {"total": len(proyectos), "projects": proyectos}

@router.get("/{project_id}")
async def obtener_proyecto(project_id: int):
    proyecto = await project_service.obtener_proyecto_por_id(project_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto

@router.post("/")
async def crear_proyecto(proyecto: Project):
    nuevo = await project_service.crear_proyecto(proyecto.dict())
    return {"mensaje": "Proyecto creado", "project": nuevo}