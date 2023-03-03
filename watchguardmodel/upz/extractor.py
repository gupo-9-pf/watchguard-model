import pandas as pd
import geopandas as gpd

from watchguardmodel.database.engine import engine

def extract() -> gpd.GeoDataFrame:
    upz_gdf = gpd.read_postgis(
        sql='SELECT * FROM upz', 
        con=engine, 
        geom_col='geometry',
        index_col='CMIUUPLA'
    )
    crime_df = pd.read_sql(
        sql='SELECT * FROM crime_reports', 
        con=engine,
        index_col='index'
    )
    severity_df = pd.read_sql(
        sql='SELECT * FROM modality_severity', 
        con=engine
    )
    return upz_gdf, crime_df, severity_df
