from models import User, SkillName, SkillUser, Experience
from session import get_session
import json

session = get_session(echo=False)

users = session.query(User).all()

andrzej = session.query(User).filter_by(username='andrzej').first()
piotr = session.query(User).get(2)


print(andrzej)
print(piotr)
# print(json.dumps(andrzej))
# print(json.dumps(dict(piotr.user_dict())))
# print(andrzej.object_as_dict())
#
# print(users.user_dict())

# def get_users_skills(user):
#     return json.dumps({skill for skill in user.skills})
    # output = []
    # for skill in user.skills:
    #     output.append(skill.object_as_dict())
    # return output

    # return {
    #     user.skills: self.id,
    #     "order_lines": [line.json() for line in self.order_lines]
    # }

# print(get_users_skills(piotr))

# all_db_users = session.query(User).all()

# for user in all_db_users:
#     print(user.object_as_dict())
#     for skill in user.skills:
#         print(skill.object_as_dict())  #, end=", ")
#     for experience in user.experience:
#         print(experience)  #.company, end=" ")
#         print(experience.object_as_dict())
#     print()



# all_db_records = [cv_instance.object_as_dict() for cv_instance in session.query(User)]
#
# print(all_db_records)