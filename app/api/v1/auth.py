from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from utils import verify
from services.auth import register_user
from services.user import get_user_by_email
from core.security import create_access_token
from schemas.user import UserCreate, UserLogin, UserOut
from db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import timedelta

from exceptions.user import UserAlreadyExistsError

router = APIRouter()


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
) -> dict:
    db_user = get_user_by_email(email=form_data.username, db=db)
    if not db_user:
        raise HTTPException(status_code=401, detail="Неверный email")
    if not verify(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Неверный пароль")

    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer", "user": UserOut.model_validate(db_user)}


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(user.email, db)
    if db_user:
        raise UserAlreadyExistsError()

    new_user = register_user(user, db)

    token = create_access_token({"sub": new_user.email}, timedelta(minutes=60))
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {"id": new_user.id, "email": new_user.email},
    }
