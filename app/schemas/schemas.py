from pydantic import BaseModel,ConfigDict
 
class UserBase(BaseModel):
    username: str
    fullname: str

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    username:str
    password:str

class UserRead(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
