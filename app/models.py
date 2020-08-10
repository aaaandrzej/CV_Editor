from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class SkillUser(Base):
    __tablename__ = 'skill_user'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)
    skill_level = Column(Integer())

    skill = relationship("SkillName", back_populates="users")
    user = relationship("User", back_populates="skills")

    # skill_name = relationship("SkillName", back_populates="skill_name")  # TODO nie umiem tego zmusic do dzialania

    def __repr__(self):
        return f"{self.skill.skill_name} {self.skill_level}"  # TODO mogę tak??


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)  # nullable=False)
    password = Column(String)  # nullable=False)
    firstname = Column(String)  # nullable=False)
    lastname = Column(String)  # nullable=False)

    skills = relationship("SkillUser", back_populates="user")
    experience = relationship("Experience", back_populates="user")

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class SkillName(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    skill_name = Column(String(), nullable=False, unique=True)

    users = relationship("SkillUser", back_populates="skill")

    def __repr__(self):
        return f"{self.skill_name}"


class Experience(Base):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    company = Column(String)  # nullable=False)
    project = Column(String)  # nullable=False)
    duration = Column(Integer)   # nullable=False)

    user = relationship("User", back_populates="experience")

    def __repr__(self):
        return f"{self.company} {self.project} {self.duration}"
