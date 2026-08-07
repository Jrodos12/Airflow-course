from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from datetime import timedelta

def print_hello():
    print('Hello world from first DAG!')


default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG('first_dag',
        default_args=default_args,
        schedule=timedelta(days=1),
        ) as dag:

    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

