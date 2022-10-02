from fastapi import FastAPI

from src.routers import expense_router

app = FastAPI()

app.include_router(expense_router.router)


@app.get("/")
async def root():
    return {"message": "First Update!"}