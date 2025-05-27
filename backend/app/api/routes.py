from fastapi import APIRouter, Depends
from app.core.security import get_api_key


router = APIRouter(
    prefix="/log",
    tags=["logging"],
    dependencies=[Depends(get_api_key)]
)

@router.post("/", status_code=201)
async def log_metric(payload: dict):
    """
    Stub endpoint: will validate & save your MetricCreate model later.
    """
    # For now, just echo back:
    return {"status": "ok", "received": payload}
