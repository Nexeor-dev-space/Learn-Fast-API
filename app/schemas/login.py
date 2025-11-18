# app/schemas/login.py
from pydantic import BaseModel
from app.schemas.register import UserRead

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    user: UserRead
    access_token: str
    token_type: str
