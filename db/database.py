from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import declarative_base,sessionmaker
from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import AnyUrl
class Settings(BaseSettings):
@@ -8,3 +8,8 @@ class Settings(BaseSettings):
settings=Settings()
Base=declarative_base()
engine = create_async_engine(settings.ASYNC_DATABASE_URL)

async_session_maker=sessionmaker(bind=engine,class_=Async,expire_on_commit=False)
async def get_async_db():
    async with async_session_maker() as session:
        yield session