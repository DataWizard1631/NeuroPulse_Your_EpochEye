from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    attention = Column(Float, nullable=False)
    meditation = Column(Float, nullable=False)
    blink = Column(Integer, nullable=False)
    user_id = Column(String, index=True)