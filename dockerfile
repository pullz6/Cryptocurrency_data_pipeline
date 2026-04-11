FROM python:3.12.11 

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt 

COPY ./src/. /app/


