from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, class_mapper, attributes
import json

Base = declarative_base()


class SkillUser(Base):
    __tablename__ = 'skill_user'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)
    skill_level = Column(Integer())

    skill = relationship("SkillName", back_populates="users")
    user = relationship("User", back_populates="skills")

    def object_as_dict(self):
        # return {self.skill.skill_name : self.skill_level}
        return {
                    "skill_name": self.skill.skill_name,
                    "skill_level": self.skill_level
                }

    def __repr__(self):
        return f"{self.object_as_dict()}"


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
        return f"{self.object_as_dict()}"

    # def object_as_dict(self):
    #     return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def object_as_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            # "skills":
            # "skills": {
            #     "xxx"
            #
            #
            # },
            "skills": {skill for skill in self.skills},
            # "skills": type({skill for skill in self.skills}),
            # "skills": {"skill:":skill for skill in self.skills},
            "exprience": {exp for exp in self.experience}
            # "exprience": type({exp for exp in self.experience})
            # "experience": {"experience":exp for exp in self.experience}

        }


class SkillName(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    skill_name = Column(String(), nullable=False, unique=True)

    users = relationship("SkillUser", back_populates="skill")

    def __repr__(self):
        return f"'{self.skill_name}'"


class Experience(Base):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    company = Column(String)  # nullable=False)
    project = Column(String)  # nullable=False)
    duration = Column(Integer)  # nullable=False)

    user = relationship("User", back_populates="experience")

    def __repr__(self):
        return f"{self.object_as_dict()}"

    def object_as_dict(self):
        # return {
        #     self.company:
        #     {self.project : self.duration}
        # }

        return {
            "project_details":
                {
                    "company": self.company,
                    "project": self.project,
                    "duration": self.duration
                }
            }


