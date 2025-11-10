# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from app.db.database import get_db, Base, engine
from app.db.models import User
from app.schemas.user import UserCreate
from app.db.init_data import init_data  # ✅ make sure ye path sahi hai
from fastapi import FastAPI
from app.db import config  # ensure this path matches your folder structure

# ✅ Database tables create karo
Base.metadata.create_all(bind=engine)

# ✅ Lifespan event — startup par default data insert karega
@asynccontextmanager
async def lifespan(app: FastAPI):
    db = next(get_db())
    init_data(db)
    db.close()
    yield

# ✅ FastAPI app initialize with lifespan
app = FastAPI(lifespan=lifespan)


# ✅ Root endpoint
@app.get("/")
def read_root():
    return {"message": "FastAPI with Alembic and PostgreSQL connected successfully!"}


# ✅ Create new user (POST)
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        fullname=user.fullname,
        hashed_password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully!", "user": new_user.username}


# ✅ Get all users (GET)
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
async def read_root():
    return {"message": "Hello, FastAPI is running!!"}
