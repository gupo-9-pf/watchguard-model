from .extractor import extract
from .transformer import transform
from .loader import load

def execute():
    df = extract()
    df = transform(df)
    load(df)