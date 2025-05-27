import os
from dotenv import load_dotenv


load_dotenv()  

from pydantic_settings import BaseSettings  
from typing import List

class Settings(BaseSettings):
    ENV: str = "development"
    API_KEY_HEADER: str = "X-API-Key"
    API_KEYS: List[str]           
    DATABASE_URL: str             

class Config:    
    env_file = None  


settings = Settings()
