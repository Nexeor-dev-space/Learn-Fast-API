# app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import get_db
from app.models.user import User
from app.schemas.register import UserCreate, UserRead
from app.services.user_service import hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserRead)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        # 1️⃣ Check if username already exists
        result = await db.execute(select(User).filter(User.username == user.username))
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )

        # 2️⃣ Hash password
        hashed_pw = hash_password(user.password)

        # 3️⃣ Create new user instance
        new_user = User(
            username=user.username,
            fullname=user.fullname,
            hashed_password=hashed_pw
        )

        # 4️⃣ Save to database
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        # 5️⃣ Return user data (without password)
        return UserRead.from_orm(new_user)

    except SQLAlchemyError as e:
        # Handle database errors
        await db.rollback()  # rollback transaction if something fails
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        )
