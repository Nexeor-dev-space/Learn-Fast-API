# C:\MyProjects\Learn-Fast-API\app\routes\auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

# 1. Import Registration Schemas (Check your file path!)
from app.schemas.user import UserIn, UserOut 

# FIX: Import login schemas from 'user'
from app.schemas.user import UserLogin, Token

# 2. Import Login/Token Schemas (Check your file path!)
from app.schemas.user import UserLogin, Token 

# Import services and DB dependency
from app.services.user import create_user 
from app.services.auth import authenticate_user, create_access_token 
from app.db.database import get_db 

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_in: UserIn,
    db: AsyncSession = Depends(get_db)
):
    # (Existing registration logic goes here)
    # ...
    pass # Replace with your existing code

# NEW ROUTE: User Login
@router.post("/login", response_model=Token)
async def login_for_access_token(
    user_in: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    """
    Handles user login, verifies credentials, and issues a JWT token.
    """
    user = await authenticate_user(db, user_in)
    
    if not user:
        # 401 Unauthorized for bad credentials
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generate and return the token
    access_token = create_access_token(
        data={"sub": user.username}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}