__author__ = 'https://github.com/tuliocg'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Weapon(Base):
    __tablename__ = 'weapon'
    weapon_name = Column(String, primary_key=True)
    type_id = Column(Integer)
    state_id = Column(Integer)

    def __repr__(self):
        return 'Showing: {name} type {type_id} state {state_id}'.format(name=self.name, type_id=self.type_id, state_id=self.state_id)

class Type(Base):
    __tablename__ = 'type'
    id_ = Column(Integer, primary_key=True)
    type_name = Column(String) 

class State(Base):
    __tablename__ = 'state'
    id_ = Column(Integer, primary_key=True)
    state_desc = Column(String)

