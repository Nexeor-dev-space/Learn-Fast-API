<<<<<<< HEAD
# C:\MyProjects\Learn-Fast-API\app\main.py

from fastapi import FastAPI
from app.routes import auth
=======
from fastapi import FastAPI
from app.routes import auth
# FIX: Import async_engine instead of engine
from app.db.database import Base, async_engine

async def create_db_and_tables():
    """Drops existing tables and recreates them based on Base.metadata."""
    # FIX: Use async_engine here too
    async with async_engine.begin() as conn:
        print("INFO: Dropping all tables...")
        await conn.run_sync(Base.metadata.drop_all)
        print("INFO: Creating all tables...")
        await conn.run_sync(Base.metadata.create_all)
    print("INFO: Database initialized successfully.")
>>>>>>> dea0a3e (feat(issue-6): Implement login and JWT-based authentication)

app = FastAPI(title="FastAPI Project")

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Application"}