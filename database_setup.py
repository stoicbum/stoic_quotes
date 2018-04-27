import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable= False)
    email = Column(String(250), nullable = False)
    picture = column(String(250), nullable = False)

class Stoics(Base):
    __tablename__ = 'stoics'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Quote(Base):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nulalble = False)
    quote = Column(String(1000), nullable = False)
    stoic_id = Column(Integer, ForeignKey('Stoics.id'))
    stoic = relationship(Stoics)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
        return{
        'name': self.name,
        'id': self.id,
        'quote': self.id,

        }

engine = create_engine(
    'sqlite:///stoicquotes.db')

Base.metadata.creat_all(engine)





