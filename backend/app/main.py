from fastapi import FastAPI
from .api.routes import router as log_router

app = FastAPI(title="NeuroPulse API")

app.include_router(log_router)

@app.get("/")
async def root():
    return {"message": "Welcome to NeuroPulse!"}