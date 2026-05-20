from app.core.supabase_client import supabase_get, supabase_post

async def obtener_experimentos():
    return supabase_get("experiments")

async def obtener_experimentos_por_proyecto(project_id: int):
    return supabase_get("experiments", {"project_id": f"eq.{project_id}"})

async def obtener_experimento_por_id(experiment_id: int):
    result = supabase_get("experiments", {"experiment_id": f"eq.{experiment_id}"})
    if not result:
        return None
    return result[0]

async def crear_experimento(experimento: dict):
    experimento.pop("experiment_id", None)
    return supabase_post("experiments", experimento)