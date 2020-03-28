from flask import Flask, render_template, request
from db_queries import query_read_db, query_read_one_from_db, select_all, select_one

app = Flask(__name__)


@app.route('/')
def index():
        return "Please use /cv or /cv/<id> to use this API"


@app.route('/cv', methods=['GET', 'POST'])
def cv():
    if request.method == "GET":
        return query_read_db(select_all)

    elif request.method == "POST":
        return "post cv"


@app.route('/cv/<id>', methods=['get', 'post', 'put', 'delete'])
def cv_id(id=None):
    if request.method == "GET":

        return query_read_one_from_db(select_one, id)

    elif request.method == "post":
        return f"post cv {id} not yet supported"
    else:
        return f'{request.method} cv {id} not yet supported'


if __name__ == '__main__':
    # cvs = query_read_db(select_all)
    # print(str(cvs))
    app.run(debug=True)
