import os
from sys import argv


script, r_uk, sql_query, schedule_cron, src_sql = argv


def deploy(dqi, sql, cron, src_sql):
    if cron != 'None':
        cron = f'"{cron}"'
    dag = f"""import datetime
from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from SSDQ.CustomOperator.ClassDq import DqControlCrdb

sql = \"\"\"{sql}\"\"\"
src_info = {src_sql}

with DAG(
    dag_id="dq_{dqi}",
    start_date=datetime(2024, 2, 1),
    schedule_interval={cron},
    catchup=False,
) as dag:

    dq_{dqi} = DqControlCrdb(
        task_id='dq_{dqi}',
        sql=sql,
        src_info=src_info,
        dqi="{dqi}"
    )
"""

    os.chdir("/app/airflow/dags/SSDQ")
    dag_file = open(f'dq_{dqi}.py', "w")
    dag_file.write(dag)
    
deploy(r_uk, sql_query, schedule_cron, src_sql)
