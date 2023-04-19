from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Attraction, City, Hotel, Restaurant


if __name__ == '__main__':

    engine = create_engine('sqlite:///test.db')
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(City).delete()
    session.query(Attraction).delete()

    nyc = City(name='New York', state='NY', country='USA')
    la = City(name='Los Angeles', state='CA', country='USA')
    sf= City(name='San Francisco', state='CA', country='USA')
    chs = City(name='Charleston', state = 'SC', country='USA')
    lv = City(name='Las Vegas', state = 'NV', country='USA')
    session.add_all([nyc, la, sf, chs, lv])
    # session.query(City).filter(City.name.in_(['New York', 'Los Angeles', 'San Francisco', 'Charleston', 'Las Vegas'])).distinct().all()
    session.commit()


    es = Attraction(name='Empire State Building', city_id=1)
    sl = Attraction(name='Statue of Liberty', city_id=1)
    cp = Attraction(name='Central Park', city_id=1)
    hs = Attraction(name='Hollywood Sign', city_id=2)
    hwf = Attraction(name='Hollywood Walk of Fame', city_id=2)
    vb = Attraction(name='Venice Beach', city_id=2)
    ggb = Attraction(name='Golden Gate Bridge', city_id=3)
    ai = Attraction(name='Alcatraz Island', city_id=3)
    op = Attraction(name='Oracle Park', city_id=3)
    ao = Attraction(name='Angel Oak Tree', city_id=4)
    fb = Attraction(name='Folly Beach', city_id=4)
    mp = Attraction(name='Magnolia Plantation', city_id=4)
    fs = Attraction(name='Fremont Street', city_id=5)
    bf = Attraction(name='Bellagio Fountain', city_id=5)
    lvs = Attraction(name='Las Vegas Strip', city_id=5)

    session.add_all([es, sl, cp, hs, hwf, vb, ggb, ai, op, ao, fb, mp, fs, bf, lvs])
    # session.query(Attraction).filter(Attraction.name.in_(['Empire State building', 'Statue of Liberty', 'Central Park', 'Hollywood Sign', 'Hollywood Walk of Fame', 'Venice Beach', 'Golden Gate Bridge', 'Alcatraz Island', 'Oracle Park', 'Angel Oak', 'Folly Beach', 'Magnolia Plantation', 'Fremont Street', 'Bellagio Fountain', 'Las Vegas Strip'])).all()
    session.commit()