from pydantic import BaseModel
 
class UserCreate(BaseModel):
    id:str
    username:str
    fullname:str
    password:str
class UserRead(UserCreate):
    pass 