# backend/app/init_db.py

from app.db.session import engine
from app.models.metric import Base

Base.metadata.create_all(bind=engine)
