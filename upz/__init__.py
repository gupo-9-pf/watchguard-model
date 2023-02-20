from .extractor import extract
from .transformer import transform
from .loader import load

def execute():
    gdf = extract()
    gdf = transform(gdf)
    load(gdf)
