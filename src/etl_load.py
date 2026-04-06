from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from connection import set_up_connection 
import psycopg2

Base = declarative_base()

class stock(Base): 
    __tablenamne__ = 'stocks'
    date = Column(TIMESTAMP)
    open = Column(Integer) 
    high = Column(Integer) 
    low = Column(Integer) 
    close = Column(Integer) 
    volume = Column(Integer)
    
#Setting up the connection 
engine = create_engine('postgresql://postgres:admin@localhost:5432/stocks', echo=True)
with engine.connect() as conn:
    # session instance is used to communicate with the database
    Session = sessionmaker(bind=engine)
    session = Session()

            




    
    