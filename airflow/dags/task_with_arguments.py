import src.greetment as greeting
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'jrodo',
    'start_date':datetime(2026,1,1),
    'depends_on_past': False,
    'email_on_failure':'tobiasriverotrujillo@gmail.com',
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

    task_with_arguments = PythonOperator(
        task_id='arguments',
        python_callable= greeting.greet_hello,
    )
