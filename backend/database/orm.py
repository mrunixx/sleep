import dotenv
from sqlmodel import SQLModel, Field, Column, JSONB
from backend.database.conn import get_session
from typing import Dict, Any

class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id: int = Field(primary_key=True)
    firstname: str = Field(nullable=False)
    lastname: str = Field(nullable=False)
    email: str = Field(unique=True)
    hpassword: str

class Session(SQLModel, table=True):
    __tablename__ = "sessions"
    __table_args__ = {"schema": "auth"}

    token: str = Field(primary_key=True)
    user_id: int = Field(nullable=False)
    user_info: Dict[str, Any] = Field(sa_column=Column(JSONB))