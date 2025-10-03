from typing import Union
from fastapi import FastAPI

# import request, return, etc. types from respective path folders
from auth.types import UserCreateRequest

# import core logic functions
from auth.types import 
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "You have accessed the root!"}

@app.post("/v1/auth/user/create")
def user_create(req: UserCreateRequest):
    pass

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