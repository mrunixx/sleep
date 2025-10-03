from contextlib import contextmanager
from sqlmodel import Session, create_engine
from dotenv import load_dotenv
import os

load_dotenv('../../.env')

# need to remember to add your own database url into .env
db_url = os.getenv('DATABASE_URL')
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