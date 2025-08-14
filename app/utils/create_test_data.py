from datetime import datetime, timedelta

from db import models
from db.database import SessionLocal
from .hashing import hash


def create_test_data(db: SessionLocal):
    """Создает тестовые данные: 2 пользователя, по 2 счета и по 3 транзакции для каждого счета."""
    if db.query(models.User).count() > 0:
        return

    users = [
        models.User(
            full_name="John Doe",
            email="john.doe@example.com",
            hashed_password=hash("password123"),
            priveliges_type="user"
        ),
        models.User(
            full_name="Jane Smith",
            email="jane.smith@example.com",
            hashed_password=hash("password456"),
            priveliges_type="admin"
        )
    ]
    db.add_all(users)
    db.commit()

    accounts = []
    for user in users:
        accounts.extend([
            models.Account(balance=1000, user_id=user.id),
            models.Account(balance=2000, user_id=user.id)
        ])
    db.add_all(accounts)
    db.commit()

    transactions = []
    for account in accounts:
        transactions.extend([
            models.Transaction(
                external_id=f"txn_{account.id}_1",
                amount=100,
                signature="sig123",
                date=datetime.utcnow() - timedelta(days=2),
                account_id=account.id,
                user_id=account.user_id
            ),
            models.Transaction(
                external_id=f"txn_{account.id}_2",
                amount=200,
                signature="sig456",
                date=datetime.utcnow() - timedelta(days=1),
                account_id=account.id,
                user_id=account.user_id
            ),
            models.Transaction(
                external_id=f"txn_{account.id}_3",
                amount=300,
                signature="sig789",
                date=datetime.utcnow(),
                account_id=account.id,
                user_id=account.user_id
            )
        ])
    db.add_all(transactions)
    db.commit()