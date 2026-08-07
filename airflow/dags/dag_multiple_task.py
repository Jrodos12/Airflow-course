from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from datetime import timedelta

def print_hello():
    print('Hello world from task A!')

def print_goodbye():
    print('Goodbye from task B!')

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG('second_DAG',
        default_args=default_args,
        schedule=timedelta(days=1),
        tags=['second_script']
        ) as dag:

    task1 = PythonOperator(
        task_id='task_A',
        python_callable=print_hello,
    )
    task2 = PythonOperator(
        task_id='task_B',
        python_callable=print_goodbye,
    )

