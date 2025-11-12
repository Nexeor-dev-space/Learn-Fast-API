# app/main.py

from fastapi import FastAPI
from app.routes import auth
# CHANGE from async_engine to engine
from app.db.database import Base, engine 


# Temporary function to drop and create all tables
async def create_db_and_tables():
    """Drops existing tables and recreates them based on Base.metadata."""
    # Note: In production, you would only use Alembic for migrations!
    async with engine.begin() as conn: # <-- USE 'engine' HERE TOO
        print("INFO: Dropping all tables...")
        await conn.run_sync(Base.metadata.drop_all)
        print("INFO: Creating all tables...")
        await conn.run_sync(Base.metadata.create_all)
    print("INFO: Database initialized successfully.")

app = FastAPI(title="FastAPI Project")

# Register the startup event
@app.on_event("startup")
async def startup_event():
    await create_db_and_tables()

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Application"}