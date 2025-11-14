from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from app.db.session import get_db_session

router = APIRouter()

@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db_session)):

    return {"message": "Database session is ready."}