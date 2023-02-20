# Importing required libraries
import pandas as pd
from ..config import LOCALITIES

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(
        columns=[
            'Fecha',
            'Mes'
        ],
        index=None
    )
    df = refactor_text(data_frame=df)
    df = df.query("localidad in @LOCALITIES").reset_index()
    return df

def refactor_text(data_frame: pd.DataFrame) -> pd.DataFrame:
    data_frame.columns = data_frame.columns.str.lower()
    data_frame.columns = data_frame.columns.str.replace(' ', '_')
    data_frame.columns = data_frame.columns.str.replace('ñ', 'ni')
    data_frame['localidad'] = data_frame['localidad'].str.replace('\d+ - ', '', regex=True)
    data_frame = data_frame.apply(lambda x: x.astype(str).str.lower())
    return data_frame
