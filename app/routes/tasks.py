from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user
from app.db.deps import get_db
from app.models.user import User
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.services.task_service import (
    create_task,
    get_tasks_for_user,
    get_task_by_id,
    update_task,
    delete_task,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task_route(
    task_in: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await create_task(db, current_user.id, task_in)

@router.get("/", response_model=list[TaskRead])
async def list_tasks_route(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await get_tasks_for_user(db, current_user.id)

@router.put("/{task_id}", response_model=TaskRead)
async def update_task_route(
    task_id: int,
    task_in: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await get_task_by_id(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await update_task(db, task, task_in)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_route(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await get_task_by_id(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await delete_task(db, task)
    return None
