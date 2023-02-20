import geopandas as gpd
from sqlalchemy import Table, MetaData
from ..config import db

def load(gdf: gpd.GeoDataFrame) -> None:
    try:
        table = Table('upz', MetaData(), autoload=True, autoload_with=db.connection_engine)
        table.drop(db.connection_engine)
    except:
        pass

    gdf.to_postgis(name='upz', con=db.connection_engine, if_exists='fail', index=False)
