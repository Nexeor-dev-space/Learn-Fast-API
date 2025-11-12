# C:\MyProjects\Learn-Fast-API\app\services\user.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User 
from app.schemas.user import UserIn

# NOTE: The import of get_password_hash is removed from here
# and moved inside the create_user function below.

async def create_user(db: AsyncSession, user_in: UserIn) -> User:
    """Creates a new user record in the database."""
    
    # IMPORT MOVED INSIDE FUNCTION TO PREVENT CIRCULAR DEPENDENCY
    from app.services.auth import get_password_hash
    
    # 1. Hash the password
    hashed_password = get_password_hash(user_in.password)
    
    # 2. Create the user model instance
    new_user = User(
        username=user_in.username,
        fullname=user_in.fullname,
        hashed_password=hashed_password
    )
    
    # 3. Add to session and commit
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user

async def get_user_by_username(db: AsyncSession, username: str):
    """Retrieves a user object by their username."""
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()