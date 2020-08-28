from flask import Flask, request, jsonify, Response
from sqlalchemy.sql import text

from models import User, SkillUser, SkillName, Experience
from session import get_session, engine

session = get_session()


json_skills = [{
               "skill_name": "sql",
               "skill_level": 20
            },
            {
                "skill_name": "zapasy",
                "skill_level": 100
                }]


# json_db_skills_dict = {json_skill['skill_name']: json_skill['skill_level'] for json_skill in json_skills}

# print(json_db_skills_dict)

# users_with_skill_set = session.query(User).join(SkillUser).join(SkillName).filter(
#     User.skills == json_skills
# ).all()
#
#
# print(users_with_skill_set)
#
# user1 = session.query(User).get(2)
# print(user1)
# print()
# print(user1.skills_dict)
# print(json_db_skills_dict)
# print(user1.skills_dict == json_db_skills_dict)
# print()
#
# print(type(user1.skills_dict))

# u1 = session.query(User).filter(
#     User.skills_dict == json_db_skills_dict
# )
#
# u1 = session.query(User).filter(
#     User.skills.in_(json_skills)
#
# ).all()
#
# #
# print(u1)
#
#
# user = session.query(User).from_statement(text(
#         "SELECT * FROM user where skills_dict=:skills"
#     )).params(skills=json_db_skills_dict).all()
#
# print(user)
