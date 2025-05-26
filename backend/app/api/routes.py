from fastapi import APIRouter
from ..models.metric import Metric

router = APIRouter()

@router.post("/log")
def log_metric(metric: Metric):
    print(f"[LOG] Project: {metric.project_id}, {metric.metric_name}={metric.value}, step={metric.step}")
    return {"status": "success"}
