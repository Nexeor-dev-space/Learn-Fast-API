from fastapi import FastAPI
from app.routes.register import router as register_router
from app.routes.login import router as login_router
from app.routes.user_routes import router as user_router
from app.routes.task import router as task_router

app = FastAPI(title="FastAPI Project")

app.include_router(register_router)
app.include_router(login_router)
app.include_router(user_router)
app.include_router(task_router)

@app.get("/")
def index():
    return {"Message": "Hello World!"}