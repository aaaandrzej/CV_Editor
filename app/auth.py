from functools import wraps

from werkzeug.security import check_password_hash
from flask import Blueprint, request, get_flashed_messages, render_template, \
    session, redirect, flash, url_for

from config import admin_username, admin_password_hashed
# from db import get_connection

auth_bp = Blueprint('auth_endpoints', __name__)


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session:
            return view(*args, **kwargs)
        else:
            return redirect(url_for('auth_endpoints.login'))

    return wrapped_view


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('login.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # conn = get_connection()
        # c = conn.cursor()
        #
        # result = c.execute('SELECT * FROM users WHERE username = ?', (username,))
        # user_data = result.fetchone()

        user_data = {"id": 1, "username": admin_username, "password": admin_password_hashed}  # TODO przerobić to później na usera z DB

        if username == admin_username:
            hashed_password = user_data['password']

            if check_password_hash(hashed_password, password):
                session['user_id'] = user_data['id']
                session['username'] = user_data['username']
                return redirect(url_for('cv'))

        flash('błędna nazwa użytkownika lub hasło')
        return redirect(url_for('auth_endpoints.login'))


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_endpoints.login'))
