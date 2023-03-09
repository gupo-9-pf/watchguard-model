import geopandas as gpd

def get_counts(gdf: gpd.GeoDataFrame) -> dict:
    return {
        'car': gdf.filter(regex='CMHA.*').sum(),
        'motorbike': gdf.filter(regex='CMHM.*').sum(),
        'bike': gdf.filter(regex='CMHB.*').sum(),
        'foot': gdf.filter(regex='CMHP.*|CMHCE.*').sum(),
        'total': gdf.filter(regex='CMH.*').sum()
    }
