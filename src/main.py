import uvicorn
from fastapi import FastAPI

from src.routers import expense_router

app = FastAPI()

app.include_router(expense_router.router)


@app.get("/")
async def root():
    return {"message": "First Update!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
