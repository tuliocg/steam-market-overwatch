from sqlalchemy import create_engine

engine = create_engine('sqlite:///db/data_source.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        print('<User {user}, name {name0}, fullname {fullname}, nickname {nickname}'.
                format(user=self.user, name=self.name, fullname=self.fullname,
                    nickname=self.nickname))

if __name__ == '__main__':
    print(engine.table_names())
#    print(Base.metadata.create_all(engine))
