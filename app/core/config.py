import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "API Student Talent & Project Hub"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/student_talent_hub")

    class Config:
        env_file = ".env"

settings = Settings()
