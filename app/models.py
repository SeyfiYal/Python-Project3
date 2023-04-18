from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.db')

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(String)
    country = Column(String)


class Hotel(Base):
    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer)


class Restaurant(Base):
    __tablename__ ='restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer)


class Attraction(Base):
    __tablename__ = 'attraction'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

nyc = City(name='New York', state='NY', country='USA')
la = City(name='Los Angeles', state='CA', country='USA')
sf= City(name='San Francisco', state='CA', country='USA')
chs = City(name='Charleston', state = 'SC', country='USA')
lv = City(name='Las Vegas', state = 'NV', country='USA')
session.add_all([nyc, la, sf, chs, lv])
# session.query(City).filter(City.name.in_(['New York', 'Los Angeles', 'San Francisco', 'Charleston', 'Las Vegas'])).delete(synchronize_session=False)
session.commit()