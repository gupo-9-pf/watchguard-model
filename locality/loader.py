import geopandas as gpd
from ..config import db

def load(gdf: gpd.GeoDataFrame) -> None:
    try:
        gdf.to_postgis(name='localities', 
                    con=db.connection_engine, 
                    if_exists='replace')
    except ValueError as error:
        print(error)
