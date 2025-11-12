# C:\MyProjects\Learn-Fast-API\app\services\auth.py

from datetime import datetime, timedelta, timezone
from typing import Optional

from passlib.context import CryptContext
from jose import jwt
from app.core.config import settings

# Imports needed for the new login logic:
from app.schemas.user import UserLogin           
from app.services.user import get_user_by_username 

# Hashing Context (Ensure this is set to the working scheme)
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto") 

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Generates a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire, "sub": "access"})
    
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt

# NEW FUNCTION: Core authentication logic
async def authenticate_user(db, user_in: UserLogin):
    """
    Finds a user by username and verifies the password.
    Returns the user object if credentials are valid, otherwise returns False.
    """
    # 1. Retrieve the user
    user = await get_user_by_username(db, user_in.username)
    
    if not user:
        print(f"DEBUG: User '{user_in.username}' NOT found.")
        return False # User not found
    
    print(f"DEBUG: User found: {user.username}")
    # SECURITY NOTE: Never print user passwords in a real application!
    print(f"DEBUG: Input Password: {user_in.password}") 
    print(f"DEBUG: Stored Hash: {user.hashed_password}")
    
    # 2. Verify the password
    if not verify_password(user_in.password, user.hashed_password):
        print("DEBUG: Password VERIFICATION FAILED.")
        return False # Password mismatch
        
    print("DEBUG: Password VERIFICATION SUCCESSFUL.")
    # 3. Credentials are valid
    return user