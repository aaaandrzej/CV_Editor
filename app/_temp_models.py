from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from session import get_session


Base = declarative_base()


class SkillsToUsers(Base):
    __tablename__ = 'skills_to_users'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skills.id'), primary_key=True)
    extra_data = Column(String(50))

    skills = relationship("Skill", back_populates="user")
    user = relationship("User", back_populates="skills")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    skills = relationship("SkillsToUsers", back_populates="user")


class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)

    users = relationship("SkillsToUsers", back_populates="skills")