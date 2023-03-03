from watchguardmodel.upz.extractor import extract
from watchguardmodel.upz.transformer import transform
from watchguardmodel.upz.loader import load

def execute():
    upz_gdf, crimes_df, severity_df = extract()
    order_df, percentage_df = transform(upz=upz_gdf, crimes=crimes_df, severity=severity_df)
    load(order=order_df, percentage=percentage_df)
