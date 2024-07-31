from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ETL_DIR = os.path.join(BASE_DIR, '..', 'etl')
DDS_SCRIPT = os.path.join(ETL_DIR, 'dds_transform_data.py')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


def run_script_with_db(script_path):
    os.system(f"python {script_path}")


dag = DAG(
    'transform_data',
    description='DAG for loading data to DDS layer',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 11, 7),
    catchup=False,
    default_args=default_args,
)

dds_transform = PythonOperator(
    task_id='dds_transform',
    python_callable=run_script_with_db,
    op_args=[DDS_SCRIPT, 'postgres_db_6'],
    dag=dag
)
