# app/main.py
from fastapi import FastAPI

app = FastAPI(title="My FastAPI Project")

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}
