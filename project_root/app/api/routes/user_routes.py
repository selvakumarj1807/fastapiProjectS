# user_routes.py
from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserModel
from app.services.user_service import register_user, login_user

router = APIRouter()

@router.post("/register/")
async def register(user: UserModel):
    return await register_user(user)

@router.post("/login/")
async def login(email: str, password: str):
    return await login_user(email, password)
