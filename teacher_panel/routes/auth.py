from flask import Blueprint, render_template, request, session
from flask import redirect, url_for
from teacher_panel.services.auth import login_user, login_check

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET"])
def login():
    return render_template('login.html')


@auth.route('/login', methods=["POST"])
def do_login():
    data = login_user(
        request.form.get('name'), request.form.get('password')
    )
    if data:
        session['user_data'] = data
        session['auth_token'] = session['user_data'].pop('token')['key']
        return redirect(url_for('auth.profile'))
    abort(401, "Unauthorized")


@auth.route('/profile')
def profile():
    if login_check(session):
        return render_template('profile.html', user=session.get('user_data'))
    return 'Authorize'
