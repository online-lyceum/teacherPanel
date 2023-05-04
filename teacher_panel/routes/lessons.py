from flask import Blueprint, render_template, session
from teacher_panel.services.auth import login_user, login_check
from teacher_panel.services.lessons import get_lessons

lessons = Blueprint('lessons', __name__)


@lessons.route('/lessons/list', methods=["GET"])
def lessons_list():
    if login_check(session):
        return render_template(
            'lessons.html',
            lessons=get_lessons(session['user_data'].get('subgroup_id'))
        )
    return '<h1>Authorize first</h1>'


@lessons.route('/lessons/lesson', methods=['GET'])
def lesson():
    return 'One lesson from list'
