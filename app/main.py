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

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'
app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return "For API please use /api/cv or /api/cv/<id>, for HTML please use /cv or /cv<id>"


# API

if api_on:

    @app.route('/api/cv', methods=['GET', 'POST'])
    def api_cv():
        if request.method == "GET":
            return json.dumps(query_read_db())

        elif request.method == "POST":
            query_data = request.get_json()
            query_insert_db(query_data)
            return "", 201


    @app.route('/api/cv/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def api_cv_id(id=None):
        if request.method == "GET":
            return query_read_one_from_db(id)

        elif request.method == "PUT":
            json_data = request.get_json()

            # id = json_data["id"]

            query_data = {
                'firstname': json_data["firstname"],
                'lastname': json_data["lastname"],
                'python': json_data["python"],
                'javascript': json_data["javascript"],
                'sql': json_data["sql"],
                'english': json_data["english"],
            }

            query_update_db(id, query_data)

            return "", 202

        elif request.method == "DELETE":
            query_remove_from_db(id)
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

    all_db_records = query_read_db()

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

        query_insert_db(query_data)

        return redirect(request.url)

    return render_template("index.html", all_db_records=all_db_records, single_result=single_result)


@app.route('/cv/<id>', methods=['GET', 'POST'])
@login_required
def cv_id(id=None):

    single_result = True

    one_db_record = query_read_one_from_db(id)

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

        query_update_db(id, query_data)

        return redirect(request.url)

    return render_template("index.html", all_db_records=[one_db_record], single_result=single_result)


if __name__ == '__main__':
    app.run(debug=True)
