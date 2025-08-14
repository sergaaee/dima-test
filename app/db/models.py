from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    priveliges_type = Column(String)

    accounts = relationship("Account", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="accounts")

    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, unique=True)
    amount = Column(Integer)
    signature = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship("Account", back_populates="transactions")

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="transactions")

    __table_args__ = (
        Index('idx_user_id_external_id', 'user_id', 'external_id'),
        Index('idx_user_id_amount', 'user_id', 'amount'),
    )
