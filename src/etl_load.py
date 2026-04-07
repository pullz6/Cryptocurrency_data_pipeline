from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, REAL, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from connection import set_up_connection 
import psycopg2
from data_import import importing_to_df

df = importing_to_df()

Base = declarative_base()

class stock(Base): 
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(TIMESTAMP)
    open = Column(REAL) 
    high = Column(REAL) 
    low = Column(REAL) 
    close = Column(REAL) 
    volume = Column(Integer)
    company = Column(CHAR)
    
#Setting up the connection 
engine = create_engine('postgresql://postgres:admin@localhost:5432/stocks', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
            

for _, row in df.iterrows():
    stock_record = stock(
         date=row['date'],
         open=row['open'],
         high=row['high'],
         low=row['low'],
         close=row['close'],
         volume=row['volume'],
         company=row['company']
     )
    session.add(stock_record)
session.commit()

    
    