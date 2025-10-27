from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import Users
from app.schemas.schemas import *
from app.db.database import get_async_db

router=APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register")
async def validate_user(users:UserCreate,db: AsyncSession = Depends(get_async_db)):
    try:
        result = await db.execute(select(Users).where(Users.username == users.username))
        existing_user = result.scalar_one_or_none()    
        if existing_user:
            raise HTTPException(status_code=400,detail="Username already exists")
        new_user=Users(username=users.username,fullname=users.fullname)
        new_user.set_password(users.password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return {"message": "User registered successfully", "username": new_user.username}
    except:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Database integrity error (possible duplicate username)")
        