from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import Users,Todo
from app.schemas.schemas import *
from app.db.database import get_async_db
from app.auth.login import create_access_token, get_current_user
from typing import List
import bcrypt

router=APIRouter(prefix="/auth",tags=["Authentication"])
crud=APIRouter(prefix="/task",tags=["Task"])

@router.post("/register")
async def validate_user(users:UserCreate,db: AsyncSession = Depends(get_async_db)):
    try:
        result = await db.execute(select(Users).where(Users.username == users.username))
        existing_user = result.scalar_one_or_none()    
        if existing_user:
            raise HTTPException(status_code=400,detail="Username already exists")
        new_user=Users(username=users.username,fullname=users.fullname)
        new_user.set_password(users.password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return {"message": "User registered successfully", "username": new_user.username}
    except:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Database integrity error (possible duplicate username)")

@router.post("/login")
async def login(entry: UserLogin, db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(select(Users).where(Users.username == entry.username))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username")
    if not bcrypt.checkpw(entry.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid password")
    access_token = create_access_token({"sub": user.username})
    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "username": user.username,
            "fullname": user.fullname
        }
    }

@router.get("/me")
async def get_me(current_user: Users = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "fullname": current_user.fullname
    }

@crud.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(task_in: TaskCreate,db: AsyncSession = Depends(get_async_db),current_user: Users = Depends(get_current_user),):
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

@crud.get("/", response_model=List[TaskRead])
async def get_tasks(db: AsyncSession = Depends(get_async_db),current_user: Users = Depends(get_current_user),):
    result = await db.execute(select(Todo).where(Todo.owner_id == current_user.id))
    tasks = result.scalars().all()
    return tasks

@crud.put("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int,task_in: TaskUpdate,db: AsyncSession = Depends(get_async_db),current_user: Users = Depends(get_current_user),):
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

@crud.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int,db: AsyncSession = Depends(get_async_db),current_user: Users = Depends(get_current_user),):
    result = await db.execute(select(Todo).where(Todo.id == task_id, Todo.owner_id == current_user.id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    await db.delete(task)
    await db.commit()
    return None