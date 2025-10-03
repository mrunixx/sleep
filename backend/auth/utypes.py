from pydantic import BaseModel

class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str