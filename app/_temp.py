# from models import User, Skill, SkillUser
from models import Child, Parent, Association
from session import get_session

session = get_session(echo=False)


# create parent, append a child via association
p = Parent()
a = Association(extra_data="some data")
a.child = Child()
p.children.append(a)

# iterate through child objects via association, including association
# attributes
for assoc in p.children:
    print(assoc.extra_data)
    print(assoc.child)








"""
# user1 = User()
user2 = User()

user2.username = "andrzej"

sql = Skill()
sql.skill_name = "sql"
sql.skill_level = 0

python = Skill()
python.skill_name = "python"
# python.skill_level = 2

user2.skills.append(sql)
user2.skills.append(python)
#
print(user2.username, user2.skills)
#
# for skl in user2.skills:
#     print(skl.skill_name, skl.skill_level)


# print(user1.name, user1.skills)
# print(user2.name, user2.skills)
#
# session.add(user1)
session.add(user2)
# session.commit()


#

# user = session.query(User).get(1)
# print(user.name, user.skills)
#
# session.add(user1)
# session.add(user2)
# session.commit()
"""



