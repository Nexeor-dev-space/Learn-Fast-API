from pydantic import BaseModel, ConfigDict
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
    
    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None  
