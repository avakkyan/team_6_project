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


def fetch_value_from_table(table_name, column_name, condition_column, condition_value):
    query = f"SELECT {column_name} FROM dds.{table_name}"
    if condition_column and condition_value:
        query += f" WHERE {condition_column} = {condition_value}"
    with engine.connect() as connection:
        result = connection.execute(query).fetchone()
    return result[0] if result else None

# Function to load data from CSV into DataFrame
def get_from_csv(table_name, delimiter=';'):
    csv_file_path = f'C:/Users/5054671/PycharmProjects/team_6_project/DWH/etl/files_csv/{table_name}.csv'
    return pd.read_csv(csv_file_path, delimiter=delimiter)

# Function to transform data
def transform_data(df, table_name):
    df['source_table'] = table_name

    if table_name == 'базы_данных_и_уровень_знаний_сотру':
        df['date_first'] = df['дата']
        df['date_last'] = df['дата']
        value = fetch_value_from_table(table_name='category_id', column_name='id', condition_column="название", condition_value=table_name)
        df['category_know_id'] = value
        df['know_id'] = df['id']
        #TODO level_id
        #TODO know_id value_level = fetch_value_from_table(table_name='category_id', column_name='id', condition_column="название", condition_value=table_name)



    elif table_name == 'опыт_сотрудника_в_предметных_обла':
        df['experience_type'] = 'subject_area'

    # Add other transformations as needed
    return df


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


def load_table(table_name):
    query = f"SELECT * FROM dds.{table_name}"
    df = pd.read_sql(query, engine)

    df_cleaned = transform_data(df, table_name)

    df_cleaned.to_sql(table_name, engine, schema='avakyan_dm', if_exists='append', index=False)
    print(f"Table {table_name} cleaned and loaded successfully.")


def main():
    tables_original = [
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
        # 'category_know',
        # 'period',
    ]

    tables_to_combine = [
        'базы_данных_и_уровень_знаний_сотру',
        'инструменты_и_уровень_знаний_сотр',
        'опыт_сотрудника_в_отраслях',
        'опыт_сотрудника_в_предметных_обла',
        'платформы_и_уровень_знаний_сотруд',
        'среды_разработки_и_уровень_знаний_',
        'технологии_и_уровень_знаний_сотру',
        'типы_систем_и_уровень_знаний_сотру',
        'фреймворки_и_уровень_знаний_сотру',
        'языки_пользователей',
        'языки_программирования_и_уровень',

    ]

    for table in tables_original:
        load_and_clean_table(table)
    for table in tables_to_combine:
        load_table(table)

    print("All tables processed and loaded into DM successfully.")


if __name__ == '__main__':
    main()
