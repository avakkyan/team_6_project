import pandas as pd
from sqlalchemy import create_engine
import psycopg2

db1 = create_engine("postgresql+psycopg2://etl_user_6:+UAu{5*-@10.82.0.4:5432/source")
db2 = create_engine("postgresql+psycopg2://etl_user_6:+UAu{5*-@10.82.0.4:5432/etl_db_6")

tables=['базы_данных', 'базы_данных_и_уровень_знаний_сотру', 'инструменты',
       'инструменты_и_уровень_знаний_сотр', 'платформы', 'платформы_и_уровень_знаний_сотруд',
'сотрудники_дар', 'среды_разработки', 'среды_разработки_и_уровень_знаний_', 'технологии',
'технологии_и_уровень_знаний_сотру', 'типы_систем', 'типы_систем_и_уровень_знаний_сотру',
'уровни_владения_ин', 'уровни_знаний', 'фреймворки', 'фреймворки_и_уровень_знаний_сотру', 'языки',
'языки_пользователей', 'языки_программирования', 'языки_программирования_и_уровень']

for table in tables:
    query = f'SELECT * FROM source.source_data.{table}'
    with db1.connect() as connection:
        df = pd.read_sql(query, connection.connection)
    df.to_sql(table, db2, schema='ods', index=False, if_exists='replace')

print('базы_данных copied.')