import datetime
import os
from typing import Tuple

import json
import jwt
from flask import Flask, request, jsonify, Response, make_response
from sqlalchemy.exc import OperationalError, DataError
from werkzeug.exceptions import BadRequest, HTTPException
from werkzeug.security import check_password_hash, generate_password_hash

from app.auth import token_required
from app.functions import replace_skills_with_json, replace_experience_with_json, parse_params, create_param_subs, \
    error_response
from app.models import User
from app.session import get_session
from app.sql_queries import SQL_COUNT, SQL_STATS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.route('/')
def index() -> Response:
    msg = 'For API please use /api/cv or /api/cv/<id>'
    return Response(msg, mimetype='text/plain')


@app.route('/login')
def login() -> Tuple[dict, int]:
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return error_response('not authorized', 401, None)

    session = get_session()

    user = session.query(User).filter_by(username=auth.username).first()

    if not user:
        return error_response('not authorized', 401, None)

    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            os.environ['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return error_response('not authorized', 401, None)


@app.route('/identify')
@token_required
def identify(current_user: User) -> Tuple[dict, int]:
    return jsonify(current_user.object_as_dict()), 200


@app.route('/api/cv', methods=['GET'])
@app.route('/api/cv/', methods=['GET'])
def api_cv_get() -> Tuple[dict, int]:
    # GET ALL CVs

    session = get_session()

    all_db_records = [user.object_as_dict() for user in session.query(User)]

    return jsonify(all_db_records), 200


@app.route('/api/cv', methods=['POST'])
@app.route('/api/cv/', methods=['POST'])
@token_required
def api_cv_post(current_user: User) -> Tuple[dict, int]:
    # ADD NEW CV BASED ON JSON DATA

    if not current_user.admin:
        return error_response('not authorized', 401, None)

    session = get_session()

    try:
        json_data = request.get_json()

    except BadRequest as ex:
        return error_response('bad input data', 400, ex)

    new_cv = User()

    try:
        new_cv.username = json_data['username']
        new_cv.password = json_data.get('password', '')
        if new_cv.password != '':
            new_cv.password = generate_password_hash(new_cv.password, method='sha256', salt_length=8)
        new_cv.admin = False
        new_cv.firstname = json_data['firstname']
        new_cv.lastname = json_data['lastname']
        replace_skills_with_json(session, new_cv, json_data)
        replace_experience_with_json(new_cv, json_data)
    except (KeyError, TypeError, AttributeError) as ex:
        return error_response('bad input data', 400, ex)
    except OperationalError as ex:
        return error_response('db error', 500, ex)

    session.add(new_cv)

    try:
        session.commit()
    except DataError as ex:
        return error_response('bad input data', 400, ex)

    return jsonify(new_cv.object_as_dict()), 201


@app.route('/api/cv/<id>', methods=['GET'])
def api_cv_id_get(id: int) -> Tuple[dict, int]:
    # GET ONE CV OF ID [id]

    session = get_session()

    one_db_record = session.query(User).get(id)

    try:
        response = jsonify(one_db_record.object_as_dict()), 200
        return response

    except AttributeError:
        return make_response('', 404)


@app.route('/api/cv/<user_id>', methods=['PUT'])
@token_required
def api_cv_id_put(current_user: User, user_id: int) -> Tuple[dict, int]:
    # UPDATE CV OF ID [id] WITH JSON DATA

    if not current_user.admin:
        if current_user.id != int(user_id):
            return error_response('not authorized', 401, None)

    json_data = request.get_json()

    session = get_session()

    cv_being_updated = session.query(User).get(user_id)

    if cv_being_updated is None:
        return error_response('bad input data', 400, None)

    cv_being_updated.username = json_data['username']
    cv_being_updated.password = json_data.get('password', '')
    if cv_being_updated.password != '':
        cv_being_updated.password = generate_password_hash(cv_being_updated.password, method='sha256', salt_length=8)

    cv_being_updated.firstname = json_data['firstname']
    cv_being_updated.lastname = json_data['lastname']

    replace_skills_with_json(session, cv_being_updated, json_data)

    replace_experience_with_json(cv_being_updated, json_data)

    session.commit()

    return jsonify(cv_being_updated.object_as_dict()), 200


@app.route('/api/cv/<user_id>', methods=['DELETE'])
@token_required
def api_cv_id_delete(current_user: User, user_id: int) -> Tuple[dict, int]:
    # DELETE CV OF ID [id]

    if not current_user.admin:
        return error_response('not authorized', 401, None)

    session = get_session()

    cv_to_be_deleted = session.query(User).get(user_id)

    if cv_to_be_deleted is not None:
        session.delete(cv_to_be_deleted)
        session.commit()

        return jsonify({}), 204

    else:
        return error_response('bad input data', 404, None)


@app.route('/api/cv/<id>/password', methods=['POST'])
def api_cv_id_password(id: int) -> Tuple[dict, int]:
    # CHANGE YOUR PASSWORD

    json_data = request.get_json()

    try:
        old_password_from_json = json_data['old_password']
        new_password_from_json = json_data['new_password']
    except KeyError as ex:
        return error_response('bad input data', 400, ex)

    session = get_session()

    cv_being_updated = session.query(User).get(id)

    if cv_being_updated is None:
        return error_response('bad input data', 404, None)

    if check_password_hash(cv_being_updated.password, old_password_from_json):
        cv_being_updated.password = generate_password_hash(new_password_from_json, method='sha256', salt_length=8)
        session.commit()

        return jsonify(cv_being_updated.object_as_dict()), 200

    return error_response('bad input data', 400, None)


@app.route('/api/cv/stats', methods=['POST'])
def api_cv_stats() -> Tuple[dict, int]:
    # GET CVs OF USERS WITH PROVIDED SKILL SET

    json_data = request.get_json()

    session = get_session()

    sql = SQL_STATS.format(subs=create_param_subs(json_data))

    params = parse_params(json_data)

    result = session.execute(sql, params).fetchall()

    users_with_skill_set = [{'firstname': user.firstname, 'lastname': user.lastname} for user in result]

    return jsonify(users_with_skill_set), 200


@app.route('/api/cv/stats/count', methods=['POST'])
def api_cv_stats_count() -> Tuple[dict, int]:
    # GET COUNT OF USERS WITH PROVIDED SKILL SET

    json_data = request.get_json()

    session = get_session()

    sql = SQL_COUNT.format(subs=create_param_subs(json_data))

    params = parse_params(json_data)

    result = session.execute(sql, params).scalar()

    return jsonify({'number_of_users_with_skill_set': result}), 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=False)
