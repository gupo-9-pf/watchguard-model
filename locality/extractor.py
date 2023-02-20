# Importing required libraries
import os
import geopandas as gpd
from dotenv import load_dotenv

# Recovering dotenv variables
load_dotenv()

# Defining files path
LOCALITY_FILES_PATH = os.getenv('LOCALITY_FILES_PATH')


def extract():
    gdf = gpd.GeoDataFrame()
    dir = LOCALITY_FILES_PATH
    for file in os.listdir(dir):
        if file.endswith('geojson'):
            absolute_path = os.path.join(dir, file)
            gdf = gpd.read_file(absolute_path)
    return gdf
