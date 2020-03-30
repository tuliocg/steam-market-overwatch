from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Base, Quality, Type
import os
import sys

sys.    

def _create_session():

    db_url = os.environ.get('SQLITE_DB_URL_STEAM_MARKET')
    if 'test' in sys.argv[0]:
        db_url += '_test'

    if not db_url:
        raise EnvironmentError('DB URL not setted!')

    engine = create_engine(db_url, echo=True)

    Session = sessionmaker(bind=engine)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    create_session = sessionmaker(bind=engine)
    
    return create_session()

session = _create_session()

def add_weapon_historical():
    pass

def add_weapon_current_bid():
    pass

def init_quality():
    quality_list = ['factory new', 'minimal wear',
                    'field-tested','well-worn',
                    'battle-scarred'] 

    for quality_ in quality_list:
        row = Quality(quality_desc=quality_)
        session.add(row)
        session.commit()

def init_type():
    type_list = ['knife', 'pistol', 'SMG', 'shotgun', 'rifle', 
                  'sniper rifle', 'machinegun', 'sticker', 'pin',
                  'agent','case','capsule', 'cotainer', 'grafitti',
                  'gloves', 'music kit', 'collectible', 'patch',
                  'key', 'pass', 'gift', 'tag','tool']
    
    for type_ in type_list:
        row = Type(type_desc=type_)
        session.add(row)
        session.commit()

if __name__ == '__main__':
    init_type()
    init_quality()
