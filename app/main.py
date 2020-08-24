from flask import Flask, request, jsonify, Response

from models import User, SkillUser, SkillName, Experience
from session import get_session
from functions import replace_skills_with_json, replace_experience_with_json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index() -> Response:
    msg = "For API please use /api/cv or /api/cv/<id>"
    return Response(msg, mimetype='text/plain')


@app.route('/api/cv', methods=['GET'])
@app.route('/api/cv/', methods=['GET'])
def api_cv_get() -> jsonify:

    session = get_session()

    all_db_records = [user.object_as_dict() for user in session.query(User)]  # TODO spr czy nie wystepuje n+1

    return jsonify(all_db_records)


@app.route('/api/cv', methods=['POST'])
@app.route('/api/cv/', methods=['POST'])
def api_cv_post() -> 201:

    # ADD NEW CV BASED ON JSON DATA

    json_data = request.get_json()

    # create new_cv object and map basic user data from json:
    new_cv = User()

    if "username" in json_data:
        new_cv.username = json_data["username"]
    if "password" in json_data:
        new_cv.password = json_data["password"]

    new_cv.firstname = json_data["firstname"]
    new_cv.lastname = json_data["lastname"]

    session = get_session()

    replace_skills_with_json(session, new_cv, json_data)

    replace_experience_with_json(new_cv, json_data)

    session.add(new_cv)
    session.commit()

    return "", 201


@app.route('/api/cv/<id>', methods=['GET'])
def api_cv_id_get(id: int = None) -> jsonify:

    session = get_session()

    one_db_record = session.query(User).get(id)

    try:
        response = jsonify(one_db_record.object_as_dict())
        return response

    except AttributeError:
        return "", 404


@app.route('/api/cv/<id>', methods=['PUT'])
def api_cv_id_put(id: int = None) -> 200:

    # UPDATE CV OF ID [id] WITH JSON DATA

    json_data = request.get_json()

    session = get_session()

    cv_being_updated = session.query(User).get(id)

    if cv_being_updated is None:
        return "", 404

    # update basic user's attributes:
    for key, value in json_data.items():  # TODO jeśli nie przekażę np firstname to nie zostanie wyczyszczone - to błąd?
        if key not in ["skills", "experience"]:
            setattr(cv_being_updated, key, value)

    replace_skills_with_json(session, cv_being_updated, json_data)

    replace_experience_with_json(cv_being_updated, json_data)

    session.commit()

    return "", 200


@app.route('/api/cv/<id>', methods=['DELETE'])
def api_cv_id_delete(id: int = None) -> 204:

    session = get_session()

    cv_to_be_deleted = session.query(User).get(id)

    if cv_to_be_deleted is not None:
        session.delete(cv_to_be_deleted)
        session.commit()

        return "", 204

    else:
        return "", 404


@app.route('/api/cv/stats/<id>', methods=['GET'])  #  TODO agregacja - zwroc uzytkownikow ktorzy maja okreslona kombinacje skilli z poziomem zaawansowania
def api_cv_stats(id: int = None) -> 200:

    json_data = request.get_json()

    session = get_session()

    return "in progress"


if __name__ == '__main__':
    app.run(debug=True)
