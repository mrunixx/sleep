from typing import Union
from fastapi import FastAPI

# import request, return, etc. types from respective path folders
from backend.auth.utypes import UserCreateRequest

# import core logic functions
from backend.auth.logic import AuthLogic

app = FastAPI()

authLogic = AuthLogic()

@app.get("/")
def read_root():
    return {"message": "You have accessed the root!"}

@app.post("/v1/auth/user/create")
def user_create(req: UserCreateRequest):
    return authLogic.user_create(req)

@app.put("/v1/auth/user/login")
def user_login():
    pass

@app.put("/v1/auth/user/logout")
def user_logout():
    pass

@app.post("/v1/sleep/{user_id}/entry")
def sleep_entry(user_id: int, ):
    pass

@app.get("/v1/sleep/{user_id}/score")
def sleep_score():
    pass