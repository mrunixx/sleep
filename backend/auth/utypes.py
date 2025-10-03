from pydantic import BaseModel

class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str

class UserTokenResponse(BaseModel):
    access_token: str
    token_type: str

class UserLoginRequest(BaseModel):
    email: str
    password: str