from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    fullname: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    fullname: str

    model_config = {
        "from_attributes": True  # enable ORM support in Pydantic v2
    }
