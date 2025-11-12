# C:\MyProjects\Learn-Fast-API\app\schemas\user.py

from pydantic import BaseModel

# --- Registration Schemas (MISSING) ---
class UserBase(BaseModel):
    username: str
    fullname: str

class UserIn(UserBase):
    """Schema for incoming registration data."""
    password: str

class UserOut(UserBase):
    """Schema for user data returned to the client (without password)."""
    id: int
    
    class Config:
        from_attributes = True

# --- Login Schemas (You already have these) ---
class UserLogin(BaseModel):
    """Schema for user login credentials."""
    username: str
    password: str 

class Token(BaseModel):
    """Schema for the JWT token response."""
    access_token: str
    token_type: str = "bearer"