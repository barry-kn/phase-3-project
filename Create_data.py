
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Farmer(Base):
    __tablename__ = 'farmers'
    id = Column(Integer, primary_key=True)
    area = Column(String)
    phone_number = Column(String)
    beans = relationship('Bean', back_populates='farmer')


class Bean(Base):
    __tablename__ = 'beans'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    method = Column(String)
    rating = Column(Integer)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    farmer = relationship('Farmer', back_populates='beans')


class Government(Base):
    __tablename__ = 'government'
    id = Column(Integer, primary_key=True)
    bean_name = Column(String)
    rating = Column(Integer)
    farmer_area = Column(String)


def connect():
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
