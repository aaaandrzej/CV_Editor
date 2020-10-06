from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
# from aws_lambda.get_secret import get_secret

ENDPOINT_URL = 'http://localhost:4566'
REGION_NAME = 'us-east-2'
AWS_ACCESS_KEY_ID = 'testing'
AWS_SECRET_ACCESS_KEY = 'testing'
AWS_SECURITY_TOKEN = 'testing'
AWS_SESSION_TOKEN = 'testing'

ECHO = os.environ.get('ECHO', 'false') == 'true'

CONNECTION_STRING = f"mysql+pymysql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"

engine = create_engine(CONNECTION_STRING, echo=ECHO)
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()


def before_all(context):
    context.session = get_session()
