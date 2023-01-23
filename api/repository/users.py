from sqlalchemy.orm import Session
from ..schemas.users import UserCreate
from ..models.users import User
from ..security.hashing import Hasher


def get_existing_users(_user: UserCreate, db: Session):
    return db.query(User).filter(User.username == _user.username).first()


def get_user(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user

def create_user(_user_create: UserCreate, db:Session):
    user = User(
        username = _user_create.username,
        hashed_password=Hasher.get_hash_password(_user_create.password),
    )
    db.add(user)
    db.commit()
    # db.refresh(user)
    return user 