from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, REAL, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy import func
from connection import set_up_connection 
import psycopg2
from data_import import importing_to_df
import logging

logger = logging.getLogger(__name__)

logger.info("Getting today's data")
df = importing_to_df()

logger.info("Creating base model")
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
    company = Column(String)
    
#Setting up the connection 
logger.info("Setting up the connection")
engine = create_engine('postgresql://postgres:admin@localhost:5432/stocks', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

logger.info("Getting the last date on the server")
max_date = session.query(func.max(stock.date)).scalar()
#print(f"Most recent date: {max_date}")

logger.info("Filtering data for only new records")
df = df[df['date'] > str(max_date)]

logger.info("Pushing new data")
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

logger.info("New data pushed")