from flask import Flask, request, jsonify, Response

from models import User, SkillUser, SkillName, Experience
from session import get_session

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index() -> Response:
    msg = "For API please use /api/cv or /api/cv/<id>"
    return Response(msg, mimetype='text/plain')


@app.route('/api/cv', methods=['GET'])
@app.route('/api/cv/', methods=['GET'])
def api_cv_get() -> jsonify:

    session = get_session(echo=False)
    """przenoszę session do endpointów bo kiedy było zdefiniowane globalnie 
    to ubijanie i podnoszenie bazy podczas działania aplikacji wywalało błędy"""

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

    session = get_session(echo=False)

    # add skills from json to new_cv object, if skills were provided:
    for skill in json_data.get('skills', []):

        # check if skill_name already exists
        skill_name_obj = session.query(SkillName).filter_by(skill_name=skill["skill_name"]).first()

        if not skill_name_obj:
            skill_name_obj = SkillName(skill_name=skill["skill_name"])
            session.add(skill_name_obj)

        skill_object = SkillUser()
        skill_object.skill = skill_name_obj
        skill_object.skill_level = skill["skill_level"]

        new_cv.skills.append(skill_object)

    # add experience from json to new_cv object, if experience was provided:
    for exp in json_data.get('experience', []):

        exp_object = Experience()
        exp_object.company = exp["company"]
        exp_object.project = exp["project"]
        exp_object.duration = exp["duration"]

        new_cv.experience.append(exp_object)

    session.add(new_cv)
    session.commit()

    return "", 201


@app.route('/api/cv/<id>', methods=['GET'])
def api_cv_id_get(id: int = None) -> jsonify:

    session = get_session(echo=False)

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

    session = get_session(echo=False)

    cv_being_updated = session.query(User).get(id)

    if cv_being_updated is None:
        return "", 404

    print(cv_being_updated)

    # update basic user's attributes:
    for key, value in json_data.items():
        if key not in ["skills", "experience"]:
            setattr(cv_being_updated, key, value)

    # overwrite user's skills (will be redesigned in future):
    if "skills" in json_data.keys():  # TODO ten if usunac, "skills" jest wymagane

        cv_being_updated.skills = []

        for json_skill in json_data.get('skills', []):  # TODO spr czy kasowanie skill user odbywa sie automatycznie

            skill_name_obj = session.query(SkillName).filter_by(skill_name=json_skill["skill_name"]).first()  # TODO zamienic to na liste skillnames
            # skill_name_obj = session.query(SkillName.skill_name.label('skill_name')).filter(SkillName.skill_name.in_([list comprehension])).first()  # TODO zamienic to na liste skillnames

            if not skill_name_obj:
                skill_name_obj = SkillName(skill_name=json_skill["skill_name"])
                session.add(skill_name_obj)

            skill_object = SkillUser()
            skill_object.skill = skill_name_obj
            skill_object.skill_level = json_skill["skill_level"]

            cv_being_updated.skills.append(skill_object)

    # overwrite user's experience (will be redesigned in future):
    if "experience" in json_data.keys():  # TODO spr czy bez .keys() zadziala

        cv_being_updated.experience = []

        for json_exp in json_data.get('experience', []):
            exp_object = Experience()
            exp_object.company = json_exp["company"]
            exp_object.project = json_exp["project"]
            exp_object.duration = json_exp["duration"]

            cv_being_updated.experience.append(exp_object)

    session.commit()

    return "", 200


@app.route('/api/cv/<id>', methods=['DELETE'])
def api_cv_id_delete(id: int = None) -> 204:

    session = get_session(echo=False)

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

    session = get_session(echo=False)

    return "in progress"


if __name__ == '__main__':
    app.run(debug=True)
