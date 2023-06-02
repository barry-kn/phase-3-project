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

def connect():
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def add_bean(session, name, method, rating):
    bean = Bean(name=name, method=method, rating=rating)
    session.add(bean)
    session.commit()

def get_all_beans(session):
    return session.query(Bean).all()

def get_beans_by_name(session, name):
    return session.query(Bean).filter(Bean.name == name).all()

def get_best_preparation_for_bean(session, name):
    return session.query(Bean).filter(Bean.name == name).order_by(Bean.rating.desc()).first()

def delete_bean(session, bean_id):
    session.query(Bean).filter(Bean.id == bean_id).delete()
    session.commit()
