import pandas as pd
from sqlalchemy import create_engine

source_db_config = {
    'user': 'etl_user_6',
    'password': '+UAu{5*-',
    'host': '10.82.0.4',
    'port': '5432',
    'database': 'source'
}

target_db_config = {
    'user': 'etl_user_6',
    'password': '+UAu{5*-',
    'host': '10.82.0.4',
    'port': '5432',
    'database': 'etl_db_6'
}

source_conn_str = f"postgresql://{source_db_config['user']}:{source_db_config['password']}@{source_db_config['host']}:{source_db_config['port']}/{source_db_config['database']}"
target_conn_str = f"postgresql://{target_db_config['user']}:{target_db_config['password']}@{target_db_config['host']}:{target_db_config['port']}/{target_db_config['database']}"

source_engine = create_engine(source_conn_str)
target_engine = create_engine(target_conn_str)

def copy_table(table_name):
    df = pd.read_sql(f'SELECT * FROM {table_name}', source_engine)
    df.to_sql(table_name, target_engine, schema='raw_data', if_exists='replace', index=False)
    print(f"Table {table_name} copied successfully")

tables_query = """
SELECT table_name 
FROM information_schema.tables
WHERE table_schema = 'source_data'
"""
tables = pd.read_sql(tables_query, source_engine)

for table in tables['table_name']:
    copy_table(table)

print("All tables copied successfully")

