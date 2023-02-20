from config.db import connection_engine
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, MetaData, String

# Create metadata object
metadata = MetaData()

# Define a table
table = Table('modality_severity', metadata,
        Column('modality', String),
        Column('severity', String)
    )

# Execute a query
conn = connection_engine.connect()
re = 'raponazo'
result = conn.execute(f"select * from modality_severity where \"modality\"= '{re}'")
for row in result:
    print(row)