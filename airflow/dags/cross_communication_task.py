from src.counter_operations import add_counter, multiply_counter
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'jrodo',
    'start_date':datetime(2026,1,1),
    'depends_on_past': False,
    'retries': 2,
    'retry_delay':timedelta(minutes=2)
}
with DAG(
    'Dag_xcomm',
    default_args=default_args,
    description='use of xcomm to share values',
    schedule=None,
    catchup=False,
    tags=['xcomm']
) as dag:
    task_add = PythonOperator (
        task_id='add_to_number',
        python_callable=add_counter,
        op_kwargs={'counter':1}
    )
    task_multiply = PythonOperator (
        task_id='mutiply_to_number',
        python_callable=multiply_counter,
        op_kwargs={'counter':9}
    )