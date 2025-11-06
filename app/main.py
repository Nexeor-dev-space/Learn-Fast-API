from fastapi import FastAPI
from app.routes import user,todo
app = FastAPI()
app.include_router(user.router)
app.include_router(todo.crud)
@app.get("/")
async def root():
    return {"greeting":"Hello world"}