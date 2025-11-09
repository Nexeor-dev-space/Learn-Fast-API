from typing import Union
from app.routes import users
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"fastapi": "sucessfully working"}


app.include_router(
    users.router,
    prefix="/api/v1",
    tags=["users"],)