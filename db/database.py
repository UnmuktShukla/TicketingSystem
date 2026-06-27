from typing import final
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

load_dotenv()

_db_name = os.getenv('DATABASE')
_db_username = os.getenv('DB_USERNAME')
_db_password = os.getenv('DB_PASSWORD')
_db_host = os.getenv('HOST')
_db_port = os.getenv('PORT')

def get_db_url() -> URL :
    return URL.create(
        drivername="postgresql",
        username=_db_username,
        password=_db_password,
        host=_db_host,
        port=int(_db_port),
        database=_db_name,
    )

engine = create_engine(get_db_url())

SessionLocal = sessionmaker(autocommit = False , autoflush= False , bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally :
        db.close()