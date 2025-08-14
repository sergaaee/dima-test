from fastapi import APIRouter
from pydantic import EmailStr

from services.user import (
    get_user_by_email,
    delete_user,
)
from schemas.user import UserOut, UserLogin, UserGet
from db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

from exceptions.user import UserNotFoundError
from utils import get_current_user

router = APIRouter()


@router.get("", response_model=UserGet)
def get_me(db: Session = Depends(get_db), current_user: UserLogin = Depends(get_current_user)):
    user = get_user_by_email(current_user.email, db)
    if not user:
        raise UserNotFoundError()

    return user


@router.delete("", response_model=dict)
def delete_me(email: EmailStr, db: Session = Depends(get_db)):
    return delete_user(email, db)
