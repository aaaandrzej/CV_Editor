from functools import wraps
import os

import jwt
from jwt.exceptions import DecodeError
from flask import request, jsonify


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        if 'x-api-key' in request.headers:
            token = request.headers['x-api-key']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, f"{os.environ['SECRET_KEY']}")
            # current_user = User.query.filter_by(public_id=data['public_id']).first()
            current_user = data['username']
            # current_user = 'dddd'
            # print(current_user)
        except (DecodeError, KeyError):
            return jsonify({'message': 'Token is invalid!'}), 401

        # return func(*args, **kwargs)
        return func(current_user, *args, **kwargs)

    return decorated
