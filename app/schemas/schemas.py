from pydantic import BaseModel
 
class UserBase(BaseModel):
    username: str
    fullname: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
class Config:
    orm_model=True