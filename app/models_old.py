from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# skills_to_users = Table(  # zamiast tego zrbimy klasę SkillsToUsers
#     'skills_to_users',
#     Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('skill_id', Integer, ForeignKey('skills.id')),
#     Column('skill_level', Integer, nullable=False)
# )


class SkillsToUsers(Base):
    __tablename__ = 'skills_to_users'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skills.id'), primary_key=True)
    skill_level = Column(Integer, nullable=False)

    skills = relationship('Skill', back_populates='user')
    user = relationship('User', back_populates='skills')

    def __repr__(self):
        return f"{self.skill_id} {self.skill_level}"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    firstname = Column(String(), nullable=False)
    lastname = Column(String(), nullable=False)

    skills = relationship('SkillsToUsers', back_populates='user')

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    skill_name = Column(String(), nullable=False)

    user = relationship('SkillsToUsers', back_populates='skills')

    def __repr__(self):
        return f"{self.skill_name}"


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

