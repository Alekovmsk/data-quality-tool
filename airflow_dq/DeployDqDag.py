import os
from sys import argv


script, r_uk, sql_query, source, schedule_cron = argv


def deploy(dqi, sql, source, cron):
    if cron != "None":
        cron = f'"{cron}"'
    dag = f"""import datetime
from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from SSDQ.CustomOperator.ClassDq import DqControl


sql = \"\"\"{sql}\"\"\"
hook = PostgresHook(postgres_conn_id='{source}').get_conn()

with DAG(
    dag_id="dq_{dqi}",
    start_date=datetime(2024, 2, 1),
    schedule_interval={cron},
    catchup=False,
) as dag:

    dq_{dqi} = DqControl(
        task_id='dq_{dqi}',
        sql=sql,
        source=hook,
        dqi="{dqi}"
    )
"""

    os.chdir("/app/airflow/dags/SSDQ")
    dag_file = open(f'dq_{dqi}.py', "w")
    dag_file.write(dag)
    
deploy(r_uk, sql, source, schedule_cron)
