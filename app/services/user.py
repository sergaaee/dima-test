from pydantic import EmailStr
from sqlalchemy.orm import Session

from db import models
from exceptions.user import UserNotFoundError


def get_user_by_email(email: EmailStr, db: Session):
    return db.query(models.User).filter_by(email=email).first()


def delete_user(email: EmailStr, db: Session):
    db_user = get_user_by_email(email, db)
    if not db_user:
        raise UserNotFoundError()
    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted successfully"}
