from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class SkillUser(Base):
    __tablename__ = 'skill_user'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    skill_id = Column(Integer, ForeignKey('skill.id'))
    skill_level = Column(Integer)  #, nullable=False)

    skills = relationship('Skill', back_populates='user')
    user = relationship('User', back_populates='skills')

    def __repr__(self):
        return f"{self.skill_id} {self.skill_level}"


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)  # nullable=False)
    password = Column(String)  # nullable=False)
    firstname = Column(String)  # nullable=False)
    lastname = Column(String)  # nullable=False)

    skills = relationship('SkillUser', back_populates='user')

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    skill_name = Column(String)  # , nullable=False)  # , unique=True)

    user = relationship('SkillUser', back_populates='skills')
    # skill_level = relationship('SkillUser', back_populates='skills')

    def __repr__(self):
        return f"{self.skill_name}"

"""
obecnie proba dodania usera do bazy konczy sie:

AssertionError: Attribute 'skills' on class '<class 'models.User'>' doesn't handle objects of type '<class 'models.Skill'>'

kod:
from session import get_session
session = get_session(echo=True)
 
# user1 = User()
user2 = User()

user2.username = "andrzej"

sql = Skill()
sql.skill_name = "sql"
# sql.skill_level = 0

# python = Skill()
# python.skill_name = "python"
# python.skill_level = 2

user2.skills.append(sql)
# user2.skills.append(python)

print(user2.username, user2.skills)  # to dziala

# for skl in user2.skills:
#     print(skl.skill_name, skl.skill_level)


# print(user1.name, user1.skills)
# print(user2.name, user2.skills)
#
# session.add(user1)
session.add(user2)  # tu jest blad AssertionError: Attribute 'skills' on class '<class 'models.User'>' doesn't handle objects of type '<class 'models.Skill'>'
# session.commit()
"""


"""
class Cv(Base):
    __tablename__ = 'basic_table'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(), nullable=False)
    lastname = Column(String(), nullable=False)
    python = Column(Integer())
    javascript = Column(Integer())
    sql = Column(Integer())
    english = Column(Integer())

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

    def object_as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
"""

