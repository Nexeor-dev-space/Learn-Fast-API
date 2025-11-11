from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings

# Load DB URL using pydantic-settings
class Settings(BaseSettings):
    ASYNC_DATABASE_URL: str

    class Config:
        env_file = ".env"  # Reads from .env file in project root

settings = Settings()

# Create async engine
engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=True)

# Create session generator
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
