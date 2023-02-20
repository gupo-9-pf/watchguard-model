# Importing required libraries
import pandas as pd
import geopandas as gpd 
from ..config import db, COLUMNS

def transform (gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    try:
        upz_data: gpd.GeoDataFrame = gpd.GeoDataFrame.from_postgis(sql='SELECT * FROM upz', 
                                                                        con=db.connection_engine, 
                                                                        geom_col='geometry')
    except ValueError as error:
        print(error)
    gdf = filter_castastral_parcels(upz_gdf=upz_data, catastral_gdf=gdf).filter(items=COLUMNS['columns'])
    gdf = refactor_text(geo_data_frame=gdf)
    return gdf 

def filter_castastral_parcels(upz_gdf: gpd.GeoDataFrame, catastral_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    gdf = gpd.GeoDataFrame()
    for upz_index, upz in upz_gdf.iterrows():
        intersection = catastral_gdf.intersection(other=upz['geometry'], align=False)
        majority = (intersection.area / catastral_gdf.area) > 0.5
        aux_gdf = catastral_gdf[majority].copy()
        aux_gdf.set_index('CMIUSCAT')
        gdf = pd.concat([gdf, aux_gdf], ignore_index=False)
    return gdf

def refactor_text(geo_data_frame: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geo_data_frame['CMNOMSCAT'] = geo_data_frame['CMNOMSCAT'].str.lower()
    geo_data_frame['CMMES'] = geo_data_frame['CMMES'].str.lower()
    return geo_data_frame
