from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import Base, engine
from contextlib import asynccontextmanager
from api.v1 import auth as auth_routes
from exceptions.register import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup...")
    try:
        from db import models
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully")
    except Exception as e:
        print(f"Error creating tables: {e}")
    yield
    print("Application shutdown...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Auth"])
