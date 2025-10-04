from typing import Union
from fastapi import FastAPI, Depends, Header

# import request, return, etc. types from respective path folders
from backend.auth.utypes import UserCreateRequest, UserTokenResponse, UserLoginRequest

# import utility functions
from backend.utils.serverutils import extract_token_from_header

# import core logic functions
from backend.auth.logic import AuthLogic

app = FastAPI()
authLogic = AuthLogic()

# server data structures
expired_tokens = set()

@app.get("/")
def read_root():
    return {"message": "You have accessed the root!"}

@app.post("/v1/auth/user/create")
def user_create(req: UserCreateRequest) -> UserTokenResponse:
    return authLogic.user_create(req)

@app.post("/v1/auth/user/login")
def user_login(req: UserLoginRequest) -> UserTokenResponse:
    return authLogic.user_login(req)

@app.post("/v1/auth/user/logout")
def user_logout(token: str = Depends(extract_token_from_header)):
    expired_tokens.add(token)
    return {'message': 'Logout successful.'}

@app.post("/v1/sleep/entry")
def sleep_entry(token: str = Depends(extract_token_from_header)):
    return authLogic.user_logout(token)

@app.get("/v1/sleep/score")
def sleep_score(access_token: str):
    pass