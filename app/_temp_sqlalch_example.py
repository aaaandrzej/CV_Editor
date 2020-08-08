# https://docs.sqlalchemy.org/en/13/orm/extensions/associationproxy.html#composite-association-proxies

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.collections import attribute_mapped_collection

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    # the same 'user_keywords'->'keyword' proxy as in
    # the basic dictionary example
    keywords = association_proxy(
                'user_keywords',
                'keyword',
                creator=lambda k, v:
                            UserKeyword(special_key=k, keyword=v)
                )

    def __init__(self, name):
        self.name = name

class UserKeyword(Base):
    __tablename__ = 'user_keyword'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    keyword_id = Column(Integer, ForeignKey('keyword.id'),
                                                    primary_key=True)
    special_key = Column(String)
    user = relationship(User, backref=backref(
            "user_keywords",
            collection_class=attribute_mapped_collection("special_key"),
            cascade="all, delete-orphan"
            )
        )

    # the relationship to Keyword is now called
    # 'kw'
    kw = relationship("Keyword")

    # 'keyword' is changed to be a proxy to the
    # 'keyword' attribute of 'Keyword'
    keyword = association_proxy('kw', 'keyword')

class Keyword(Base):
    __tablename__ = 'keyword'
    id = Column(Integer, primary_key=True)
    keyword = Column('keyword', String(64))

    def __init__(self, keyword):
        self.keyword = keyword



"""
skill_level <=> skill_name
"""

"""
keywords = skills
keyword = skill_name
keyword_id = skill_id
user_keyword = user_skill
user_keywords = user_skills
special_key = skill_level
kw=sk
"""
