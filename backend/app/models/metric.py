from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Metric(BaseModel):
    project_id: str
    metric_name: str
    value: float
    step: Optional[int] = None
    timestamp: Optional[datetime] = None
