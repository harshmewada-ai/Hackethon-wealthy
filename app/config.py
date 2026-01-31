from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5433/wealthy_dashboard"
    DEBUG: bool = True
    GOOGLE_API_KEY: Optional[str] = None  # For Gemini AI agent
    
    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra fields from .env


settings = Settings()
