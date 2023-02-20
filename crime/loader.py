# Importing required libraries
import pandas as pd
from ..config import db

def load(df: pd.DataFrame):
    try:
        df.to_sql(name='crime_reports', 
                con=db.connection_engine, 
                if_exists='replace')
    except ValueError as err:
        print(err)
