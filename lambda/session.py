from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from get_secret import get_secret

# CONNECTION_STRING = f"mysql+pymysql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
CONNECTION_STRING = f"mysql+pymysql://{os.environ['DB_USER']}:{get_secret()}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"

ECHO = os.environ.get('ECHO', 'false') == 'true'

engine = create_engine(CONNECTION_STRING, echo=ECHO)
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()
