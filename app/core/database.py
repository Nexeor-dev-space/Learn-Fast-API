from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.core.config import settings

# Create async SQLAlchemy engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create sessionmaker factory
async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency for DB session
async def get_db():
    async with async_session_maker() as session:
        yield session
