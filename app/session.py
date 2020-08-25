from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
# import os
#
# DB_USER = os.getenv('DB_USER')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_NAME = os.getenv('DB_NAME')

# engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME')
engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/my_db')
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()
