from fastapi import APIRouter
from sqlalchemy.future import select
from app.models.models import Users
from app.schemas.schemas import *
from app.db.database import get_async_db

router=APIRouter()

@router.post("/auth/register")
async def validate_user(users:UserCreate,db: get_async_db):
    result = await db.execute(select(Users).filter(Users.username == users.username))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        print("Username already exists")
    new_user = Users(username=users.username)
    new_user.set_password(users.password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {"message": "User registered successfully", "username": new_user.username}
        