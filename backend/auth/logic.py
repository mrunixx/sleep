from .types import UserCreateRequest
from passlib.context import CryptContext

class AuthLogic:
    def __init__(self):
        self.hasher = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def userCreate(self, req: UserCreateRequest):
        hashed_password = self.hasher.hash(req.password)
        
