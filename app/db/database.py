from app.core.settings import DB_Settings
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import declarative_base,sessionmaker
from pydantic import AnyUrl

Base=declarative_base()
engine = create_async_engine(DB_Settings.ASYNC_DATABASE_URL)

async_session_maker=sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)
async def get_async_db():
    async with async_session_maker() as session:
        yield session