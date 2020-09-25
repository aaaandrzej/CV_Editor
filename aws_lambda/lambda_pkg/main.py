from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import DataError
import json
from typing import Tuple
from models import User
from session import get_session
from functions import replace_skills_with_json, replace_experience_with_json


def response(status_code, body):
    return {
        'statusCode': status_code,
        'body': body
    }


def index_handler(event, context):
    return response(200, ('httpMethod: ' + json.dumps(event['httpMethod'])))


def db_check_handler(event, context):
    session = get_session()

    query = session.query(User).all()

    return response(200, (f'query: {query}'))


def post_handler(event, context):
    try:
        json_data = event['body']
        # json_data = json.loads(event['body'])

    except (KeyError, TypeError):
        return response(400, 'bad event body')

    new_cv = User()

    try:
        new_cv.username = json_data.get('username', '')
        new_cv.password = json_data.get('password', '')
        new_cv.firstname = json_data['firstname']
        new_cv.lastname = json_data['lastname']
        replace_skills_with_json(None, new_cv, json_data)
        replace_experience_with_json(new_cv, json_data)
    except (KeyError, TypeError, AttributeError) as ex:
        return response(400, f"bad input in event body: {type(json_data)} {json_data}")

    return response(200, f'item {new_cv.object_as_dict()} added')


def handler(event, context):
    session = get_session()

    try:
        json_data = event['body']

    except (KeyError, TypeError):
        return response(400, 'bad event body')

    new_cv = User()

    try:
        new_cv.username = json_data.get('username', '')
        new_cv.password = json_data.get('password', '')
        new_cv.firstname = json_data['firstname']
        new_cv.lastname = json_data['lastname']
        replace_skills_with_json(session, new_cv, json_data)
        replace_experience_with_json(new_cv, json_data)
    except (KeyError, TypeError, AttributeError) as ex:
        return response(400, f"bad input in event body: {event['body']}")
    except OperationalError as ex:
        return response(500, f"db error")

    session.add(new_cv)

    try:
        session.commit()
    except DataError as ex:
        return response(400, f"bad input caused DataError")

    return response(200, f'item {json.dumps(new_cv.object_as_dict())} added')


event = {'body': {"firstname": "Placek",
"lastname": "",
"skills": [],
"experience": []
}}

print(post_handler(event, ''))
# print(type(event))