# Importing required libraries
import os
import geopandas as gpd
from dotenv import load_dotenv

# Recovering dotenv variables
load_dotenv()

# Defining files path
CATASTRAL_FILES_PATH: str = os.getenv('CATASTRAL_FILES_PATH')

def extract() -> gpd.GeoDataFrame:
    gdf: gpd.GeoDataFrame = gpd.GeoDataFrame()
    
    for file in os.listdir(CATASTRAL_FILES_PATH):
        if file.endswith('geojson'):
            absolute_path: str = os.path.join(CATASTRAL_FILES_PATH, file)
            gdf = gpd.read_file(absolute_path)
    return gdf
