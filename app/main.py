from fastapi import FastAPI
from app.routes.register import router as register_router
from app.routes.login import router as login_router
from app.routes.user_routes import router as user_router

app = FastAPI(title="FastAPI Project")

# Include your actual routers
app.include_router(register_router)
app.include_router(login_router)
app.include_router(user_router)

@app.get("/")
def index():
    return {"Message": "Hello World!"}
