import pandas as pd
import geopandas as gpd

from watchguardmodel.catastralparcel.utils.counts import get_counts

def transform(catastral: gpd.GeoDataFrame) -> pd.DataFrame:
    order = {}
    for index, row in catastral.iterrows():
        order[index] = get_counts(gdf=catastral.loc[index])
    order_df = pd.DataFrame.from_dict(data=order, orient='index')
    order_percentage = (order_df.iloc[:, :-1] / order_df.iloc[:, -1].values.reshape(-1, 1)).round(3)
    order_percentage = order_percentage.fillna(0)
    return order_df, order_percentage
