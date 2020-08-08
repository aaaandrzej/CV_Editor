from flask import Flask, request, render_template, redirect
from auth import auth_bp, login_required

import json

from models import Cv
from session import get_session

session = get_session(echo=False)

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'
app.register_blueprint(auth_bp)



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
