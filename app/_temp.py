from models import User, SkillName, SkillUser
# from models import Child, Parent, Association
from session import get_session

session = get_session(echo=False)

"""
andrzej = User()
sql = SkillUser(skill_level=1)
sql.skill = SkillName()
andrzej.skills.append(sql)


for sku in andrzej.skills:
    print(sku.skill_level)
    print(sku.skill_id)

session.add(andrzej)
# session.commit()

print(andrzej.skills)
"""

# user = session.query(User).get(1)
#
andrzej = User()
piotr = User()

andrzej.username = "andrzej"
piotr.username = "piotr"


python_name = SkillName()
python_name.skill_name = "python"

python_piotra = SkillUser()
python_piotra.skill = python_name
python_piotra.skill_level = 5


python2_name = SkillName()
python2_name.skill_name = "python"


sql_name = SkillName()
sql_name.skill_name = "sql"

sql_piotra = SkillUser()
sql_piotra.skill = sql_name
sql_piotra.skill_level = 4


# user2.skills.append(sql)
piotr.skills.append(python_piotra)
piotr.skills.append(sql_piotra)
#
# print(user.username, user.skills)
#
for skl in piotr.skills:
    print(skl.user.username, end=": ")
    print(skl.skill.skill_name, skl.skill_level)
    # print(type(skl))
    # print()

print()
print(andrzej.username, andrzej.skills)
print(piotr.username, piotr.skills)
#
# session.add(user1)
# session.add(user)
# session.commit()


#

# print(user.name, user.skills)
#
# session.add(user1)
# session.add(user2)
# session.commit()
# """



