from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends
from fastapi import APIRouter, HTTPException, status
from fastapi import Response
# from fastapi.security.utils import get_authorization_scheme_param

from sqlalchemy.orm import Session
# from jose import jwt, JWTError
# from datetime import timedelta

from ..db.session import get_db
from ..security.security import authenticate_user
from ..security.security import create_access_token


# from core.config import settings
# from apis.utils.security import OAuth2PasswordBearerWithCookie
# from db.repository.login import get_user
# from core.hashing import Hasher


router = APIRouter()

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)
                         # response: Response,
                           ):
    user = authenticate_user(username=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token = create_access_token(data={"sub": user.username})
    # response.set_cookie( key="access_token", 
    #                      value=f"Bearer {access_token}", 
    #                      httponly=True)
    return {"access_token": access_token, "token_type": "bearer"}
        