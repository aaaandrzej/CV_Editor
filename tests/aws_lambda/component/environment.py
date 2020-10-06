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


# APP_URL = 'http://127.0.0.1:5000/'
DB_HOST = 'aszulc-db3.c6nhgfuujgle.us-east-2.rds.amazonaws.com'
DB_PORT = 3306
DB_USER = 'admin'
DB_PASSWORD = 'KnvB1ixsiYjNE5PvDsaD'
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
#     context.app_url = {APP_URL}
