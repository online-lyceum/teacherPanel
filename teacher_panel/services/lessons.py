import requests
from teacher_panel.services import API_URL


def get_lessons(subgroup_id: int):
    lessons = requests.get(API_URL + 'lessons/nearest_day',
                           params={
                            'subgroup_id': subgroup_id
                           })
    lessons.raise_for_status()
    lessons = lessons.json()['lessons']
    return lessons