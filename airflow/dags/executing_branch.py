from airflow.sdk import DAG
from src.driver_license import has_driver_license,elegible_to_drive,not_elegible_to_drive,brancher
from airflow.providers.standard.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'jrodo',
    'start_date':datetime(2026,1,1),
    'depends_on_past': False,
    'retries': 2,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    'First_DAG_with_branch',
    description='Branch the flow depending of having or not a license',
    default_args=default_args,
    schedule=None,
    catchup=False,
    start_date=datetime(2026,1,1),
    tags=['Branching']
) as dag:
    has_driver_license_task = PythonOperator(
        task_id='has_driver_license',
        python_callable=has_driver_license
    )
    branching_task = BranchPythonOperator(
        task_id='branch',
        python_callable=brancher
    )
    eligible_task = PythonOperator(
        task_id='eligible_to_drive',
        python_callable=not_elegible_to_drive
    )
    not_eligible_task = PythonOperator(
        task_id='not_elegible_to_drive',
        python_callable=elegible_to_drive
    )
    has_driver_license_task >> branching_task >> [eligible_task,not_eligible_task]