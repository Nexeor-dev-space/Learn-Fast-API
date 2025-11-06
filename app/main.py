from fastapi import FastAPI
from app.db import config  # ensure this path matches your folder structure

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI is running!!"}
