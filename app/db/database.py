from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import declarative_base,sessionmaker
from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import AnyUrl
class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file='.env',extra="ignore")
    ASYNC_DATABASE_URL:str
settings=Settings()
Base=declarative_base()
engine = create_async_engine(settings.ASYNC_DATABASE_URL)

async_session_maker=sessionmaker(bind=engine,class_=Async,expire_on_commit=False)
async def get_async_db():
    async with async_session_maker() as session:
        yield session