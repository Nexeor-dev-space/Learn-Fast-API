from pydantic import BaseModel

class Token(BaseModel):
    access_token: str 
    token_type: str = "bearer"

class TookenData(BaseModel):
    username: str | None = None