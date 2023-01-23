from fastapi import APIRouter
from . import users, login

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(login.router, prefix="/login", tags=["login"])