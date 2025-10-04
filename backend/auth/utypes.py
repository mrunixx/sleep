from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    tz: str


class UserTokenResponse(BaseModel):
    access_token: str
    token_type: str
    user_firstname: str
    user_lastname: str
    user_email: str


class UserLoginRequest(BaseModel):
    email: str
    password: str


class UserLogoutResponse(BaseModel):
    message: str
