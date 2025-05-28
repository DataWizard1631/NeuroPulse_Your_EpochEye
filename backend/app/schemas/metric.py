# backend/app/schemas/metric.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MetricCreate(BaseModel):
    timestamp: datetime
    attention: float = Field(..., ge=0.0, le=1.0)
    meditation: float = Field(..., ge=0.0, le=1.0)
    blink: int = Field(..., ge=0)
    user_id: Optional[str] = None  # optional if you're identifying by API key
