from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    fullname: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    fullname: str

    class Config:
        orm_mode = True