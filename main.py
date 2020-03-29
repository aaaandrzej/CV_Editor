from flask import Flask, request
from db_queries import query_read_db, select_all
from db_queries import query_read_one_from_db, select_one
from db_queries import query_insert_db, insert_dummy_cv, insert_dummy_cv_params
from db_queries import query_remove_from_db, remove_one


app = Flask(__name__)


@app.route('/')
def index():
    return "Please use /cv or /cv/<id> to use this API"


@app.route('/cv', methods=['GET', 'POST'])  # czemu /cv działa a /cv/ daje błąd?
def cv():
    if request.method == "GET":
        return query_read_db(select_all)  # DONE

    elif request.method == "POST":  # w jaki sposób powinny być przekazywane dane? json? czytać je request.form.get..?
        query_insert_db(insert_dummy_cv, insert_dummy_cv_params)
        return f"{insert_dummy_cv_params} cv added to db"


@app.route('/cv/<id>', methods=['get', 'post', 'put', 'delete'])
def cv_id(id=None):
    if request.method == "GET":  # DONE
        return query_read_one_from_db(select_one, id)

    elif request.method == "POST":  # to samo co 21
        return f"post cv {id} not yet supported"

    elif request.method == "DELETE":  # DONE
        query_remove_from_db(remove_one, id)
        return f"cv {id} successfully removed"

    elif request.method == "PUT":  # to samo co 21
        return f"put cv {id} not yet supported"

    else:
        return f'{request.method} cv {id} not yet supported'


if __name__ == '__main__':
    # cvs = query_read_db(select_all)
    # print(str(cvs))
    app.run(debug=True)
