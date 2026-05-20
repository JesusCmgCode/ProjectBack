from app.core.supabase_client import supabase_get, supabase_post

async def obtener_proyectos():
    return supabase_get("projects")

async def obtener_proyecto_por_id(project_id: int):
    result = supabase_get("projects", {"project_id": f"eq.{project_id}"})
    if not result:
        return None
    return result[0]

async def crear_proyecto(proyecto: dict):
    proyecto.pop("project_id", None)
    return supabase_post("projects", proyecto)