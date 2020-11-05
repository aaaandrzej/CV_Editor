import logging
import os

from sqlalchemy.exc import DataError, IntegrityError
from werkzeug.security import generate_password_hash

from app.models import User
from app.session import get_session

session = get_session()

app_admin_user = User(username=os.environ['APP_USER'],
                      password=generate_password_hash(os.environ['APP_PASSWORD'], method='sha256', salt_length=8),
                      firstname=os.environ['APP_USER'][:2],
                      lastname=os.environ['APP_USER'][2:],
                      admin=True)

if __name__ == '__main__':
    session.add(app_admin_user)
    try:
        session.commit()
        print('admin user created')
    except (DataError, IntegrityError) as ex:
        logging.exception(ex)
        print('admin user already exists in db')
