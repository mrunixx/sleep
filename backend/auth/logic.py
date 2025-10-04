# function imports
from backend.auth.utypes import (
    UserCreateRequest,
    UserTokenResponse,
    UserLoginRequest,
    UserLogoutResponse,
)
from backend.database.orm import User, Session
from backend.database.conn import get_session
from dotenv import load_dotenv
from sqlmodel import select
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from pathlib import Path

# package imports
import bcrypt
import re
import os

# fast api imports
from fastapi import HTTPException

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)


class AuthLogic:
    def __init__(self):
        self.email_regex = re.compile(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        )
        self.pw_regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        self.secret_key = os.getenv("SECRET_KEY")
        self.algo = os.getenv("ALGORITHM")

    def create_access_token(self, user_id: int) -> jwt:
        """
        Creates a JWT with the user id as the subject
        """
        expire = datetime.now(timezone.utc) + timedelta(minutes=60)
        payload = {"sub": str(user_id), "exp": expire.timestamp()}
        return jwt.encode(payload, self.secret_key, self.algo)

    def validate_access_token(self, access_token: str) -> int:
        """
        Returns the user ID
        """
        try:
            payload = jwt.decode(access_token, self.secret_key, algorithms=[self.algo])
            user_id = payload.get("sub")
            if user_id is None:
                raise HTTPException(
                    status_code=401, detail="Invalid token: missing subject"
                )
            return int(user_id)
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

    def user_create(self, req: UserCreateRequest) -> UserTokenResponse:
        if not re.match(self.email_regex, req.email):
            return HTTPException(
                422,
                detail="Email does not match required format",
            )
        elif not re.match(self.pw_regex, req.password):
            return HTTPException(
                422,
                detail="Password does not match required format",
            )

        hashed_password = bcrypt.hashpw(
            req.password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        new_user = User(
            firstname=req.first_name,
            lastname=req.last_name,
            email=req.email,
            hpassword=hashed_password
        )

        # insert and commit the new user
        with get_session() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

        # create jwt
        new_user_jwt = self.create_access_token(new_user.id)

        # create new session
        new_session = Session(
            token=new_user_jwt,
            user_id=new_user.id,
            user_email=new_user.email,
            user_firstname=new_user.firstname,
            user_lastname=new_user.lastname,
        )

        # commit the new session
        with get_session() as session:
            session.add(new_session)
            session.commit()

        return {
            "access_token": new_user_jwt,
            "token_type": "bearer",
            "user_firstname": new_user.firstname,
            "user_lastname": new_user.lastname,
            "user_email": new_user.email,
        }

    def user_login(self, req: UserLoginRequest) -> UserTokenResponse:
        with get_session() as session:
            user = session.exec(select(User).where(User.email == req.email)).first()
            if not user:
                raise HTTPException(
                    status_code=401, detail="Email does not exist in database"
                )

        if not bcrypt.checkpw(
            req.password.encode("utf-8"), user.hpassword.encode("utf-8")
        ):
            raise HTTPException(status_code=401, detail="Incorrect password")

        user_jwt = self.create_access_token(user.id)

        new_session = Session(
            token=user_jwt,
            user_id=user.id,
            user_firstname=user.firstname,
            user_lastname=user.lastname,
            user_email=user.email,
        )

        with get_session() as session:
            session.add(new_session)
            session.commit()

        return {
            "access_token": user_jwt,
            "token_type": "bearer",
            "user_firstname": user.firstname,
            "user_lastname": user.lastname,
            "user_email": user.email,
        }

    def user_logout(self, token: str) -> UserLogoutResponse:
        with get_session() as session:
            print(token)
            curr_session = session.exec(
                select(Session).where(Session.token == token)
            ).first()

            if not curr_session:
                raise HTTPException(status_code=404, detail="Session not found")

            session.delete(curr_session)
            session.commit()

        return UserLogoutResponse(message="Successfully logged out.")
