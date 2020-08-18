from flask import Flask, request, jsonify, render_template, redirect
from auth import auth_bp, login_required

from models import User, SkillUser, SkillName, Experience
from session import get_session

import json

session = get_session(echo=False)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# app.secret_key = 'tajny-klucz-9523'  # do odkomentowania jak będę robić auth
# app.register_blueprint(auth_bp)  # j/w


@app.route('/')
def index():
    return "For API please use /api/cv or /api/cv/<id>"  # TODO jak to zmusić do wyświetlania <id> w safari? po uruchomieniu tego w przeglądarce mam: "For API please use /api/cv or /api/cv/"


@app.route('/api/cv', methods=['GET'])
@app.route('/api/cv/', methods=['GET'])
def api_cv_get():
    all_db_records = [user.object_as_dict() for user in session.query(User)]

    return jsonify(all_db_records)


@app.route('/api/cv', methods=['POST'])  # TODO to nie dziala z /cv (/cv/ jest OK)
@app.route('/api/cv/', methods=['POST'])
def api_cv_post():

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

    # add skills from json to new_cv object, if skills were provided:
    for skill in json_data.get('skills', []):

        # check if skill_name already exists
        skill_name_obj = session.query(SkillName).filter_by(skill_name=skill["skill_name"]).first()

        if not skill_name_obj:  # TODO to byla wczesniej osobna funkcja ale sqlite nie obsluguje kilku watkow bazy, i musi byc if tutaj
            skill_name_obj = SkillName(skill_name=skill["skill_name"])
            session.add(skill_name_obj)

        skill_object = SkillUser()
        skill_object.skill = skill_name_obj
        skill_object.skill_level = skill["skill_level"]

        new_cv.skills.append(skill_object)  # TODO dlaczego pycharm podswietla append na zolto..?

    # add experience from json to new_cv object, if experience was provided:
    for exp in json_data.get('experience', []):

        exp_object = Experience()
        exp_object.company = exp["company"]
        exp_object.project = exp["project"]
        exp_object.duration = exp["duration"]

        new_cv.experience.append(exp_object)  # TODO dlaczego pycharm podswietla append na zolto..?

    session.add(new_cv)
    session.commit()

    return "", 201


@app.route('/api/cv/<id>', methods=['GET'])
def api_cv_id_get(id=None):
    one_db_record = session.query(User).get(id)

    try:
        response = json.dumps(one_db_record.object_as_dict())
        return response

    except AttributeError:
        return "", 404


@app.route('/api/cv/<id>', methods=['PUT'])
def api_cv_id_put(id=None):

    # UPDATE CV OF ID [id] WITH JSON DATA

    json_data = request.get_json()

    cv_being_updated = session.query(User).get(id)

    if cv_being_updated is None:
        return "", 404

    print(cv_being_updated)

    # update basic user's attributes:
    for key, value in json_data.items():
        if key not in ["skills", "experience"]:
            setattr(cv_being_updated, key, value)

    # overwrite user's skills:  # TODO zakładam, że nadpisuję istniejące skille tymi przekazanymi w json'ie. jeśli nie, to mam prawie gotowy, chociaz pokręcony kod w poprzednim commicie
    if "skills" in json_data.keys():  # TODO kod jest zduplikowany z funkcją POST, czy powinienem to przerobić na funkcje add_skills() i add_experience() i wynieść poza endpointy?

        cv_being_updated.skills = []

        for json_skill in json_data.get('skills', []):

            skill_name_obj = session.query(SkillName).filter_by(skill_name=json_skill["skill_name"]).first()

            if not skill_name_obj:
                skill_name_obj = SkillName(skill_name=json_skill["skill_name"])
                session.add(skill_name_obj)

            skill_object = SkillUser()
            skill_object.skill = skill_name_obj
            skill_object.skill_level = json_skill["skill_level"]

            cv_being_updated.skills.append(skill_object)

    # overwrite user's experience:  # TODO zakładam, że nadpisuję istniejące experience tym przekazanymi w json'ie, tak jak w skills powyżej
    if "experience" in json_data.keys():

        cv_being_updated.experience = []

        for json_exp in json_data.get('experience', []):
            exp_object = Experience()
            exp_object.company = json_exp["company"]
            exp_object.project = json_exp["project"]
            exp_object.duration = json_exp["duration"]

            cv_being_updated.experience.append(exp_object)

    session.commit()

    return "", 202


@app.route('/api/cv/<id>', methods=['DELETE'])
def api_cv_id_delete(id=None):

    cv_to_be_deleted = session.query(User).get(id)

    if cv_to_be_deleted is not None:
        session.delete(cv_to_be_deleted)
        session.commit()

        return "", 202

    else:
        return "", 404


if __name__ == '__main__':
    app.run(debug=True)
