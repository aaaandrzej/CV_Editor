from models import User, Skill, UserSkill
# from models import Skill, User, SkillsToUsers
from session import get_session

if __name__ == '__main__':

    session = get_session(echo=False)

user1 = User('andrzej')
user1.skills = {
    'python':1,
    'sql':0
    }

user2 = User('ania')
user2.skills = {
    'english':5,
    }

print(user1.name, user1.skills)
print(user2.name, user2.skills)
#
# user = session.query(User).get(10)
# print(user.skills)  # TODO DLACZEGO???

# session.add(user1)
# session.add(user2)
# session.commit()


# w konsoli:
# alembic downgrade base
# alembic revision --autogenerate -m "start"
# alembic upgrade head
