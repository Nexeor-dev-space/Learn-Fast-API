from pydantic import BaseModel

<<<<<<< HEAD
class UserCreate(BaseModel):
    username: str
    fullname: str
    password: str  # raw password, will hash before saving

class UserRead(BaseModel):
    id: int
    username: str
    fullname: str
=======
class UserBase(BaseModel):
    username: str
    fullname: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
>>>>>>> main-daminiyadav23

    class Config:
        orm_mode = True
