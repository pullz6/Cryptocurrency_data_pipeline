from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
import psycopg2
import logging

logging.info("Connection Started")
# Define the database engine
def set_up_connection(): 
        engine = create_engine('postgresql://postgres:admin@localhost:5432/stocks', echo=True)
        with engine.connect() as conn:
            result = conn.execute(text("select 'hello world'"))
            print(result.all())
