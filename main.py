from flask import Flask, request, render_template
import json
from db_queries import query_read_db
from db_queries import query_read_one_from_db
from db_queries import query_insert_db
from db_queries import query_remove_from_db


app = Flask(__name__)


@app.route('/')
def index():
    return "For API please use /api/cv or /api/cv/<id>, for WWW please use /cv or /cv<id>"


# API

@app.route('/api/cv', methods=['GET', 'POST'])
def api_cv():
    if request.method == "GET":
        return query_read_db("select_all.sql")

    elif request.method == "POST":
        query_data = request.get_json()
        query_insert_db("insert_cv.sql", query_data)
        return f"{query_data} cv added to db"


@app.route('/api/cv/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_cv_id(id=None):
    if request.method == "GET":
        return query_read_one_from_db("select_one.sql", id)

    elif request.method == "POST":  # TODO co tu robić? nadpisywać dane cv? to ma sens?
        return f"post cv {id} not yet supported"

    elif request.method == "DELETE":
        query_remove_from_db("delete_one.sql", id)
        return f"cv {id} successfully removed"

    elif request.method == "PUT":  # TODO co tu robić? modyfikacja danego cv?
        return f"put cv {id} not yet supported"

    else:
        return f'{request.method} cv {id} not yet supported'


# HTML

@app.route('/cv', methods=['GET', 'POST'])
def cv():

    all_db_records = query_read_db("select_all.sql")
    all_db_records_json = json.loads(all_db_records)

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

        query_insert_db("insert_cv.sql", query_data)

        # TODO jak wymusić przeładowanie tej strony po dodaniu nowego CV???

    return render_template("index.html", all_db_records=all_db_records_json)


@app.route('/cv/<id>', methods=['GET', 'POST'])
def cv_id(id=None):
    if id is None:
        return "czyżbyś wszedł na /cv/ ?"  # TODO czemu to nie działa...?

    if request.method == "GET":  # TODO todosek w htmlku jak wyłączyć/ zmienić formularz
        one_db_record = query_read_one_from_db("select_one.sql", id)
        one_db_record_json = json.loads(one_db_record)
        return render_template("index.html", all_db_records=one_db_record_json)

    elif request.method == "POST":  # TODO co z tym robimy - tzn co to powinno robić?
        return f"post cv {id} not yet supported"


if __name__ == '__main__':
    app.run(debug=True)
