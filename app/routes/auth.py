# C:\MyProjects\Learn-Fast-API\app\routes\auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
<<<<<<< HEAD

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
=======
from sqlalchemy.future import select
from app.schemas.user import UserCreate, UserRead, UserLogin, Token
from app.models.user import User
from app.services.user_service import create_user, authenticate_user
from app.db.database import get_db  # ← Make sure this import is correct
from datetime import timedelta
from app.core.config import settings
from app.services.auth_service import create_access_token

# ADD prefix and tags to fix routing
router = APIRouter(prefix="/auth", tags=["authentication"])

# --- Registration endpoint ---
@router.post("/register", response_model=UserRead)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await db.execute(
        select(User).where(User.username == user.username)
    )
    if existing_user.scalars().first():
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = await create_user(user, db)
    return new_user

# --- Login endpoint ---
@router.post("/login", response_model=Token)
async def login_for_access_token(
    user_login: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(user_login.username, user_login.password, db)
    if not user:
>>>>>>> dea0a3e (feat(issue-6): Implement login and JWT-based authentication)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
<<<<<<< HEAD
    
    # Generate and return the token
    access_token = create_access_token(
        data={"sub": user.username}
    )
    
=======
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
>>>>>>> dea0a3e (feat(issue-6): Implement login and JWT-based authentication)
    return {"access_token": access_token, "token_type": "bearer"}