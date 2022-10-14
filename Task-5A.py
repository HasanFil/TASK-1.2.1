from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.types import *
from  sqlalchemy.sql.expression import func
import numpy as np
from faker import Faker
import time


engine = create_engine("postgresql://postgres:hasan0816fil@localhost:5432/postgres")
session =sessionmaker(bind=engine)
Base = declarative_base()
fake = Faker()

start_time=time.time()

class Table_first(Base):
  __tablename__ = "Table_one"
  
  id = Column(Integer, primary_key = True)
  mail = Column(String(50))
  password = Column(String(50))

class Table_second(Base):
    __tablename__ = 'Findings'
    
    id = Column(Integer, primary_key = True)
    mail = Column(String(50))
    password = Column(String(50))
    

def Sahte(i): 
    empty_list = []
    for i in range(i):
        fake = Faker()
        list_1 = []
        list_1.append(fake.email())
        list_1.append(fake.password())
        empty_list.append(list_1)    
    return empty_list  

Base.metadata.create_all(engine)
Sahte(1000)

session.commit()

end_time=time.time()
print(end_time-start_time)


