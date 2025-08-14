from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def hash(password: str) -> str:
    return pwd_context.hash(password)
