from watchguardmodel.catastralparcel.loader import load
from watchguardmodel.catastralparcel.extractor import extract
from watchguardmodel.catastralparcel.trasformer import transform

def execute():
    df = extract()
    df, per = transform(df)
    load(df, per)
