from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exceptions.user.errors import UserNotFoundError, UserAlreadyExistsError, PermissionDeniedError


def register_user_exception_handlers(app: FastAPI):
    @app.exception_handler(UserNotFoundError)
    def user_not_found_handler(request: Request, exc: UserNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"error": "user_not_found", "detail": str(exc)},
        )

    @app.exception_handler(UserAlreadyExistsError)
    def user_exists_handler(request: Request, exc: UserAlreadyExistsError):
        return JSONResponse(
            status_code=409,
            content={"detail": str(exc), "error": "user_already_exists"},
        )

    @app.exception_handler(PermissionDeniedError)
    def user_permission_denied_handler(request: Request, exc: PermissionDeniedError):
        return JSONResponse(
            status_code=403,
            content={"error": "user_permission_denied", "detail": str(exc)},
        )
