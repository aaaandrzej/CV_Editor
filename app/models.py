from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, inspect

Base = declarative_base()


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


class User(Base):
    __tablename__ = 'login_table'

    id = Column(Integer, primary_key=True)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)

    def __repr__(self):
        return f"{self.username} {self.password}"

