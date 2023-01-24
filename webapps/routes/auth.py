from fastapi import APIRouter, Request, Depends, Response, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from api.db.session import get_db
from api.security.security import authenticate_user, create_access_token, get_current_user, get_authorization_scheme_param
from api.routes.login import login_for_access_token


router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/")
def login(request: Request,
          db: Session=Depends(get_db),
          # current_user: users_schemas.User = Depends(get_current_user)
          ):
    try:
        authorization = request.cookies.get("access_token")
        scheme, param = get_authorization_scheme_param(authorization)
        user = get_current_user(token=param, db=db)
        return templates.TemplateResponse("home.html", {"request": request})        
    except HTTPException:
        return templates.TemplateResponse("user/login.html", {"request": request})

@router.post("/")
async def login(response: Response, 
                request: Request, 
                db: Session=Depends(get_db),
                ):
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    errors = []
    try:
        user = authenticate_user(username=username, password=password, db=db)
        if not user:
            errors.append("Username does not exists")
            return templates.TemplateResponse("user/login.html", {"request": request,"errors": errors})
        access_token = create_access_token(data={"sub": username})
        response = templates.TemplateResponse("home.html", {"request":request})
        response.set_cookie(key="access_token",
                            value=f"Bearer {access_token}",
                            httponly=True)
        return response
        
    except HTTPException:
        errors.append("Incorrect Username or password")
        return templates.TemplateResponse("user/login.html", {"request": request, "errors": errors})        