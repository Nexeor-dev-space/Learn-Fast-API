from fastapi import FastAPI

app = FastAPI(title="Learn FastAPI")

@app.get("/")
async def root():
    return {"message": "Welcome to Learn-Fast-API!"}
