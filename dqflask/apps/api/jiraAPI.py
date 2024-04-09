from dqflask.apps.classes.conf import ConfYaml
import requests
import json


class JiraTasks:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.data = {
            'fields': {
                "project":
                    {
                        "key": "JIRA_PROJECT"
                    },
                "issuetype": {
                    "name": "Внутреннее"
                },
                "customfield_30601": {
                    "id": "238234"
                },
                "customfield_30603": {
                    "id": "239840"
                },
                "labels": ["DQI",
                           "ККД"],
                "components": [
                    {
                        "id": "55933",
                    },
                ],
                "reporter": {
                    "name": "TEST"
                },
                "assignee": {
                    "name": "USER"
                },
                "customfield_30598": [{
                    "value": "Да",
                    "id": "214255"}]
            }
        }
        self.auth = (ConfYaml.config['jira']['auth']['login'], ConfYaml.config['jira']['auth']['password'])
        self.url = ConfYaml.config['jira']['url']

    def create_task(self, form_data):
        self.data['fields']['summary'] = "Контроль №" + form_data['Код']
        self.data['fields']['description'] = (
                'Название контроля: ' + form_data['Название контроля'] + '\n' +
                'Алгоритм проверки в бизнес-терминах: ' + form_data['Алгоритм проверки в бизнес-терминах'] + '\n' +
                'Условие отбора данных для проверки: ' + form_data['Условие отбора данных для проверки'] + '\n' +
                'Алгоритм проверки в технических терминах (опционально): ' + form_data.get('Алгоритм проверки в технических терминах (опционально)', '-') + '\n' +
                'Описание контроля: ' + form_data['Описание контроля'] + '\n' +
                'Действия офицера при ошибках: ' + form_data['Действия офицера при ошибках'] + '\n'
        )
        self.data['fields']["customfield_30604"] = form_data['Объект контроля']
        response = requests.post(self.url, verify=False, json=self.data, headers=self.headers, auth=self.auth)

        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            return None

    def update_task(self, key, form_data):
        url = self.url + str(key)
        response = requests.get(url, verify=False, headers=self.headers, auth=self.auth)
        getData = json.loads(response.text)
        summary = "Контроль №" + form_data['Код']
        description = ('Название контроля: ' + form_data['Название контроля'] + '\n' +
                       'Алгоритм проверки в бизнес-терминах: ' +
                       form_data['Алгоритм проверки в бизнес-терминах'] + '\n' +
                       'Условие отбора данных для проверки: ' + form_data['Условие отбора данных для проверки'] + '\n' +
                       'Алгоритм проверки в технических терминах (опционально): ' +
                       form_data.get('Алгоритм проверки в технических терминах (опционально)', '-') + '\n' +
                       'Описание контроля: ' + form_data['Описание контроля'] + '\n' +
                       'Действия офицера при ошибках: ' + form_data['Действия офицера при ошибках'] + '\n')
        customfield_30604 = form_data['Объект контроля']

        data = {'fields': {}}
        if getData['fields']['summary'] != summary:
            data['fields']['summary'] = summary
        if getData['fields']['description'] != description:
            data['fields']['description'] = description
        if getData['fields']['customfield_30604'] != customfield_30604:
            data['fields']['customfield_30604'] = form_data['Объект контроля']

        response = requests.put(url, verify=False, json=data, headers=self.headers, auth=self.auth)
        return response

    def get_task(self, key):
        url = self.url + str(key)
        response = requests.get(url, verify=False, headers=self.headers, auth=self.auth)

        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            return None
