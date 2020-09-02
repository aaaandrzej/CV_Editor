from flask import Flask, request, jsonify, Response, make_response
from sqlalchemy.exc import OperationalError
from typing import Tuple
from app.models import User
from app.session import get_session
from app.functions import replace_skills_with_json, replace_experience_with_json, parse_params, create_param_subs
from app.sql_queries import SQL_COUNT, SQL_STATS


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index() -> Response:
    msg = 'For API please use /api/cv or /api/cv/<id>'
    return Response(msg, mimetype='text/plain')


@app.route('/api/cv', methods=['GET'])
@app.route('/api/cv/', methods=['GET'])
def api_cv_get() -> Response:

    # GET ALL CVs

    session = get_session()

    all_db_records = [user.object_as_dict() for user in session.query(User)]

    return jsonify(all_db_records)


@app.route('/api/cv', methods=['POST'])
@app.route('/api/cv/', methods=['POST'])
def api_cv_post() -> Tuple[dict, int]:

    # ADD NEW CV BASED ON JSON DATA

    error_response = {'error': 'bad input data'}, 400
    db_error_response = {'error': 'database error'}, 503
    success_response = {'success': 'item added'}, 201

    json_data = request.get_json()

    if type(json_data) is not dict:
        return error_response

    for key in json_data.keys():  # sprawdzanie zbędnych kluczy, wydaje mi się nadmiarowe, ale daj znać co ty myślisz
        if key not in ['firstname', 'lastname', 'username', 'password', 'skills', 'experience']:
            return error_response

    session = get_session()

    # create new_cv object and map basic user data from json:
    new_cv = User()

    new_cv.username = json_data.get('username', '')
    new_cv.password = json_data.get('password', '')

    try:
        new_cv.firstname = json_data['firstname']
        new_cv.lastname = json_data['lastname']
        replace_skills_with_json(session, new_cv, json_data)
        replace_experience_with_json(new_cv, json_data)

    except KeyError:
        return error_response

    except OperationalError:
        return db_error_response

    session.add(new_cv)
    session.commit()

    return success_response


@app.route('/api/cv/<id>', methods=['GET'])
def api_cv_id_get(id: int) -> Response:

    # GET ONE CV OF ID [id]

    session = get_session()

    one_db_record = session.query(User).get(id)

    try:
        response = jsonify(one_db_record.object_as_dict())
        return response

    except AttributeError:
        return make_response('', 404)


@app.route('/api/cv/<id>', methods=['PUT'])
def api_cv_id_put(id: int) -> Tuple[str, int]:

    # UPDATE CV OF ID [id] WITH JSON DATA

    json_data = request.get_json()

    session = get_session()

    cv_being_updated = session.query(User).get(id)

    if cv_being_updated is None:
        return '', 404

    cv_being_updated.username = json_data.get('username', '')
    cv_being_updated.password = json_data.get('password', '')

    cv_being_updated.firstname = json_data['firstname']
    cv_being_updated.lastname = json_data['lastname']

    replace_skills_with_json(session, cv_being_updated, json_data)

    replace_experience_with_json(cv_being_updated, json_data)

    session.commit()

    return '', 200


@app.route('/api/cv/<id>', methods=['DELETE'])
def api_cv_id_delete(id: int) -> Tuple[str, int]:

    # DELETE CV OF ID [id]

    session = get_session()

    cv_to_be_deleted = session.query(User).get(id)

    if cv_to_be_deleted is not None:
        session.delete(cv_to_be_deleted)
        session.commit()

        return '', 204

    else:
        return '', 404


@app.route('/api/cv/stats', methods=['POST'])
def api_cv_stats() -> Response:

    # GET CVs OF USERS WITH PROVIDED SKILL SET

    json_data = request.get_json()

    session = get_session()

    sql = SQL_STATS.format(subs=create_param_subs(json_data))

    params = parse_params(json_data)

    result = session.execute(sql, params).fetchall()

    users_with_skill_set = [{'firstname': user.firstname, 'lastname': user.lastname} for user in result]

    return jsonify(users_with_skill_set)


@app.route('/api/cv/stats/count', methods=['POST'])
def api_cv_stats_count() -> Response:

    # GET COUNT OF USERS WITH PROVIDED SKILL SET

    json_data = request.get_json()

    session = get_session()

    sql = SQL_COUNT.format(subs=create_param_subs(json_data))

    params = parse_params(json_data)

    result = session.execute(sql, params).scalar()

    return make_response({'number_of_users_with_skill_set': result})


if __name__ == '__main__':
    app.run(debug=True)
