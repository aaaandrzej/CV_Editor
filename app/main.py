from flask import Flask, request, render_template, redirect
from auth import auth_bp, login_required

from sqlalchemy.orm.exc import UnmappedInstanceError

from models import User, SkillUser, SkillName, Experience
from session import get_session

import json

session = get_session(echo=False)

app = Flask(__name__)
# app.secret_key = 'tajny-klucz-9523'
# app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return "For API please use /api/cv or /api/cv/<id>"  # TODO jak to zmusić do wyświetlania <id> w safari?


@app.route('/api/cv', methods=['GET'])
@app.route('/api/cv/', methods=['GET'])
def api_cv_get():

    all_db_records = [user.object_as_dict() for user in session.query(User)]

    return json.dumps(all_db_records)  # TODO halo Piotr, czy da się bez json.dumps - zgodnie z uwaga z PR?


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
    if "skills" in json_data and len(json_data["skills"]) > 0:  # if skills:
        for skill in json_data["skills"]:
            # TODO to wyzej zamienic na:
            # for skill in json_data.get('skills', []):

            # check if skill_name already exists
            skill_name_obj = session.query(SkillName).filter_by(skill_name=skill["skill_name"]).first()

            if not skill_name_obj:  # TODO to byla wczesniej osobna funkcja ale sqlite nie obsluguje kilku watkow bazy, i musi byc if tutaj
                skill_name_obj = SkillName(skill_name=skill["skill_name"])
                session.add(skill_name_obj)

            skill_object = SkillUser()
            skill_object.skill = skill_name_obj
            skill_object.skill_level = skill["skill_level"]

            new_cv.skills.append(skill_object)

    # add experience from json to new_cv object, if experience was provided:
    if "experience" in json_data and len(json_data["experience"]) > 0:  # if experience:
        for exp in json_data["experience"]:
            exp_object = Experience()
            exp_object.company = exp["company"]
            exp_object.project = exp["project"]
            exp_object.duration = exp["duration"]

            new_cv.experience.append(exp_object)

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

    # ADD NEW CV BASED ON JSON DATA

    json_data = request.get_json()

    cv_being_updated = session.query(User).get(id)

    if cv_being_updated is None:
        return "", 404

    print(cv_being_updated)

    # update basic user's attributes:
    for key, value in json_data.items():
        if key not in ["skills", "experience"]:
            setattr(cv_being_updated, key, value)

    print("update to:")
    print(cv_being_updated)
    # print(cv_being_updated.skills)
    print()

    # add skills from json to new_cv object, if skills were provided:
    for skill in json_data.get('skills', []):
        # skill_name_obj = SkillName(skill_name=skill["skill_name"])
        # skill_obj = SkillUser()
        # skill_obj.skill = skill_name_obj
        # skill_obj.skill_level = skill["skill_level"]

        skills_list_from_db = [skill.object_as_dict() for skill in cv_being_updated.skills]
        # print(skills_list_from_db)
        # print(type(skills_list_from_db))
        # print()

        if skill not in skills_list_from_db:   # TODO WHYYYY!!!????
        # if skill_obj not in cv_being_updated.skills:   # TODO WHYYYY!!!????
        #     print(skill_obj)
            print(type(skill))
            print(skill)
            print("not in")
            print(type(skills_list_from_db))
            print(skills_list_from_db)
            print()






            # check if skill_name already exists
            # skill_name_obj = session.query(SkillName).filter_by(skill_name=skill["skill_name"]).first()
            #
            # if not skill_name_obj:  # TODO to byla wczesniej osobna funkcja ale sqlite nie obsluguje kilku watkow bazy, i musi byc if tutaj
            #     skill_name_obj = SkillName(skill_name=skill["skill_name"])
            #     session.add(skill_name_obj)
            #
            # skill_object = SkillUser()
            # skill_object.skill = skill_name_obj
            # skill_object.skill_level = skill["skill_level"]
            #
            # cv_being_updated.skills.append(skill_object)

        else:
            print("old skill, no update needed")



    # session.commit()

    # return "", 202
    return "feature in progress", 222


@app.route('/api/cv/<id>', methods=['DELETE'])
def api_cv_id_delete(id=None):

    cv_to_be_deleted = session.query(User).get(id)

    try:
        session.delete(cv_to_be_deleted)
        session.commit()

        return "", 202

    except UnmappedInstanceError:
        return "", 404


if __name__ == '__main__':
    app.run(debug=True)
