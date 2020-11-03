from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os

APP_URL = 'http://127.0.0.1:5000/'
DB_HOST = 'localhost'
DB_PORT = 3307
DB_USER = 'user'
DB_PASSWORD = 'dupa'
DB_NAME = 'my_db'
ECHO = 'false'

ECHO = os.environ.get('ECHO', 'false') == 'true'

CONNECTION_STRING = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(CONNECTION_STRING, echo=ECHO)
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()


def before_all(context):
    context.session = get_session()
    context.app_url = {APP_URL}
