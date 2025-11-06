from fastapi import APIRouter,Depends,HTTPException, status,Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas import *
from app.auth.login import create_access_token, get_current_user
from app.models.models import Todo
from app.db.database import get_async_db
from sqlalchemy.future import select
from typing import List,Optional

crud=APIRouter(prefix="/task",tags=["Task"])

@crud.post("/create", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(task_in: TaskCreate,db: AsyncSession = Depends(get_async_db),current_user: Todo = Depends(get_current_user),):
    if task_in.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot create task for another user")

    new_task = Todo(
        title=task_in.title,
        description=task_in.description,
        completed=task_in.completed,
        owner_id=current_user.id
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

@crud.post("/list", response_model=List[TaskRead])
async def list_tasks_paginated(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    query: Optional[str] = Query("", description="Filter by title substring"),
    db: AsyncSession = Depends(get_async_db),
    current_user: Todo = Depends(get_current_user),):
    offset = (page - 1) * limit

    stmt = select(Todo).where(Todo.owner_id == current_user.id)
    if query:
        stmt = stmt.where(Todo.title.ilike(f"%{query}%"))

    result = await db.execute(stmt.limit(limit).offset(offset))
    tasks = result.scalars().all()
    return tasks

@crud.put("/update/{task_id}", response_model=TaskRead)
async def update_task(task_id: int,task_in: TaskUpdate,db: AsyncSession = Depends(get_async_db),current_user: Todo = Depends(get_current_user),):
    result = await db.execute(select(Todo).where(Todo.id == task_id, Todo.owner_id == current_user.id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    update_data = task_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    await db.commit()
    await db.refresh(task)
    return task

@crud.delete("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int,db: AsyncSession = Depends(get_async_db),current_user: Todo = Depends(get_current_user),):
    result = await db.execute(select(Todo).where(Todo.id == task_id, Todo.owner_id == current_user.id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    await db.delete(task)
    await db.commit()
    return None