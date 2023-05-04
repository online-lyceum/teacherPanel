import requests
import json
from os import environ
from flask import abort
from teacher_panel.services import API_URL

tokens = []  # TODO Replace to check token in api


def create_user(login: str, password: str) -> 'Token':
    pass


def login_user(login: str, password: str) -> 'Token':
    token = requests.post(API_URL + 'auth/login', json={"name": login, "password": password})
    token = token.json().get('key')
    if token:
        tokens.append(token)
        return token
    abort(401, 'Invalid authorize')


def login_check(session, raise_unauth=True):
    return session.get('auth_token') in tokens