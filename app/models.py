from sqlalchemy import Column, Integer, String, ForeignKey, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table(
    'skills_to_users',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('skill_id', Integer, ForeignKey('skills.id'))
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    firstname = Column(String(), nullable=False)
    lastname = Column(String(), nullable=False)

    skills = relationship(
        'Skill',
        secondary=association_table,
        back_populates='users')

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    skill_name = Column(String(), nullable=False)

    users = relationship(
        'User',
        secondary=association_table,
        back_populates='users'
    )

    def __repr__(self):
        return f"{self.skill_name}"


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


