from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.services.user import create_user, get_user_by_username

# Create the router instance
# The prefix means all routes defined here will start with /auth
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post(
    "/register", 
    response_model=UserRead, 
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user"
)
async def register_user(
    user_in: UserCreate, 
    db: AsyncSession = Depends(get_db) # Dependency injection for DB session
):
    """
    Handles user registration by:
    1. Validating the unique username.
    2. Hashing the password (done in service layer).
    3. Saving the new user to the database.
    """
    try:
        # 1. Validate unique username using the service function
        existing_user = await get_user_by_username(db, username=user_in.username)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )
        
        # 2. Hash password and save user (handled by the service function)
        new_user = await create_user(db, user_in)
        
        # 3. Return the user data, using UserRead to omit the password
        return UserRead.model_validate(new_user)
    except Exception:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
