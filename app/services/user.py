from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.auth import get_password_hash # Import hashing utility

async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    """Hashes the password and creates a new user in the database."""
    
    # 1. Hash the password
    hashed_password = get_password_hash(user_in.password)
    
    # 2. Create the User model instance
    db_user = User(
        username=user_in.username,
        fullname=user_in.fullname,
        hashed_password=hashed_password
    )
    
    # 3. Add to session, commit, and refresh
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user_by_username(db: AsyncSession, username: str) -> User | None:
    """Retrieves a user by username."""
    
    # Use SQLAlchemy Core/ORM to select the user
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    # scalar_one_or_none is used for fetching a single result or None
    return result.scalar_one_or_none()