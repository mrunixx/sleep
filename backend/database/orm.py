from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id: int = Field(primary_key=True)
    firstname: str = Field(nullable=False)
    lastname: str = Field(nullable=False)
    email: str = Field(unique=True)
    tz: str = Field(nullable=False)
    hpassword: str


class Session(SQLModel, table=True):
    __tablename__ = "sessions"
    __table_args__ = {"schema": "auth"}

    token: str = Field(primary_key=True)
    user_id: int = Field(nullable=False)
    user_firstname: str = Field(nullable=False)
    user_lastname: str = Field(nullable=False)
    user_email: str = Field(nullable=False)
