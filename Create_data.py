from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

####### Creating the base class for the declarative models:####
Base = declarative_base()

#####  AIM  ############
### 1) one-to-many relationship >>>>>>> between the Farmer and Bean
### 2) farmer can have multiple beans associated with them, 
###    but each bean is associated with only one farmer.


#####   kuDefining  the Farmer class which represents the farmers table:
class Farmer(Base):
    __tablename__ = 'farmers'
    id = Column(Integer, primary_key=True)
    area = Column(String)
    phone_number = Column(String)
    beans = relationship('Bean', back_populates='farmer')
 ### one to many  rela,  
 ### Bean is the taget class of the rela
## 





### kuDefining the Bean class, which represents the beans table:

class Bean(Base):
    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    method = Column(String)
    rating = Column(Integer)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    farmer = relationship('Farmer', back_populates='beans')
####  rela >>>> many to one 
### farmer is the taget class 



#### gover table  

class Government(Base):
    __tablename__ = 'government'
    id = Column(Integer, primary_key=True)
    bean_name = Column(String)
    rating = Column(Integer)
    farmer_area = Column(String)

#### function ya connecting to database (data.db)
def connect():
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


#### seeding to see the structure of the tables 


def create_data():
    session = connect()

    # Example data for the farmers table
    farmer1 = Farmer(area='kimbu', phone_number='0746272382')
    farmer2 = Farmer(area='kitale', phone_number='0743536282')
    session.add_all([farmer1, farmer2])
    session.commit()
    print("Farmers added successfully!")

    # Example data for the beans table
    bean1 = Bean(name='Red Kidney Beans', method='Bean Stew', rating=75, farmer=farmer1)
    bean2 = Bean(name='Pigeon Peas', method='Pigeon Pea Curry', rating=84, farmer=farmer2)
    
    session.add_all([bean1, bean2])
    session.commit()
    print("Beans added successfully!")

    session.close()

# Call the create_data() function
create_data()





####### kuita the file when the script run directly 
if __name__ == '__main__':
    create_data()
