from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.security import get_password_hash, verify_password

async def create_user(user: UserCreate, db: AsyncSession) -> User:
    print(f"🔐 REGISTER: Creating user {user.username} with password: {user.password}")
    hashed_password = get_password_hash(user.password)
    print(f"🔐 REGISTER: Hashed password: {hashed_password}")
    
    db_user = User(
        username=user.username,
        fullname=user.fullname,
        hashed_password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def authenticate_user(username: str, password: str, db: AsyncSession) -> User | None:
    print(f"🔐 LOGIN: Attempting login for user: {username}")
    print(f"🔐 LOGIN: Password provided: {password}")
    
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalars().first()
    
    if not user:
        print(f"❌ LOGIN: User '{username}' not found")
        return None
    
    print(f"✅ LOGIN: User '{username}' found")
    print(f"🔐 LOGIN: Stored hash: {user.hashed_password}")
    
    # Verify the password
    is_valid = verify_password(password, user.hashed_password)
    print(f"🔐 LOGIN: Password verification result: {is_valid}")
    
    if not is_valid:
        print(f"❌ LOGIN: Password verification FAILED")
        return None
        
    print(f"✅ LOGIN: SUCCESS - User authenticated")
    return user