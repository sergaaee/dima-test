from sqlalchemy.orm import Session
from db import models
from schemas import user as user_schema
from utils import hash, verify
from core.security import create_access_token
from datetime import timedelta
from fastapi import HTTPException


def register_user(user: user_schema.UserCreate, db: Session):
    new_user = models.User(email=user.email, full_name=user.full_name, hashed_password=hash(user.password), priveliges_type="Regular")
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
