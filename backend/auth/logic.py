# logic + helpers
from backend.auth.utypes import UserCreateRequest
import bcrypt
from backend.database.orm import User
from backend.database.conn import get_session
import re

# fast api imports
from fastapi import HTTPException

class AuthLogic:
    def __init__(self):
        self.email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        self.pw_regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

    def user_create(self, req: UserCreateRequest):
        if not re.match(self.email_regex, req.email):
            return HTTPException(
                422,
                detail="Email does not match required format (e.g user@example.com)"
            )
        elif not re.match(self.pw_regex, req.password):
            return HTTPException(
                422,
                detail="Password does not match required format (atleast 8 characters, 1 letter, 1 number)"
            )

        hashed_password = bcrypt.hashpw(req.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

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

        # return the new users id
        return {'user_id': new_user.id}
