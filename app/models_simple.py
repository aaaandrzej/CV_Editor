from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    firstname = Column(String(), nullable=False)
    lastname = Column(String(), nullable=False)

    skills = relationship("Skill", back_populates="user")  # docelowo zrobic backref=
    experience = relationship("Experience", back_populates="user")  # docelowo zrobic backref=

    def __repr__(self):
        return f"{self.username} - {self.firstname} {self.lastname}"


class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    skill_name = Column(String(), nullable=False)
    skill_level = Column(Integer, nullable=False)

    user = relationship("User", back_populates="skills")  # docelowo wywalic jak bedzie backref w User

    def __repr__(self):
        return f"{self.skill_name} {self.skill_level}"


class Experience(Base):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    company = Column(String(), nullable=False)
    project = Column(String(), nullable=False)
    duration = Column(Integer, nullable=False)

    user = relationship("User", back_populates="experience")  # docelowo wywalic jak bedzie backref w User

    def __repr__(self):
        return f"{self.company} {self.project} {self.duration}"
