from fastapi import APIRouter
from . import auth, welcome

router = APIRouter()
router.include_router(auth.router)
router.include_router(welcome.router)
