from pydantic import BaseModel, EmailStr, ConfigDict
from sqlalchemy import DateTime

from db import Account, Transaction
from schemas.schemas_extra import user_get_config, user_login_config, transaction_get_config, user_create_config, \
    account_get_config


class AccountGet(BaseModel):
    model_config = account_get_config
    id: int
    balance: int
    user_id: int

class TransactionGet(BaseModel):
    model_config = transaction_get_config

    id: int
    external_id: str
    amount: int
    signature: str
    date: DateTime
    account_id: int
    user_id: int


class UserCreate(BaseModel):
    model_config = user_create_config

    email: EmailStr
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr


class UserLogin(BaseModel):
    model_config = user_login_config

    email: EmailStr
    password: str


class UserGet(BaseModel):
    model_config = user_get_config

    id: str
    email: EmailStr
    accounts: list[Account]
    transactions: list[Transaction]


class Token(BaseModel):
    access_token: str
    token_type: str
