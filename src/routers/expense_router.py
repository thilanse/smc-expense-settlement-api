from fastapi import APIRouter

from src.models.expense import Expense

router = APIRouter()


@router.get("/expenses/", tags=["Expense Controller"])
async def read_users():
    expense = Expense("bowling")
    return expense


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
