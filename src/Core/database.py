# app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Database URL from settings
SQLALCHEMY_DATABASE_URL = ''

# Database connection setup
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # Use SQLite for simplicity

# Base class for models
Base = declarative_base()