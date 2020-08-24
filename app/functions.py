from models import User, SkillUser, SkillName, Experience
from session import get_session
from sqlalchemy.orm import Session


def replace_skills_with_json(session: Session, cv: object, json_data: dict) -> None:

    cv.skills = []

    json_db_skill_name_list = session.query(SkillName).filter(SkillName.skill_name.in_(skill['skill_name'] for skill in json_data["skills"])).all()

    json_db_skill_name_dict = {skill_object.skill_name: skill_object for skill_object in json_db_skill_name_list}

    json_skills = json_data['skills']

    for skill in json_skills:
        skill_name = skill['skill_name']
        skill_level = skill['skill_level']

        skill_name_obj = json_db_skill_name_dict.get(skill_name, 0)

        if skill_name_obj == 0:
            skill_name_obj = SkillName(skill_name=skill_name)
            session.add(skill_name_obj)

        skill_obj = SkillUser()
        skill_obj.skill = skill_name_obj
        skill_obj.skill_level = skill_level

        cv.skills.append(skill_obj)

    return


def replace_experience_with_json(cv: object, json_data: dict) -> None:

    cv.experience = []

    for json_exp in json_data.get('experience', []):
        exp_object = Experience()
        exp_object.company = json_exp["company"]
        exp_object.project = json_exp["project"]
        exp_object.duration = json_exp["duration"]

        cv.experience.append(exp_object)

    return
