# Importing required libraries
import os
import geopandas as gpd
from dotenv import load_dotenv

# Recovering dotenv variables
load_dotenv()

# Defining files path
UPZ_FILES_PATH: str = os.getenv('UPZ_FILES_PATH')

def extract() -> gpd.GeoDataFrame:
    gdf: gpd.GeoDataFrame = gpd.GeoDataFrame()
    
    for file in os.listdir(UPZ_FILES_PATH):
        if file.endswith('geojson'):
            absolute_path: str = os.path.join(UPZ_FILES_PATH, file)
            gdf = gpd.read_file(absolute_path)
    return gdf
