from fastapi import APIRouter, Request, Depends, status, Response, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from api.db.session import get_db
from api.routes.login import login_for_access_token
from api.repository import users as users_crud
from api.schemas import users as users_shemas
from api.security.security import authenticate_user, create_access_token, get_current_user, is_token


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")
router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/welcome")
def welcome(request: Request,
            current_user: users_shemas.User = Depends(get_current_user)):
    return templates.TemplateResponse("home.html", {"request":request})