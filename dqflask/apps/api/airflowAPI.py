import requests
import datetime
from datetime import timedelta
from ..classes.conf import ConfYaml
import json


class AirflowAPI:
    def __init__(self):

        url = str(ConfYaml.config['airflowAPI']['url'])
        if url.endswith('/'):
            self.url = url
        else:
            self.url = url + '/'

        self.auth = (ConfYaml.config['airflowAPI']['auth']['login'], ConfYaml.config['airflowAPI']['auth']['password'])
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

    def get_running_runs(self, id):
        endpoint = f'{self.url}dq_{str(id)}/dagRuns'
        params = {'state': 'running,queued'}
        response = requests.get(endpoint, headers=self.headers, params=params, auth=self.auth, verify=False)
        run = json.loads(response.text)
        if run['total_entries'] != 0:
            return run['dag_runs'][0]
        else:
            return None

    def unpause_dag(self, id):
        endpoint = self.url + 'dq_' + str(id)
        params = {'update_mask': 'is_paused'}
        json_data = {'is_paused': False}
        response = requests.patch(endpoint, params=params, headers=self.headers, json=json_data, auth=self.auth,
                                  verify=False)
        return response.text

    def pause_dag(self, id):
        endpoint = self.url + 'dq_' + str(id)
        params = {'update_mask': 'is_paused'}
        json_data = {'is_paused': True}
        response = requests.patch(endpoint, params=params, headers=self.headers, json=json_data, auth=self.auth,
                                  verify=False)
        return response.text

    def trigger_dag(self, id):
        endpoint = self.url + 'dq_' + str(id) + '/dagRuns'
        json_data = {
            'logical_date': (datetime.datetime.now() + timedelta(hours=-3)).strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        response = requests.post(endpoint, headers=self.headers, json=json_data, auth=self.auth, verify=False)
        return response.text

    def kill_dag(self, id):
        run = self.get_running_runs(id)
        if run is None:
            return None
        run_id = run['dag_run_id']
        endpoint = self.url + 'dq_' + str(id) + '/dagRuns/' + str(run_id)
        json_data = {'state': 'failed'}
        response = requests.patch(endpoint, headers=self.headers, json=json_data, auth=self.auth, verify=False)
        return response.text
