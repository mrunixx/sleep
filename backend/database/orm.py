import dotenv
from sqlmodel import SQLModel, Field
from conn import get_session

class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id: int = Field(primary_key=True)
    firstname: str
    lastname: str
    email: str
    hpassword: str