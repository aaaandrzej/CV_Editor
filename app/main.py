from flask import Flask, request, render_template, redirect
from auth import auth_bp, login_required

from models import User, SkillUser, SkillName, Experience
from session import get_session

import json

session = get_session(echo=False)

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'
app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return "For API please use /api/cv or /api/cv/<id>"  # TODO jak to zmusić do wyświetlania <id> w safari?


@app.route('/api/cv', methods=['GET'])
@app.route('/api/cv/', methods=['GET'])  # TODO czy tak się robi? czy w <id> też dorobić / po adresie?
def api_cv_get():

    all_db_records = [user.object_as_dict_string() for user in session.query(User)]

    return json.dumps(all_db_records)


@app.route('/api/cv', methods=['POST'])
@app.route('/api/cv/', methods=['POST'])
def api_cv_post():

    # query_data = request.get_json()
    #
    # session.add(Cv(**query_data))
    # session.commit()

    return "", 201


@app.route('/api/cv/<id>', methods=['GET'])
def api_cv_id_get(id=None):

    # one_db_record = session.query(Cv).get(id)
    # try:
    #     response = json.dumps(one_db_record.object_as_dict())
    #     return response
    #
    # except AttributeError:
        return "", 404


@app.route('/api/cv/<id>', methods=['PUT'])
def api_cv_id_put(id=None):
    # json_data = request.get_json()
    #
    # cv_being_updated = session.query(Cv).get(id)
    #
    # cv_being_updated.firstname = json_data["firstname"]
    # cv_being_updated.lastname = json_data["lastname"]
    # cv_being_updated.python = json_data["python"]
    # cv_being_updated.javascript = json_data["javascript"]
    # cv_being_updated.sql = json_data["sql"]
    # cv_being_updated.english = json_data["english"]
    #
    # # TODO od PD - uprościć update objektu tak o:
    # # for key, value in json_data.items():
    # #     setattr(cv_being_updated, key, value)
    #
    # session.commit()

    return "", 202


@app.route('/api/cv/<id>', methods=['DELETE'])
def api_cv_id_delete(id=None):

    # cv_to_be_deleted = session.query(Cv).get(id)
    # session.delete(cv_to_be_deleted)
    # session.commit()

    return "", 202


if __name__ == '__main__':
    app.run(debug=True)
