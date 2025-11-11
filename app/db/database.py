from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

Base = declarative_base()

engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=True)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,  # ✅ Correct class
    expire_on_commit=False
)


async def get_async_db():
    async with async_session_maker() as session:
        yield session
