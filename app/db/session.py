from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from app.db.database import AsyncSessionLocal  # ✅ fixed import

# Dependency function to provide DB session to routes
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
