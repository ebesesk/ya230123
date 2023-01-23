from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..schemas.users import UserCreate, ShowUser
from ..models.users import User
from ..security.security import get_current_user_from_token
from ..repository import users as users_crud

router = APIRouter()

@router.post("/create_user", response_model=ShowUser)
def create_user(
    _user_create: UserCreate,
    db: Session = Depends(get_db)
    ):
    user = users_crud.get_existing_users(_user_create, db)
    print(_user_create.username, _user_create.password, '------------------------------')
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    user = users_crud.create_user(_user_create, db)
    return user
