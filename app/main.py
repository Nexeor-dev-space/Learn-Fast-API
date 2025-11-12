# C:\MyProjects\Learn-Fast-API\app\main.py

from fastapi import FastAPI
from app.routes import auth

app = FastAPI(title="FastAPI Project")

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Application"}