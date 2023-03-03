import pandas as pd

from watchguardmodel.database.engine import engine

def load(order: pd.DataFrame, percentage: pd.DataFrame) -> None:
    order.to_sql('order_crime_upz',engine, if_exists='replace')
    percentage.to_sql('order_crime_upz_perc', engine, if_exists='replace')
