from functools import wraps
import os

import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError
from flask import request, jsonify
from sqlalchemy.orm.exc import NoResultFound

from app.models import User
from app.session import get_session


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            token = token.split(' ')[1]
            data = jwt.decode(token, os.environ['SECRET_KEY'])

        except (DecodeError, KeyError):
            return jsonify({'message': 'Token is invalid!'}), 401
        except ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401

        session = get_session()

        try:
            current_user = session.query(User).filter_by(username=data['username']).one()
        except NoResultFound:
            return jsonify({'message': 'Token is invalid!'}), 401

        return func(current_user, *args, **kwargs)

    return decorated
