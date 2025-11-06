from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    fullname: str
    password: str  # raw password, will hash before saving

class UserRead(BaseModel):
    id: int
    username: str
    fullname: str

    class Config:
        orm_mode = True
