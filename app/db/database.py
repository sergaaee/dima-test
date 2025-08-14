from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    print(f"Using database: {db.get_bind().url}")
    try:
        yield db
    finally:
        db.close()
