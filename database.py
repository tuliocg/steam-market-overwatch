from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db/data_source.db', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    '''
    import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db()
    '''
    from models import Weapon
    Base.metadata.create_all(bind=engine)
