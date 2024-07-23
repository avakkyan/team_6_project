import pandas as pd
import configparser
from sqlalchemy import create_engine, text, MetaData, Table

config = configparser.ConfigParser()
config.read('config.ini')

target_host = config['target_database']['host']
target_port = config['target_database']['port']
target_database = config['target_database']['database']
target_user = config['target_database']['user']
target_password = config['target_database']['password']
conn_str = f"postgresql://{target_user}:{target_password}@{target_host}:{target_port}/{target_database}"
engine = create_engine(conn_str)


def fetch_value_from_table(schema, table_name, column_name, condition_column, condition_value):
    query = text(f"SELECT {column_name} FROM {schema}.{table_name} WHERE {condition_column} = :condition_value")
    with engine.connect() as connection:
        try:
            result = connection.execute(query, {'condition_value': condition_value}).fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def get_from_csv(table_name, delimiter=';'):
    csv_file_path = f'C:/Users/5054671/PycharmProjects/team_6_project/DWH/etl/files_csv/{table_name}.csv'
    return pd.read_csv(csv_file_path, delimiter=delimiter)


# Function to load table data
def load_table(table_name, schema='dds'):
    query = f"SELECT * FROM {schema}.{table_name}"
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)
    return df


def find_period_id(periods_df, date_first, date_last):
    period_row = periods_df[
        ((periods_df['начало_периода'] < date_last) & (date_last < periods_df['конец_периода'])) |
        ((periods_df['начало_периода'] < date_first) & (date_first < periods_df['конец_периода']))
    ]
    if not period_row.empty:
        return period_row.iloc[0]['id']
    return None

def update_growth(df):
    cte = df.groupby(['User ID', 'category_know_id', 'know_id']).agg(
        max_level=('n_level', 'max'),
        min_level=('n_level', 'min')
    ).reset_index()

    updated_df = pd.merge(df, cte, on=['User ID', 'category_know_id', 'know_id'], how='left', suffixes=('', '_cte'))

    df['growth'] = updated_df.apply(
        lambda row: 1 if pd.isna(row['max_level']) else row['max_level'] - row['min_level'] + 1,
        axis=1
    )

    max_level_df = df[df['n_level'] == df.groupby(['User ID', 'category_know_id', 'know_id'])['n_level'].transform('max')]

    return max_level_df

def transform_data(df, table_name):
    levels_df = load_table('levels', schema='dm_avakyan')
    periods_df = load_table('period', schema='dm_avakyan')
    df.drop(columns=['активность'], inplace=True)
    if table_name == 'базы_данных_и_уровень_знаний_сотру':
        df['date_first'] = df['дата']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название', 'Базы данных ')
        df['category_know_id'] = category_know_id
        df["know_id"] = df["Базы данных"]

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень знаний',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']), axis=1)
        df.drop(columns=['Дата изм.', 'Базы данных', 'Уровень знаний', 'дата'], inplace=True)
        df['id'] = range(1, len(df) + 1)

        df['growth'] = 1
        df = update_growth(df)

    elif table_name == 'инструменты_и_уровень_знаний_сотр':
        df['date_first'] = df['дата']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название', 'Инструменты ')
        df['category_know_id'] = category_know_id
        df["know_id"] = df["инструменты"]

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень знаний',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']), axis=1)
        df.drop(columns=['Дата изм.', 'инструменты', 'Уровень знаний', 'дата'], inplace=True)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        df['growth'] = 1
        df = update_growth(df)

    elif table_name == 'среды_разработки_и_уровень_знаний_':
        df['date_first'] = df['дата']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название', 'Среда разработки ')
        df['category_know_id'] = category_know_id
        df["know_id"] = df["Среды разработки"]

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень знаний',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']), axis=1)
        df.drop(columns=['Дата изм.', 'Среды разработки', 'Уровень знаний', 'дата'], inplace=True)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        df['growth'] = 1
        df = update_growth(df)

    elif table_name == 'платформы_и_уровень_знаний_сотруд':
        df['date_first'] = df['дата']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название', 'Платформы ')
        df['category_know_id'] = category_know_id
        df["know_id"] = df["платформы"]

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень знаний',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']), axis=1)
        df.drop(columns=['Дата изм.', 'платформы', 'Уровень знаний', 'дата'], inplace=True)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        df['growth'] = 1
        df = update_growth(df)

    elif table_name == 'типы_систем_и_уровень_знаний_сотру':
        df['date_first'] = df['дата']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название', 'Типы систем ')
        df['category_know_id'] = category_know_id
        df["know_id"] = df["Типы систем"]

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень знаний',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']), axis=1)
        df.drop(columns=['Дата изм.', 'Типы систем', 'Уровень знаний', 'дата'], inplace=True)

        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        df['growth'] = 1
        df = update_growth(df)

    elif table_name == 'фреймворки_и_уровень_знаний_сотру':
        df['date_first'] = df['дата']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название', 'Фреймворки ')
        df['category_know_id'] = category_know_id
        df["know_id"] = df["фреймворки"]

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень знаний',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']), axis=1)
        df.drop(columns=['Дата изм.', 'фреймворки', 'Уровень знаний', 'дата'], inplace=True)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        df['growth'] = 1
        df = update_growth(df)

    elif table_name == 'языки_программирования_и_уровень':
            df['date_first'] = df['дата']
            df['date_last'] = df['Дата изм.']
            category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название',
                                                      'Язык программирования ')
            df['category_know_id'] = category_know_id
            df["know_id"] = df["Языки программирования"]

            df = df.merge(
                levels_df[['id', 'n_level']],
                left_on='Уровень знаний',
                right_on='id',
                how='left'
            )
            df['level_id'] = df['id_y']
            df['n_level'] = df['n_level']
            df.drop(columns=['id_y', 'id_x'], inplace=True)

            df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']),
                                       axis=1)
            with engine.connect() as connection:
                result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
                current_max_id = result.scalar()

            df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

            df = update_growth(df)

            columns_to_drop = ['Дата изм.', 'Языки программирования', 'Уровень знаний', 'дата']
            df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    elif table_name == 'технологии_и_уровень_знаний_сотру':
            df['date_first'] = df['дата']
            df['date_last'] = df['Дата изм.']
            category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название',
                                                      'Технологии ')
            df['category_know_id'] = category_know_id
            df["know_id"] = df["технологии"]

            df = df.merge(
                levels_df[['id', 'n_level']],
                left_on='Уровень знаний',
                right_on='id',
                how='left'
            )
            df['level_id'] = df['id_y']
            df['n_level'] = df['n_level']
            df.drop(columns=['id_y', 'id_x'], inplace=True)

            df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']),
                                       axis=1)
            with engine.connect() as connection:
                result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
                current_max_id = result.scalar()

            df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

            df = update_growth(df)

            columns_to_drop = ['Дата изм.', 'технологии', 'Уровень знаний', 'дата']
            df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    elif table_name == 'опыт_сотрудника_в_отраслях':
            df['date_first'] = df['дата']
            df['date_last'] = df['Дата изм.']
            category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название',
                                                      'Отрасли ')
            df['category_know_id'] = category_know_id

            df["know_id"] = df["отрасли"]

            df = df.merge(
                levels_df[['id', 'n_level']],
                left_on='Уровень знаний в отрасли',
                right_on='id',
                how='left'
            )
            df['level_id'] = df['id_y']
            df['n_level'] = df['n_level']
            df.drop(columns=['id_y', 'id_x'], inplace=True)

            df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']),
                                       axis=1)
            with engine.connect() as connection:
                result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
                current_max_id = result.scalar()

            df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

            columns_to_drop = ['Дата изм.', 'отрасли', 'Уровень знаний в отрасли', 'дата']
            df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    elif table_name == 'опыт_сотрудника_в_предметных_обла':
        df['date_first'] = df['дата']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название',
                                                  'Предметные области ')
        df['category_know_id'] = category_know_id

        df["know_id"] = df["Предметные области"]

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень знаний в предметной облас',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']),
                                   axis=1)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        columns_to_drop = ['Дата изм.', 'Предметные области', 'Уровень знаний в предметной облас', 'дата']
        df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    elif table_name == 'языки_пользователей':
        df['date_first'] = df['Дата изм.']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название',
                                                  'Языки ')
        df['category_know_id'] = category_know_id

        df["know_id"] = df["язык"]

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень знаний ин. языка',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']),
                                   axis=1)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        columns_to_drop = ['Дата изм.', 'язык', 'Уровень знаний ин. языка', 'дата', 'название']
        df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    elif table_name == 'образование_пользователей':
        df['date_first'] = df['Дата изм.']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название',
                                                  'Образование ')
        df['category_know_id'] = category_know_id

        df = df.merge(
            levels_df[['id', 'n_level']],
            left_on='Уровень образования',
            right_on='id',
            how='left'
        )
        df['level_id'] = df['id_y']
        df['n_level'] = df['n_level']
        df.drop(columns=['id_y', 'id_x'], inplace=True)

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']),
                                   axis=1)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        columns_to_drop = ['Дата изм.', 'Уровень образования', 'Название учебного заведения', 'Год окончания', 'Фиктивное название']
        df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    elif table_name == 'сертификаты_пользователей':
        df['date_first'] = df['Дата изм.']
        df['date_last'] = df['Дата изм.']
        category_know_id = fetch_value_from_table('dm_avakyan', 'category_know', 'id', 'название',
                                                  'Сертификаты ')
        df['category_know_id'] = category_know_id

        df['period_id'] = df.apply(lambda row: find_period_id(periods_df, row['date_first'], row['date_last']),
                                   axis=1)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COALESCE(MAX(id), 0) FROM dm_avakyan.summary_tab"))
            current_max_id = result.scalar()

        df['id'] = range(current_max_id + 1, current_max_id + 1 + len(df))

        columns_to_drop = ['Дата изм.', 'Организация, выдавшая сертификат', 'Наименование сертификата', 'Год сертификата']
        df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)
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


def load_table_and_transform(table_name):
    query = f"SELECT * FROM dds.{table_name}"
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)

    df_cleaned = transform_data(df, table_name)

    df_cleaned.to_sql('summary_tab', engine, schema='dm_avakyan', if_exists='append', index=False)
    print(f"Table {table_name} cleaned and loaded successfully into summary_tab.")


def main():

    tables_original = [
         'сотрудники_дар',
         #'category_know',
          'period',
    ]

    tables_to_combine = [
        'базы_данных_и_уровень_знаний_сотру',
        'инструменты_и_уровень_знаний_сотр',
        'среды_разработки_и_уровень_знаний_',
        'платформы_и_уровень_знаний_сотруд',
        'типы_систем_и_уровень_знаний_сотру',
        'фреймворки_и_уровень_знаний_сотру',
        'языки_программирования_и_уровень',
        'опыт_сотрудника_в_отраслях',
        'опыт_сотрудника_в_предметных_обла',
        'языки_пользователей',
        'технологии_и_уровень_знаний_сотру',
         'образование_пользователей',
    ]

    for table in tables_original:
        load_and_clean_table(table)
    for table in tables_to_combine:
        load_table_and_transform(table)

    print("All tables processed and loaded into DM successfully.")


if __name__ == '__main__':
    main()
