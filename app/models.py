from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class SkillUser(Base):
    __tablename__ = 'skill_user'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)
    extra_data = Column(String(50))
    # child = relationship("Child", back_populates="parents")
    skill = relationship("Skill", back_populates="users")
    # parent = relationship("Parent", back_populates="children")
    user = relationship("User", back_populates="skills")


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    skills = relationship("SkillUser", back_populates="user")


class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)

    # parents = relationship("Association", back_populates="child")
    users = relationship("SkillUser", back_populates="skill")