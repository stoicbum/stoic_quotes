import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Stoics(Base):
    __tablename__ = 'stoics'
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String(80), nullable = False)


class Quote(Base):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key = True, autoincrement=True)
    quote = Column(String(1000), nullable = False)
    stoic_id = Column(Integer, ForeignKey('stoics.id'))
    stoic = relationship(Stoics)



    @property
    def serialize(self):
        return{
        'name': self.name,
        'id': self.id,
        'quote': self.id,

        }

engine = create_engine(
    'sqlite:///stoic.db')

Base.metadata.create_all(engine)





