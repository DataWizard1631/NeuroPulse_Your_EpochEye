from fastapi import FastAPI
from .api.routes import router

app = FastAPI(title="NeuroPulse Logging API")

app.include_router(router)
