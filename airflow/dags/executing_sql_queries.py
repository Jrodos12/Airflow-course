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
    'sql_executing',
    default_args=default_args,
    description='use of sql operator for print values from a table',
    schedule=None,
    catchup=False,
    tags=['sql']
) as dag:
    insert_values = SQLExecuteQueryOperator(
        task_id= 'insert_values_1',
        sql="""
            insert into users (name,age,is_active) VALUES
            ('Julie',30,false),
            ('Peter',55,true),
            ('Emily',37,false),
            ('Katrina',54,false),
            ('Joshep',27,true);
            """,
            conn_id='my_sqlite_conection'
    )
    insert_values_2 = SQLExecuteQueryOperator(
        task_id= 'insert_values_2',
        sql="""
            insert into users (name,age) VALUES
            ('Harry',49),
            ('Nancy',52),
            ('Elvis',26),
            ('Mia',20);
            """,
            conn_id='my_sqlite_conection'
    )
    display_user = SQLExecuteQueryOperator(
        task_id= 'select_users',
        do_xcom_push=True,
        handler=lambda cursor: cursor.fetchall(),
        show_return_value_in_logs= True,
        sql="""
            SELECT * FROM users;
            """,
            conn_id='my_sqlite_conection'
    )
    [insert_values,insert_values_2] >> display_user