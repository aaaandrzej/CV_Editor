from app.models import SkillUser, SkillName, Experience, User
from sqlalchemy.orm import Session
from typing import List, Tuple
import logging


def replace_skills_with_json(session: Session, cv: User, json_data: dict) -> None:
    cv.skills = []

    json_db_skill_name_list = session.query(SkillName).filter(
        SkillName.skill_name.in_(skill['skill_name'] for skill in json_data['skills'])).all()

    json_db_skill_name_dict = {skill_object.skill_name: skill_object for skill_object in json_db_skill_name_list}

    json_skills = json_data['skills']

    for skill in json_skills:
        skill_name = skill['skill_name']
        skill_level = skill['skill_level']

        try:
            skill_name_obj = json_db_skill_name_dict[skill_name]

        except KeyError:
            skill_name_obj = SkillName(skill_name=skill_name)
            session.add(skill_name_obj)

        cv.skills.append(SkillUser(skill = skill_name_obj, skill_level = skill_level))


def replace_experience_with_json(cv: User, json_data: dict) -> None:
    cv.experience = [
        Experience(
            company=json_exp['company'],
            project=json_exp['project'],
            duration=json_exp['duration']
        ) for json_exp in json_data.get('experience', [])
    ]


def parse_params(json: List[dict]) -> dict:
    params = {f'param{n}': (skill['skill_name'], skill['skill_level']) for n, skill in enumerate(json)}
    params['count'] = len(json)
    return params


def create_param_subs(json: List[dict]) -> str:
    return ', '.join(f':param{n}' for n in range(len(json)))


def error_response(msg: str, status: int, ex: Exception = None) -> Tuple[dict, int]:
    logging.exception(ex)
    return {'error': msg}, status
