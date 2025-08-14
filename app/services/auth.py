from pydantic import EmailStr
from sqlalchemy.orm import Session
from db import models
from schemas import user as user_schema
from utils import hash, verify
from core.security import create_access_token
from datetime import timedelta
from fastapi import HTTPException

from exceptions.user.errors import UserNotFoundError


def register_user(user: user_schema.UserCreate, db: Session):
    new_user = models.User(email=user.email, hashed_password=hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user(user: user_schema.UserLogin, db: Session):
    db_user = db.query(models.User).filter_by(username=user.username).first()
    if not db_user or not verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email}, timedelta(minutes=60))
    return token


def get_user_by_email(email: EmailStr, db: Session):
    return db.query(models.User).filter_by(email=email).first()


def delete_user(email: EmailStr, db: Session):
    db_user = get_user_by_email(email, db)
    if not db_user:
        raise UserNotFoundError()
    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted successfully"}
