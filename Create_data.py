from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Bean(Base):
    __tablename__ = 'beans'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    method = Column(String)
    rating = Column(Integer)

class Farmer(Base):
    __tablename__ = 'farmers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    area = Column(String)
    phone = Column(Integer)

def connect():
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def add_bean(session, name, method, rating):
    bean = Bean(name=name, method=method, rating=rating)
    session.add(bean)
    session.commit()

def add_farmer(session, name, area, phone):
    farmer = Farmer(name=name, area=area, phone=phone)
    session.add(farmer)
    session.commit()

def get_all_beans(session):
    return session.query(Bean).all()

def find_bean_by_name(session, name):
    return session.query(Bean).filter_by(name=name).first()

def find_best_preparation_method(session, name):
    bean = session.query(Bean).filter_by(name=name).first()
    if bean:
        return bean.method
    else:
        return None

def delete_bean(session, bean):
    session.delete(bean)
    session.commit()
