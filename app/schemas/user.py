# app/schemas/user.py

from pydantic import BaseModel

# ------------------------------------------------------
# Common fields shared between create/read schemas
# ------------------------------------------------------
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    fullname: str


# ------------------------------------------------------
# Schema for creating a new user
# ------------------------------------------------------
class UserCreate(UserBase):
    password: str  # Plain password from the client


# ------------------------------------------------------
# Schema for reading user data (response model)
# ------------------------------------------------------
class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True  # Converts SQLAlchemy model -> Pydantic model
        orm_mode = True
