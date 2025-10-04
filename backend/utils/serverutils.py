from fastapi import Header, HTTPException
from backend.database.conn import get_session
from backend.database.orm import Session

from sqlmodel import select


def extract_token_from_header(Authorization: str = Header(...)):
    """
    extracts the authorization JWT from the header.
    """
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    token = Authorization.split(" ")[1]
    return token


def authenticate_token(access_token: str) -> int:
    """
    used to authenticate a token, and return the user id given the token.
    """
    with get_session() as session:
        curr_session = session.exec(
            select(Session).where(Session.token == access_token)
        ).first()

        if not curr_session:
            raise HTTPException(status_code=401, detail="Session does not exist")

        return curr_session.user_id
