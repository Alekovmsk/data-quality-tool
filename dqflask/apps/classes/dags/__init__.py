from ..database import DqConnection
from ..conf import ConfYaml
import paramiko
import sys


class Dag(ConfYaml):
    dq_connection = DqConnection('dqServer')

    def __init__(self, dqi=None, source=None, sql=None, cron=None, crossdb=False, src_cnt=None, sql_list=None,
                 source_list=None, custom_name_list=None):
        self.airflow_venv = str(self.config['server']['airflow']['venvpath'])
        self.airflow_path = str(self.config['server']['airflow']['path'])
        self.airflow_host = str(self.config['server']['airflow']['host'])
        self.airflow_user = str(self.config['server']['airflow']['username'])
        self.airflow_pass = str(self.config['server']['airflow']['password'])
        self.dqi = dqi
        self.source = source
        self.sql = sql
        self.cron = cron

        # cross-database
        self.src_sql = []
        self.crossdb = crossdb
        if crossdb:
            for cur in range(src_cnt):
                self.src_sql.append(
                    {
                        'source': source_list[cur],
                        'sql': sql_list[cur],
                        'src_name': custom_name_list[cur]
                    }
                )

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.airflow_host, username=self.airflow_user, password=self.airflow_pass)

    def deploy_dag(self):
        if self.crossdb:
            ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(
                f'source {self.airflow_venv} && '
                f'python {self.airflow_path}/DeployDqDagCrdb.py "{self.dqi}" "{self.sql}" "{self.cron}" "{self.src_sql}"'
            )
        else:
            ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(
                f'source {self.airflow_venv} && '
                f'python {self.airflow_path}/DeployDqDag.py "{self.dqi}" "{self.sql}" "{self.source}" "{self.cron}"'
            )
        print(ssh_stderr.read(), file=sys.stderr)

    def remove_dag(self):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(
            f'source {self.airflow_venv} && '
            f'python {self.airflow_path}/RemoveDqDag.py "{self.dqi}"'
        )
        print(ssh_stderr.read(), file=sys.stderr)
