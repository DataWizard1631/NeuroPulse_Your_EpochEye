from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from .config import settings

api_key_header = APIKeyHeader(name=settings.API_KEY_HEADER, auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    if not api_key or api_key not in settings.API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid or missing API Key")
    return api_key