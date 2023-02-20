# Importing required libraries
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Recovering environment variables
load_dotenv()

# Defining db properties
DB_ENGINE = os.getenv('DB_ENGINE')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE_NAME = os.getenv('DB_DATABASE_NAME')

try:

    connection_engine = create_engine(f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE_NAME}')
except Exception:
    raise
