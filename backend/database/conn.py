from contextlib import contextmanager
from sqlmodel import Session, create_engine
from dotenv import load_dotenv
from pathlib import Path
import os

# safe way to get the .env path, incase you run the script from outside
# the folder this file is in
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

# need to remember to add your own database url into .env
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)


# generator function that allows you to re-use the same engine
@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        # always closes the session even in exceptions (?)
        session.close()
