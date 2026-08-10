from src.greetment import greet_hello,greet_with_city
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
    'Task_with_arguments',
    default_args=default_args,
    description='Dag usign python with arguments',
    schedule=timedelta(days=1),
    catchup= False,
    tags=['arguments']
) as dag:

    task_with_arguments_a = PythonOperator(
        task_id='arguments',
        python_callable= greet_hello,
        op_kwargs={'name':'Tobias'}
    )
    task_with_arguments_b = PythonOperator(
        task_id='two_arguments',
        python_callable=greet_with_city,
        op_kwargs={'name':'Tobias', 'city':'Buenos Aires'}
    )

    task_with_arguments_a >> task_with_arguments_b