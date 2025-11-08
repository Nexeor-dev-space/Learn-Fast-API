# app/schemas/user.py

from pydantic import BaseModel

# ------------------------------------------------------
# Common fields shared between create/read schemas
# ------------------------------------------------------
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
class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True  # Converts SQLAlchemy model -> Pydantic model
