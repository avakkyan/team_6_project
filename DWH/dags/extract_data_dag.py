from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ETL_DIR = os.path.join(BASE_DIR, '../../../..', 'etl')
EXTRACT_SCRIPT = os.path.join(ETL_DIR, 'extract_data.py')

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
    'extract_data_dag',
    description='DAG for extracting data and connecting to two DBs',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 11, 7),
    catchup=False,
    default_args=default_args,
)

extract_data = PythonOperator(
    task_id='extract_data',
    python_callable=run_script_with_db,
    op_args=[EXTRACT_SCRIPT, 'postgres', 'postgres_db_6	'],
    dag=dag
)
