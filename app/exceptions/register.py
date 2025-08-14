from fastapi import FastAPI
from exceptions.user import register_user_exception_handlers

def register_exception_handlers(app: FastAPI):
    register_user_exception_handlers(app)
