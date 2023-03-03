import geopandas as gpd

from watchguardmodel.database.engine import engine

def extract() -> gpd.GeoDataFrame:
    return gpd.read_postgis(
        sql='SELECT * FROM catastral_parcels', 
        con=engine, 
        geom_col='geometry',
        index_col='CMIUSCAT'
    )
