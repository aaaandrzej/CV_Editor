from models import User, SkillName, SkillUser, Experience
# from models import Child, Parent, Association
from session import get_session

import json

session = get_session(echo=False)

andrzej = session.query(User).filter_by(username='andrzej').first()
piotr = session.query(User).get(2)


# andrzej = User()
# piotr = User()
#
# andrzej.username = "andrzej"
# piotr.username = "piotr"
#
# python_name = SkillName()
# python_name.skill_name = "python"
#
# python_piotra = SkillUser()
# python_piotra.skill = python_name
# python_piotra.skill_level = 5
#
# python_andrzeja = SkillUser()
# python_andrzeja.skill = python_name
# python_andrzeja.skill_level = 1
#
#
# python2_name = SkillName()
# python2_name.skill_name = "python"
#
#
# sql_name = SkillName()
# sql_name.skill_name = "sql"
#
# sql_piotra = SkillUser()
# sql_piotra.skill = sql_name
# sql_piotra.skill_level = 4
#
#
# # user2.skills.append(sql)
# piotr.skills.append(python_piotra)
# andrzej.skills.append(python_andrzeja)
# piotr.skills.append(sql_piotra)


# st_piotra = Experience()
# st_piotra.company = "Secure Trading"

# andrzej.experience.append(st_piotra)

# for exp in piotr.experience:
#     exp.project = "Server"
#     exp.duration = 2
#     print(exp)
#
#
# for skl in piotr.skills:
#     print(skl.user.username, end=": ")
#     print(skl.skill.skill_name, "=", skl.skill_level)
#     print(type(skl))
#     print()
#
# print()
# print(andrzej.username, andrzej.skills, andrzej.experience)
# print(piotr.username, piotr.skills, piotr.experience)
#
# session.add(andrzej)
# session.add(piotr)
# session.commit()

# for exp in piotr.experience:
#     if exp:
#         session.delete(exp)
#         session.commit()
#         break

# session.commit()

#

# print(user.name, user.skills)
#
# session.add(user1)
# session.add(user2)
# session.commit()

data = {
'bill': 'tech',
'federer': 'tennis',
'ronaldo': 'football',
'people' : [ {
'name': 'Scott',
'website': 'stackabuse.com',
'from': 'Nebraska'},
{'name': 'Larry',
'website': 'google.com',
'from': 'Michigan' } ]
}

# data_s = json.dumps(data)
# print(data_s)

users = session.query(User).all()

andrzej = session.query(User).filter_by(username='andrzej').first()
piotr = session.query(User).get(2)
jacek = session.query(User).get(3)


# print(andrzej.skills)

skill = {'skill_name': 'pyt1111hon', 'skill_level': 5}


# from main import api_cv_post

# print(add_skill_name(skill))
#
# try:
#     session.add(skill_obj)
# except Exception as ex:
#     print(ex)
    # print("z bazy: ", end="")
    # print(skill_db_existing)

print()
print()




# print(jacek)
#
# users = session.query(User).all()
#
# print(json.dumps([user.object_as_dict_string() for user in users]))
# print(piotr)
# print(type(andrzej.object_as_dict()))
# andrzej_repr_str = str(andrzej.object_as_dict())
# print(type(andrzej_repr_str))
# andrzej_json = json.dumps(andrzej_repr_str)
# print(andrzej_json)