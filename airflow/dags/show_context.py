from src.context import show_context,show_context_clearly
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
    'Show_context',
    default_args=default_args,
    description='Show the context of the DAG using python operator',
    schedule=timedelta(days=1),
    catchup= False,
    tags=['context']
) as dag:

    task_with_arguments_a = PythonOperator(
        task_id='show_context',
        python_callable= show_context,
    )
    task_with_arguments_b = PythonOperator(
        task_id='show_context_clearly',
        python_callable= show_context_clearly,
    )
    task_with_arguments_a >> task_with_arguments_b
