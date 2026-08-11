from airflow.sdk import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'jrodo',
    'start_date':datetime(2026,1,1),
    'depends_on_past': False,
    'retries': 2,
    'retry_delay':timedelta(minutes=2)
}
with DAG(
    'first_sql_dag',
    default_args=default_args,
    description='use of sql operator for  queries',
    schedule=None,
    catchup=False,
    tags=['sql']
) as dag:
    create_table = SQLExecuteQueryOperator(
        task_id= 'create_table',
        sql="""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            age INTEGER NOT NULL,
            is_active BOOL DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            conn_id='my_sqlite_conection'
    )
    delete_table = SQLExecuteQueryOperator(
        task_id= 'delete_table',
        sql="""
            DROP TABLE users
            """,
            conn_id='my_sqlite_conection'
    )

    delete_table >> create_table