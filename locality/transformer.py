# Importing required libraries
import geopandas as gpd
from ..config import LOCALITIES, COLUMNS

def transform (gdf: gpd.GeoDataFrame):
    gdf = refactor_text(geo_data_frame=gdf)
    gdf = gdf.query("CMNOMLOCAL in @LOCALITIES").filter(items=COLUMNS['columns']).reset_index()
    return gdf

def refactor_text(geo_data_frame: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geo_data_frame['CMNOMLOCAL'] = geo_data_frame['CMNOMLOCAL'].str.lower()
    geo_data_frame['CMMES'] = geo_data_frame['CMMES'].str.lower()
    return geo_data_frame
