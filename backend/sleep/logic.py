# function imports
from backend.sleep.utypes import SleepEntryRequest
from backend.database.orm import User, Session
from backend.auth.logic import AuthLogic

from backend.database.orm import User, Session
from backend.database.conn import get_session
from dotenv import load_dotenv
from sqlmodel import select
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from pathlib import Path

# fast api imports
from fastapi import HTTPException

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

class SleepLogic:
    def sleep_entry(token, req: SleepEntryRequest):
        userId = AuthLogic.validate_access_token(token)

        user = Session.exec(select(User).where(User.id == userId)).first()
        # user = Session.exec(select(User).where(sleep.user_id == userId)).first()



