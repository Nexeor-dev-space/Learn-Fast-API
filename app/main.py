from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.tasks import router as tasks_router

app = FastAPI(title = "ToDo API")

app.include_router(auth_router)
app.include_router(tasks_router)


@app.get("/")
async def root():
    return {"status": "ok"}