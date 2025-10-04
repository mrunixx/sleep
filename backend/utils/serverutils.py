from fastapi import Depends, Header, HTTPException
from backend.auth.logic import AuthLogic


def extract_token_from_header(Authorization: str = Header(...)):
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    token = Authorization.split(" ")[1]
    return token
