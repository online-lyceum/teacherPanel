import requests
import json
from os import environ
from flask import abort
from teacher_panel.services import API_URL

tokens = []  # TODO Replace to check token in api


def create_user(login: str, password: str) -> 'Token':
    pass


def login_user(login: str, password: str) -> 'Token':
    user_info = requests.post(API_URL + 'auth/login', json={"name": login, "password": password})
    user_info = user_info.json()
    if user_info and user_info.get('detail') is None:
        tokens.append(user_info['token']['key'])
        return user_info
    abort(401, 'Invalid authorize')


def login_check(session, raise_unauth=True):
    if session.get('auth_token') in tokens:
        return True
    if raise_unauth:
        abort(401, 'Invalid authorize')
    return False
