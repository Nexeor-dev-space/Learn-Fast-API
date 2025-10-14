from sqlalchemy.ext.asyncio import create_async_engine
from pathlib import Path
from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import AnyUrl
class config:
    env_file=str(Path(__file__).resolve().parent.parent/".env")
class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file='.env',extra="ignore")
    ASYNC_DATABASE_URL:str
settings=Settings()
engine = create_async_engine(settings.ASYNC_DATABASE_URL)
