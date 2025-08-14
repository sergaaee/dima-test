import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    PROJECT_NAME = "TestDima"
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()
