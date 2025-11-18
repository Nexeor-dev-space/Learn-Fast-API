# app/routes/login.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, timedelta
from jose import jwt, JWTError

from app.db.database import get_db
from app.models.user import User
from app.schemas.register import UserRead  # for returning minimal user info
from app.services.user_service import verify_password
from app.core.settings import settings  # read JWT settings from .env

router = APIRouter(prefix="/auth", tags=["Auth"])


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


@router.post("/login")
async def login(username: str, password: str, db: AsyncSession = Depends(get_db)):
    try:
        # Fetch the user
        result = await db.execute(select(User).filter(User.username == username))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

        # Verify password
        if not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

        # Create JWT token
        access_token = create_access_token({"sub": user.username})

        # Return user info and token
        return {
            "user": UserRead.model_validate(user),
            "access_token": access_token,
            "token_type": "bearer"
        }

    except HTTPException:
        # Re-raise HTTP errors as is
        raise
    except JWTError as e:
        # JWT-related errors
        raise HTTPException(status_code=500, detail=f"Token generation error: {str(e)}")
    except Exception as e:
        # Catch-all for other unexpected errors
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
