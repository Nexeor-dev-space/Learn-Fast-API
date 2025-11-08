from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import  declarative_base
from app.core.config import settings

engine = create_async_engine(
    settings.ASYNC_DB_URL,
    echo=False,
    pool_pre_ping=True
)

# Create async session maker
AsyncSessionLocal =  async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


# Base class for models
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session