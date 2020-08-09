from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.collections import attribute_mapped_collection

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    skills = association_proxy(
                'user_skills',
                'skill_level',
                creator=lambda k, v:
                            UserSkill(skill_name=k, skill_level=v)
                )

    def __init__(self, name):
        self.name = name


class UserSkill(Base):
    __tablename__ = 'user_skill'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'),
                                                    primary_key=True)
    skill_level = Column(Integer)
    user = relationship(User, backref=backref(
            "user_skills",
            collection_class=attribute_mapped_collection("skill_name"),
            cascade="all, delete-orphan"
            )
        )

    sk = relationship("Skill")

    skill_name = association_proxy('sk', 'skill_name')


class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    skill_name = Column(String)

    def __init__(self, skill_name):
        self.skill_name = skill_name
