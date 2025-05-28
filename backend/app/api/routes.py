from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.metric import MetricCreate
from app.models.metric import Metric
from app.db.session import SessionLocal
from app.core.security import get_api_key

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/metrics")
def create_metric(
    metric: MetricCreate,
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key),
):
    db_metric = Metric(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return {"message": "Metric saved", "id": db_metric.id}
