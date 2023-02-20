from config.db import connection_engine
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, MetaData, String

# Create metadata object
metadata = MetaData()

# Define a table
table = Table('relations', metadata,
        Column('CODE_CAT', String),
        Column('CODE_UPZ', String)
    )

# Execute a query
conn = connection_engine.connect()
re = 'UPZ22'
result = conn.execute(f"select * from relations where \"code_upz\"= '{re}'")
for row in result:
    print(row)