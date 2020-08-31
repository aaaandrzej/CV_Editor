from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import pymysql.cursors
import os

DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_ROOT_USER = os.environ['DB_ROOT_USER']
DB_ROOT_PASSWORD = os.environ['DB_ROOT_PASSWORD']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']

ECHO = os.environ.get('ECHO', 'false') == 'true'

engine = create_engine(f'mysql+pymysql://{DB_ROOT_USER}:{DB_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=ECHO)
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()


# Connect to the database to use pure SQL
connection = pymysql.connect(host=DB_HOST,
                             user=DB_ROOT_USER,
                             password=DB_ROOT_PASSWORD,
                             db=DB_NAME,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)
