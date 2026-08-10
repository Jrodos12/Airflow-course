from src.price_pipeline import *
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
    'Dag_xcom_pipeline',
    default_args=default_args,
    description='use of xcomm to create a pipeline',
    schedule=None,
    catchup=False,
    tags=['xcomm']
) as dag:
    show_price = PythonOperator (
        task_id='get_price',
        python_callable=get_price,
        op_kwargs={'price':100}
    )
    show_discount = PythonOperator (
        task_id='apply_discount',
        python_callable=apply_discount,
    )
    show_taxes = PythonOperator (
        task_id='add_tax',
        python_callable=add_tax,
    )
    show_final = PythonOperator (
        task_id='print_final_price',
        python_callable=print_final_price,
    )
    show_price >> show_discount >> show_taxes >> show_final