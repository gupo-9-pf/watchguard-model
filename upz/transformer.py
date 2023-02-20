# Importing required libraries
import pandas as pd
import geopandas as gpd 
from ..config import db, COLUMNS

def transform (gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    try:
        locality_data: gpd.GeoDataFrame = gpd.GeoDataFrame.from_postgis(sql='SELECT * FROM localities', 
                                                                        con=db.connection_engine, 
                                                                        geom_col='geometry')
    except ValueError as error:
        print(error)
    gdf = clean_upz(upz_gdf=gdf, locality_gdf=locality_data).filter(items=COLUMNS['columns'])
    gdf = refactor_text(geo_data_frame=gdf)
    return gdf

def clean_upz(upz_gdf: gpd.GeoDataFrame, locality_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    gdf = gpd.GeoDataFrame()
    for locality_index, locality in locality_gdf.iterrows():
        intersection = upz_gdf.intersection(other=locality['geometry'], align=False)
        majority = (intersection.area / upz_gdf.area) > 0.5
        aux_gdf = upz_gdf[majority].copy()
        aux_gdf['CMNOMLOCAL'] = locality['CMNOMLOCAL']
        aux_gdf.set_index('CMIUUPLA')
        gdf = pd.concat([gdf, aux_gdf])
    return gdf

def refactor_text(geo_data_frame: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geo_data_frame['CMNOMUPLA'] = geo_data_frame['CMNOMUPLA'].str.lower()
    geo_data_frame['CMMES'] = geo_data_frame['CMMES'].str.lower()
    return geo_data_frame
