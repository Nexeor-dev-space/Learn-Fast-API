from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# 1. Define the Declarative Base class
class Base(DeclarativeBase):
    pass

# 2. Setup the async engine
engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,
    echo=True, # Set to False in production
)

# 3. Setup the async session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# 4. Dependency for database session
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db