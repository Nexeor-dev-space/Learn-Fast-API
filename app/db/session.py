from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator

from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)


AsyncSessionFactory = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:

    async with AsyncSessionFactory() as session:
        try:
            yield session
        finally:
            await session.close()