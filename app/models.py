from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class SkillUser(Base):
    __tablename__ = 'skill_user'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)
    skill_level = Column(Integer())

    skill = relationship("SkillName", back_populates="users")  # czy skills? czy user?
    user = relationship("User", back_populates="skills")

    # skill_name = relationship("SkillName", back_populates="skill_name")

    def __repr__(self):
        return f"{self.skill.skill_name} {self.skill_level}"


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)  # nullable=False)
    password = Column(String)  # nullable=False)
    firstname = Column(String)  # nullable=False)
    lastname = Column(String)  # nullable=False)

    skills = relationship("SkillUser", back_populates="user")

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class SkillName(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    skill_name = Column(String(), nullable=False)  # , unique=True)

    users = relationship("SkillUser", back_populates="skill")  # czy skills? czy user?

    def __repr__(self):
        return f"{self.skill_name}"
