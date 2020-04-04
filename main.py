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


@app.route('/api/cv', methods=['GET', 'POST']) # API
def api_cv():
    if request.method == "GET":
        return query_read_db("select_all.sql")

    elif request.method == "POST":
        query_data = request.get_json()
        query_insert_db("insert_cv.sql", query_data)
        return f"{query_data} cv added to db"


@app.route('/cv', methods=['GET', 'POST']) # WWW
def cv():
    if request.method == "GET":
        all_db_records = query_read_db("select_all.sql")
        all_db_records_json = json.loads(all_db_records)
        return render_template("index.html", all_db_records=all_db_records_json)


'''
# przerobić, dodać formularz - póki co post to kopia z api
    elif request.method == "POST":  # przerobić to wszystko na request.form.get..
        query_data = request.get_json()

        query_insert_db("insert_cv.sql", query_data)
        return f"{query_data} cv added to db"
'''


@app.route('/api/cv/<id>', methods=['get', 'post', 'put', 'delete']) # API
def api_cv_id(id=None):
    if request.method == "GET":  # DONE
        return query_read_one_from_db("select_one.sql", id)

    elif request.method == "POST":
        return f"post cv {id} not yet supported"

    elif request.method == "DELETE":  # DONE
        query_remove_from_db("delete_one.sql", id)
        return f"cv {id} successfully removed"

    elif request.method == "PUT":
        return f"put cv {id} not yet supported"

    else:
        return f'{request.method} cv {id} not yet supported'

'''
#przerobić analogicznie jak /cv
@app.route('/cv/<id>', methods=['get', 'post', 'put', 'delete']) # WWW
def api_cv_id(id=None):
    if request.method == "GET":  # DONE
        return query_read_one_from_db("select_one.sql", id)

    elif request.method == "POST":  # to samo co 21 - przekazywać form get czy json?
        return f"post cv {id} not yet supported"

    elif request.method == "DELETE":  # DONE
        query_remove_from_db("delete_one.sql", id)
        return f"cv {id} successfully removed"

    elif request.method == "PUT":  # to samo co 21
        return f"put cv {id} not yet supported"

    else:
        return f'{request.method} cv {id} not yet supported'
'''


if __name__ == '__main__':
    # cvs = query_read_db(select_all)
    # print(str(cvs))
    app.run(debug=True)
