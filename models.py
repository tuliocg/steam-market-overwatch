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
        return '<Weapon : {weapon_name} type {type_id} state {state_id}'.format(self.weapon_name, self.type_id, self.state_id)

class Type(Base):
    __tablename__ = 'type'
    id_ = Column(Integer, primary_key=True)
    type_name = Column(String) 
    
    def __repr__(self):
        return '<Type : {type_name}, id : {id_}'.format(self.type_name, self.id_)

class State(Base):
    __tablename__ = 'state'
    id_ = Column(Integer, primary_key=True)
    state_desc = Column(String)

    def __repr__(self):
        return '<State : {state_name}}, id : {id_}'.format(self.state_name, self.id_)
