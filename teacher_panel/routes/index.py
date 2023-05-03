from flask import Blueprint, render_template
from teacher_panel import db

index = Blueprint('index', __name__)


@index.route('/')
def main():
    return render_template('index.html')

