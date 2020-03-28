from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Base

engine = create_engine('sqlite:///db/data_source.db', echo=True)

Session = sessionmaker(bind=engine)

def init_db():
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    init_db()
