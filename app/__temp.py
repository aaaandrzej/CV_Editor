from flask import Flask, request, jsonify, Response
from sqlalchemy.sql import text

from models import User, SkillUser, SkillName, Experience
from session import get_session, engine, connection

session = get_session()

json_skills = [{
    "skill_name": "sql",
    "skill_level": 20
},
    {
        "skill_name": "zapasy",
        "skill_level": 100
    }]

json_db_skills_dict = {json_skill['skill_name']: json_skill['skill_level'] for json_skill in json_skills}

print(json_db_skills_dict)

json_db_skills_tuple = tuple((json_skill['skill_name'], json_skill['skill_level']) for json_skill in json_skills)

print(json_db_skills_tuple)


with connection.cursor() as cursor:
    sql = (
        "SELECT u.firstname, u.lastname "
        "FROM ( "
            "SELECT q.user_id, COUNT(*) as count "
            "FROM ( "
                "SELECT su.user_id, s.skill_name, su.skill_level "
                "FROM skill_user su "
                "JOIN skill s on su.skill_id = s.id "
                "WHERE (s.skill_name, su.skill_level) IN (%s, %s) "
                ") q "
                "GROUP BY q.user_id "
            ") r "
        "JOIN user u ON r.user_id = u.id "
        "WHERE r.count = 2")

    params = (('python', 2), ('sql', 1))  # TODO za nic nie mogę zmusić sql żeby przyjmował tuplę tupli (ani listę tupli) jako jedną zmienną, i to jedyny wariant gdzie mi cokolwiek działa
    cursor.execute(sql, params)
    result = cursor.fetchall()
    print(result)
