from flask import Blueprint, render_template, session, request
from flask import redirect, url_for
from teacher_panel.services.auth import login_user, login_check
from teacher_panel.services.lessons import send_timetable 

lessons = Blueprint('lessons', __name__)


@lessons.route('/lessons', methods=["GET"])
def lessons_panel():
    if login_check(session):
        return render_template(
            'lessons.html'
        )
    return '<h1>Authorize first</h1>'


@lessons.route('/lessons', methods=["POST"])
def cancel():
    if login_check(session):
        if 'file' in request.files:
            school_id = request.form.get('school_id')
            file = request.files['file']
            if file.filename != '' and file:
                send_timetable(file.read(), int(school_id), session.get('auth_token')) 
                return redirect(url_for('auth.profile'))
        return redirect(request.url)
    return '<h1>Authorize first</h1>'

