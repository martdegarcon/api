# conect to the database

#imports 
# creates a connection to the database
from sqlalchemy import create_engine

# needed to create a base class
from sqlalchemy.ext.declarative import declarative_base

# factory for creating sessions
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


# autocommit = False - we need to explicitly commit changes
# autoflush = False - we need to explicitly save the changes
# bind = engine — the session is con to our connection engine
# db = SessionLocal() make a request to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()