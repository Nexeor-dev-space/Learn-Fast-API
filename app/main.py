from fastapi import FastAPI
app = FastAPI(title = "ToDo API")

@app.get("/")
async def root():
    return {"status": "ok"}