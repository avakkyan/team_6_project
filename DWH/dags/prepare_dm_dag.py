from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ETL_DIR = os.path.join(BASE_DIR, '../../../..', 'etl')
PREPARE_SCRIPT = os.path.join(ETL_DIR, 'prepare_dm.py')

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
    'prepare_dm_dag',
    description='DAG for preparing data DM',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 8, 1),
    catchup=False,
    default_args=default_args,
)

prepare_data = PythonOperator(
    task_id='prepare_data',
    python_callable=run_script_with_db,
    op_args=[PREPARE_SCRIPT],
    dag=dag
)
