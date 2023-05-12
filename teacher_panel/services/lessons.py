import requests
from datetime import date
from teacher_panel.services import API_URL
import json


def get_lessons(subgroup_id: int):
    lessons = requests.get(API_URL + 'lessons/nearest_day',
                           params={
                            'subgroup_id': subgroup_id
                           })
    lessons.raise_for_status()
    lessons = lessons.json()['lessons']
    return lessons


def cancel_lesson(lesson_id: int, auth_token: str):
    for_day = date.today()
    for_day = {'day': for_day.day, 'month': for_day.month, 'year': for_day.year}
    res = requests.patch(API_URL + 'lessons/', json={'lesson_id': int(lesson_id), 'for_date': for_day, 'is_existing': False}, headers={'auth-token': auth_token})



def send_timetable(timetable, school_id, auth_token: str):
    res = requests.post(API_URL + 'timetable/', files={'lessons_file': timetable}, 
            params={"school_id": school_id}, headers={'auth-token': auth_token})
    if res.status_code == 200:
        return True
    return False
