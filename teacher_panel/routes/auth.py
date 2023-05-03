from flask import Blueprint, render_template, request
from teacher_panel import db
from teacher_panel.services.auth import login_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print(request.form)
        return render_template('login.html', token=login_user(
            request.form.get('name'), request.form.get('password')
        ))
    return render_template('login.html') 


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        
    else:
        return render_template('signup.html') 

