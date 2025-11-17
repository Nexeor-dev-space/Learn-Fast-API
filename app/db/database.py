from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.core.settings import settings  # import our settings instance

# 1️⃣ Create async engine
engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,  # get async DB URL from settings
    echo=True,                    # optional: logs all SQL queries
    future=True
)

# 2️⃣ Create async session generator
AsyncSessionLocal = sessionmaker(
    bind=engine,                  # bind to our async engine
    class_=AsyncSession,          # use async session class
    expire_on_commit=False        # prevents objects from expiring after commit
)

# 3️⃣ Declarative base for models
Base = declarative_base() 

# 3️⃣ Dependency injection function for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:  # create a new session
        try:
            yield session                       # yield session to route
        finally:
            await session.close()               # close session after use
