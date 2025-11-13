from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

class Base(DeclarativeBase):
    pass

# Make sure this variable is named async_engine
async_engine = create_async_engine(  # ← This should be async_engine
    settings.ASYNC_DATABASE_URL,
    echo=True,
)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,  # ← And use it here
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db