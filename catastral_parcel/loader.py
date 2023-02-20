import geopandas as gpd

from sqlalchemy import Table, MetaData

from ..config import db

def load(gdf: gpd.GeoDataFrame) -> None:
    try:
        catastral_table = Table('catastral_parcels', MetaData(), autoload=True, autoload_with=db.connection_engine)
        catastral_table.drop(db.connection_engine)        
    except:
        pass
    gdf.to_postgis(name='catastral_parcels', con=db.connection_engine, if_exists='fail', index=False)
