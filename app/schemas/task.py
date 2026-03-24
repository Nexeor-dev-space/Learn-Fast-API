from datetime import datetime
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    owner_id: int
    created_at: datetime

    model_config = {"from_attributes": True}

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None