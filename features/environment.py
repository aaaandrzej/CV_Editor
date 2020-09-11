from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os

APP_URL = 'http://127.0.0.1:5000/'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_ROOT_USER = 'root'
DB_ROOT_PASSWORD = 'root'
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_NAME = 'my_db'
ECHO = 'false'
# DB_HOST = os.environ['DB_HOST']
# DB_PORT = os.environ['DB_PORT']
# DB_ROOT_USER = os.environ['DB_ROOT_USER']
# DB_ROOT_PASSWORD = os.environ['DB_ROOT_PASSWORD']
# # DB_USER = os.environ['DB_USER']
# # DB_PASSWORD = os.environ['DB_PASSWORD']
# DB_NAME = os.environ['DB_NAME']

ECHO = os.environ.get('ECHO', 'false') == 'true'

engine = create_engine(f'mysql+pymysql://{DB_ROOT_USER}:{DB_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=ECHO)
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()


def before_all(context):
    context.session = get_session()
    context.app_url = {APP_URL}
