import pandas as pd
import configparser
from sqlalchemy import create_engine

# Read database configuration from config file
config = configparser.ConfigParser()
config.read('config.ini')

# Database connection string
target_host = config['target_database']['host']
target_port = config['target_database']['port']
target_database = config['target_database']['database']
target_user = config['target_database']['user']
target_password = config['target_database']['password']
conn_str = f"postgresql://{target_user}:{target_password}@{target_host}:{target_port}/{target_database}"
engine = create_engine(conn_str)

# Function to load data from CSV into DataFrame
def get_from_csv(table_name, delimiter=';'):
    csv_file_path = f'C:/Users/5054671/PycharmProjects/team_6_project/DWH/etl/files_csv/{table_name}.csv'
    return pd.read_csv(csv_file_path, delimiter=delimiter)

# Function to load and clean table data
def load_and_clean_table(table_name):
    if table_name == 'category_know' or table_name == 'period':
        df = get_from_csv(table_name)
        df.to_sql(table_name, engine, schema='dm_avakyan', if_exists='append', index=False)
    else:
        query = f"SELECT * FROM dds.{table_name}"
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
        df.to_sql(table_name, engine, schema='dm_avakyan', if_exists='append', index=False)

    print(f"Table {table_name} cleaned and loaded successfully.")

def main():
    tables = [
        # 'базы_данных',
        # 'инструменты',
        # 'языки',
        # 'уровни_владения_ин',
        # 'среды_разработки',
        # 'фреймворки',
        # 'платформы',
        # 'отрасли',
        # 'технологии',
        # 'типы_систем',
        # 'уровни_знаний',
        # 'языки_программирования',
        # 'уровни_знаний_в_отрасли',
        # 'уровни_знаний_в_предметной_област',
        # 'предметная_область',
        # 'уровень_образования',
        # 'сотрудники_дар',
        # 'сертификаты_пользователей',
        #'category_know',
        #'period',
    ]

    for table in tables:
        load_and_clean_table(table)

    print("All tables processed and loaded into DM successfully.")

if __name__ == '__main__':
    main()
