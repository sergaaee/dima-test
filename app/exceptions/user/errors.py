class ServiceError(Exception):
    pass

class UserNotFoundError(ServiceError):
    def __init__(self,):
        super().__init__(f"User not found")

class UserAlreadyExistsError(ServiceError):
    def __init__(self,):
        super().__init__(f"User with this email already exists")

class InvalidTokenError(ServiceError):
    pass

class PermissionDeniedError(ServiceError):
    def __init__(self,):
        super().__init__(f"You do not have permission to perform this action")
