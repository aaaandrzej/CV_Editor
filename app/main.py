from flask import Flask, request, render_template, redirect
from auth import auth_bp, login_required
# from db import get_connection

import json
from db_queries import query_read_db
from db_queries import query_read_one_from_db
from db_queries import query_insert_db
from db_queries import query_remove_from_db
from db_queries import query_update_db
from config import api_on

from models import Cv
from session import get_session

session = get_session(echo=False)

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'
app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return "For API please use /api/cv or /api/cv/<id>, for HTML please use /cv or /cv<id>"  # TODO jak to zmusić do wyświetlania <id> w safari?


# API

if api_on:

    @app.route('/api/cv', methods=['GET', 'POST'])
    @app.route('/api/cv/', methods=['GET', 'POST'])
    def api_cv():
        if request.method == "GET":

            all_db_records = [cv_instance.object_as_dict() for cv_instance in session.query(Cv)]

            return json.dumps(all_db_records)

        elif request.method == "POST":

            query_data = request.get_json()

            session.add(Cv(**query_data))
            session.commit()

            return "", 201


    @app.route('/api/cv/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def api_cv_id(id=None):
        if request.method == "GET":

            one_db_record = session.query(Cv).get(id).object_as_dict()

            return json.dumps(one_db_record)

        elif request.method == "PUT":
            json_data = request.get_json()

            cv_being_updated = session.query(Cv).get(id)

            cv_being_updated.firstname = json_data["firstname"]  # TODO uprościć... jakoś z **json_data ?
            cv_being_updated.lastname = json_data["lastname"]
            cv_being_updated.python = json_data["python"]
            cv_being_updated.javascript = json_data["javascript"]
            cv_being_updated.sql = json_data["sql"]
            cv_being_updated.english = json_data["english"]

            session.commit()

            return "", 202

        elif request.method == "DELETE":

            cv_to_be_deleted = session.query(Cv).get(id)
            session.delete(cv_to_be_deleted)
            session.commit()

            return "", 202

        elif request.method == "POST":
            return f"POST cv {id} not supported, use POST /api/cv to add or PUT /cv/<id> to update"

        else:
            return f'{request.method} cv {id} not yet supported'


# HTML

@app.route('/cv', methods=['GET', 'POST'])
@app.route('/cv/', methods=['GET', 'POST'])
@login_required
def cv():
    single_result = False

    all_db_records = [cv_instance for cv_instance in session.query(Cv)]

    if request.method == "GET":
        pass

    if request.method == "POST":
        query_data = {
                  'firstname': request.form.get('firstname_from_form'),
                  'lastname': request.form.get('lastname_from_form'),
                  'python': request.form.get('python_from_form'),
                  'javascript': request.form.get('javascript_from_form'),
                  'sql': request.form.get('sql_from_form'),
                  'english': request.form.get('english_from_form')
                  }

        session.add(Cv(**query_data))
        session.commit()

        return redirect(request.url)

    return render_template("index.html", all_db_records=all_db_records, single_result=single_result)


@app.route('/cv/<id>', methods=['GET', 'POST'])
@login_required
def cv_id(id=None):

    single_result = True

    one_db_record = session.query(Cv).get(id)

    if request.method == "GET":
        pass

    if request.method == "POST":

        cv_being_updated = session.query(Cv).get(id)

        cv_being_updated.firstname = request.form.get('firstname_from_form')
        cv_being_updated.lastname = request.form.get('lastname_from_form')
        cv_being_updated.python = request.form.get('python_from_form')
        cv_being_updated.javascript = request.form.get('javascript_from_form')
        cv_being_updated.sql = request.form.get('sql_from_form')
        cv_being_updated.english = request.form.get('english_from_form')

        session.commit()

        return redirect(request.url)

    return render_template("index.html", all_db_records=[one_db_record], single_result=single_result)


if __name__ == '__main__':
    app.run(debug=True)
