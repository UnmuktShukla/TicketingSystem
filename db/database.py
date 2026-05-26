from typing import final
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

_db_name = os.getenv('DATABASE')
_db_username = os.getenv('DB_USERNAME')
_db_password = os.getenv('DB_PASSWORD')
_db_host = os.getenv('HOST')
_db_port = os.getenv('PORT')

URL_BASE = f"postgresql://{_db_name}:{_db_password}@{_db_host}:{_db_port}"

engine = create_engine(URL_BASE)

SessionLocal = sessionmaker(autocommit = False , autoflush= False , bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally :
        db.close()