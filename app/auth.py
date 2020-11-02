from functools import wraps
import os

import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError
from flask import request, jsonify
from sqlalchemy.orm.exc import NoResultFound

from app.models import User
from app.session import get_session


class ExpiredTokenError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


class MissingTokenError(Exception):
    pass


def extract_user():
    token = request.headers.get('Authorization')

    if not token:
        raise MissingTokenError

    try:
        token = token.split(' ')[1]
        data = jwt.decode(token, os.environ['SECRET_KEY'])

    except (DecodeError, KeyError):
        raise InvalidTokenError
    except ExpiredSignatureError:
        raise ExpiredTokenError

    session = get_session()

    try:
        current_user = session.query(User).filter_by(username=data['username']).one()
    except NoResultFound:
        raise InvalidTokenError

    return current_user


def token_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            current_user = extract_user()

        except MissingTokenError:
            return jsonify({'message': 'token is missing'}), 401
        except InvalidTokenError:
            return jsonify({'message': 'token is invalid'}), 401
        except ExpiredTokenError:
            return jsonify({'message': 'token has expired'}), 401

        return func(current_user, *args, **kwargs)
    return inner
