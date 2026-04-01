from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

async def create_task(db: AsyncSession, owner_id: int, task_in: TaskCreate) -> Task:
    task = Task(
        title=task_in.title,
        description=task_in.description,
        completed=task_in.completed,
        owner_id=owner_id,
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_tasks_for_user(db: AsyncSession, owner_id: int) -> list[Task]:
    result = await db.execute(select(Task).where(Task.owner_id == owner_id))
    return list(result.scalars().all())

async def get_task_by_id(db: AsyncSession, task_id: int, owner_id: int) -> Task | None:
    result = await db.execute(
        select(Task).where(Task.id == task_id, Task.owner_id == owner_id)
    )
    return result.scalar_one_or_none()

async def update_task(db: AsyncSession, task: Task, task_in: TaskUpdate) -> Task:
    if task_in.title is not None:
        task.title = task_in.title
    if task_in.description is not None:
        task.description = task_in.description
    if task_in.completed is not None:
        task.completed = task_in.completed

    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, task: Task) -> None:
    await db.delete(task)
    await db.commit()
