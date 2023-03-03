# Importing required libraries
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import ArgumentError, NoSuchModuleError, OperationalError, ProgrammingError

# Recovering environment variables
load_dotenv()

# Defining db properties
DB_ENGINE = os.getenv('DB_ENGINE')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

try:
    engine = create_engine(f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
except ArgumentError as error:
    print(error)
except NoSuchModuleError as error:
    print(error)
except OperationalError as error:
    print(error)
except ProgrammingError as error:
    print(error)
