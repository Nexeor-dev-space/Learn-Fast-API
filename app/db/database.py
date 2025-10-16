from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import AnyUrl
class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file='.env',extra="ignore")
    ASYNC_DATABASE_URL:str
settings=Settings()
Base=declarative_base()
engine = create_async_engine(settings.ASYNC_DATABASE_URL)
