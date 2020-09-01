from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class SkillUser(Base):
    __tablename__ = 'skill_user'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)
    skill_level = Column(Integer)

    skill = relationship('SkillName', back_populates='users', lazy='joined')
    user = relationship('User', back_populates='skills', lazy='joined')

    def object_as_dict(self) -> dict:
        return {
            'skill_name': self.skill.skill_name,
            'skill_level': self.skill_level
        }

    def __repr__(self) -> str:
        return f'{self.object_as_dict()}'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    password = Column(String(64))
    firstname = Column(String(64))
    lastname = Column(String(64))

    skills = relationship('SkillUser', back_populates='user', cascade='all, delete-orphan', lazy='selectin')
    experience = relationship('Experience', back_populates='user', cascade='all, delete-orphan', lazy='joined')

    def __repr__(self) -> str:
        return f'{self.object_as_dict()}'

    def object_as_dict(self) -> dict:
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'skills': [skill.object_as_dict() for skill in self.skills],
            'experience': [exp.object_as_dict() for exp in self.experience]
        }


class SkillName(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    skill_name = Column(String(64), nullable=False, unique=True)

    users = relationship('SkillUser', back_populates='skill')

    def __repr__(self) -> str:
        return f'{self.skill_name}'


class Experience(Base):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    company = Column(String(64))
    project = Column(String(64))
    duration = Column(Integer)

    user = relationship('User', back_populates='experience')

    def __repr__(self) -> str:
        return f'{self.object_as_dict()}'

    def object_as_dict(self) -> dict:
        return {
            'company': self.company,
            'project': self.project,
            'duration': self.duration
        }
