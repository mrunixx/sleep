from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime
from datetime import datetime


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
    user_firstname: str = Field(nullable=False)
    user_lastname: str = Field(nullable=False)
    user_email: str = Field(nullable=False)


class SleepEntry(SQLModel, table=True):
    __tablename__ = "entry"
    __table_args__ = {"schema": "sleep"}

    id: int = Field(primary_key=True)
    user_id: int = Field(nullable=False)
    start_dt_utc: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    end_dt_utc: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    sleep_time_s: int = Field(nullable=False)
    tz_name: str = Field(nullable=False)
