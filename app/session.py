from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def get_session(echo: bool = False) -> Session:
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/my_db', echo=echo)
    session_factory = sessionmaker(bind=engine)

    return session_factory()
