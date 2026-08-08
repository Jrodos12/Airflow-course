from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from datetime import timedelta

def task_a():
    print('Hello world from task A!')

def task_b():
    print('Hello world from task B!')

def task_c():
    print('Hello world after A and B from task C!')

def task_d():
    print('Hello world after A and B from task D!')

def task_e():
    print('Hello world after A and B from task E!')

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG('Dag_with_dependecies',
        default_args=default_args,
        schedule=timedelta(days=1),
        tags=['second_script']
        ) as dag:

    task1 = PythonOperator(
        task_id='task_A',
        python_callable=task_a,
    )
    task2 = PythonOperator(
        task_id='task_B',
        python_callable=task_b,
    )
    task3 = PythonOperator(
        task_id='task_C',
        python_callable=task_c,
    )
    task4 = PythonOperator(
        task_id='task_D',
        python_callable=task_d,
    )
    task5 = PythonOperator(
        task_id='task_E',
        python_callable=task_e,
    )
    task1 >> [task3,task4] 
    task2 >> [task3,task4]
    [task3,task4] >> task5