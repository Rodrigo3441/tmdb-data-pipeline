"""
=====================================================
Database Connection
=====================================================
Script Purpose:
    This script establishes a connection to the SQL Server database using
    SQLAlchemy. It defines the database connection settings and provides a
    reusable function that returns a database engine for use throughout the
    ETL pipeline.

Notes:
    - Uses Windows Authentication (Trusted Connection).
    - Creates a SQLAlchemy engine for SQL Server.
    - Database credentials are defined as configuration variables.
    - Reports an error if the connection cannot be established.
"""

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# database credentials
server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
driver = os.getenv('DB_DRIVER')

def get_connection():
    try:
        conn = create_engine(f'mssql://{server}/{database}?driver={driver}&trusted_connection=yes')
        return conn
    
    except Exception as e:
        print("Error while connecting to database by sqlalchemy:", e)