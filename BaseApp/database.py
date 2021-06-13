from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
# Dot env file load module of python
from dotenv import load_dotenv
# Load .env file variables in file os
load_dotenv()

# Get sql database url form os environment
SQLALCHEMY_DATABASE_URL = os.environ.get('SQL_DB_URL')

# Create engine using sql database url variable
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

# Make local session using sql orm session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# To create models of app use sql declarative base object
# Use Base variable
Base = declarative_base()
