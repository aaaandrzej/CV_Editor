from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://postgres:postgres@localhost:5432/my_db')
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()
