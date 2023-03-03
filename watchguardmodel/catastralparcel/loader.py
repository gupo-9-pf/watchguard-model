import pandas as pd

from watchguardmodel.database.engine import engine

def load(df: pd.DataFrame, percentage: pd.DataFrame) -> None:
    df.to_sql(name='order_crime_catastral', con=engine, if_exists='replace')
    percentage.to_sql(name='order_crime_catastral_per', con=engine, if_exists='replace')
