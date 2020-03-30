__author__ = 'https://github.com/tuliocg'

from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeaponHistorical(Base):
    __tablename__ = 'weapon_historical'
    weapon_name = Column(String, primary_key=True)
    type_id = Column(Integer)
    state_id = Column(Integer)
    date = Column(Date)
    price_value = Column(Float)

    def __repr__(self):
        return '<Weapon: {weapon_name}, type: {type_id}, state: {state_id}, price: {price_value}, date: {date}'.format(self.weapon_name 
                , self.type_id, self.state_id, self.price_value, self.date)

class WeaponCurrentBid(Base):
    __tablename__ = 'weapon_current_bid'
    weapon_name = Column(String, primary_key=True)
    type_id = Column(Integer)
    state_id = Column(Integer)
    date = Column(Date)
    bid_value = Column(Float)

    def __repr__(self):
        return '<Weapon: {weapon_name}, type: {type_id}, state: {state_id}, price: {price_value}, date: {date}'.format(self.weapon_name 
                , self.type_id, self.state_id, self.price_value, self.date)

class Type(Base):
    __tablename__ = 'type'
    id_ = Column(Integer, primary_key=True)
    type_desc = Column(String) 
    
    def __repr__(self):
            return '<Type : {type_desc}, id : {id_}'.format(self.type_desc, self.id_)

class Quality(Base):
    __tablename__ = 'quality'
    id_ = Column(Integer, primary_key=True)
    quality_desc = Column(String)

    def __repr__(self):
        return '<State : {quality_desc}, id : {id_}'.format(self.quality_desc, self.id_)

class FXRate(Base):
    __tablename__ = 'fx_rate'
    id_ = Column(Integer, primary_key=True)
    from_cur = Column(String)
    to_cur = Column(String)
    date = Column(Date)
    fx_value = Column(Float)
    source_type = Column(String)

    def __repr__(self):
        return '<FX_Rate : id : {id_}, from_cur: {from_cur}, to_cur: {to_cur}, date: {date}, fx_value: {fx_value}, source: {source_type}'.format(
                self.id_, self.from_cur,self.to_cur, self.date, self.fx_value)
                

