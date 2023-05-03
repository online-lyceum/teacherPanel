import requests
import json
from os import environ

API_URL = environ.get('API_URL')


def create_user(login: str, password: str) -> 'Token':
    return
    token = requests.post(API_URL + 'auth/register', json={"name": login, "password": password})


def login_user(login: str, password: str) -> 'Token':
    token = requests.post(API_URL + 'auth/login', json={"name": login, "password": password})
    print(token, token.json(), login, password)
    return token.json()['key']
