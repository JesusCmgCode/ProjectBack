from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/status")
def status():
    return {"mensaje": "Auth en construcción"}