from pydantic import BaseModel
 
class UserCreate(BaseModel):
    username:str
    fullname:str
    password:str
class UserRead(UserCreate):
    pass 