from flask import Blueprint, render_template, request, session
from flask import redirect, url_for
from teacher_panel.services.auth import login_user, login_check

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET"])
def login():
    return render_template('login.html')


@auth.route('/login', methods=["POST"])
def do_login():
    session['auth_token'] = login_user(
        request.form.get('name'), request.form.get('password')
    )
    session['user_data'] = {'subgroup_id': 63}
    return redirect(url_for('auth.profile'))


@auth.route('/profile')
def profile():
    if login_check(session):
        return render_template('profile.html', user=session['user_data'])
    return 'Authorize'