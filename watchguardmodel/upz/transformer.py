import pandas as pd
import geopandas as gpd

from watchguardmodel.upz.utils.counts import get_counts

def transform(upz: gpd.GeoDataFrame, crimes: pd.DataFrame, severity: pd.DataFrame):
    order_data = {}
    for index, row in upz.iterrows():
        filter_df = crimes.query("upz == @row['CMNOMUPLA']")
        order_data[index] = get_counts(df=filter_df,severity_data=severity)
    order_df = pd.DataFrame.from_dict(data=order_data, orient='index')
    order_percentage = (order_df.iloc[:, :-1] / order_df.iloc[:, -1].values.reshape(-1, 1)).round(3)
    order_percentage['type_1_events'] = order_percentage['type_1_events'] * 1
    order_percentage['type_2_events'] = order_percentage['type_2_events'] * 2
    order_percentage['type_3_events'] = order_percentage['type_3_events'] * 3
    return order_df, order_percentage
