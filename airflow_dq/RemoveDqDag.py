import os
from sys import argv


script, dqi = argv


def delete_dag(dqi):
    os.remove(f'/app/airflow/dags/SSDQ/dq_{dqi}.py')


delete_dag(dqi)
