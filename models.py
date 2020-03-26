__author__ = 'https://github.com/tuliocg'

from sqlalchemy import Column, Integer, String
from database import Base, Session

class Weapon(Base):
    __tablename__ = 'weapon'
    name = Column(String, primary_key=True)
    type_id = Column(Integer)
    state_id = Column(Integer)

    def __repr__(self):
        return 'Showing: {name} type {type_id} state {state_id}'.format(name=self.name, type_id=self.type_id, state_id=self.state_id)

if __name__ =='__main__':
    session = Session()
    gun = Weapon(name='AK', type_id=1, state_id=2)
    session.add(gun)
    session.commit()
   

