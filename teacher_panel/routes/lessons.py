from flask import Blueprint, render_template, request
from teacher_panel import db
from teacher_panel.services.auth import login_user

lessons = Blueprint('lessons', __name__)


@lessons.route('/lessons/list', methods=["GET"])
def lessons_list():
    return 'Lessons list' 


@lessons.route('/lessons/lesson', methods=['GET'])
def lesson():
    return 'One lesson from list' 

