from pydantic import BaseModel
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False  

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True  

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None  
