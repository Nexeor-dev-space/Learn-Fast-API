from datetime import datetime
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    completed: bool | None = None

class TaskRead(TaskBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True
