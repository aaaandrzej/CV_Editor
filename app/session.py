from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']

ECHO = os.environ.get('ECHO', 'false') == 'true'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}', echo=ECHO)
# engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}', echo=ECHO)
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()
