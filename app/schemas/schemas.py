from pydantic import BaseModel,ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    fullname: str
    password: str

class UserLogin(UserBase):
    password:str

class UserRead(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TaskCreate(BaseModel):
    id:int
    title:str
    description:str
    created_at:datetime

class TaskUpdate(TaskCreate):
    pass

class TaskRead(TaskCreate):
    model_config = ConfigDict(from_attributes=True)
