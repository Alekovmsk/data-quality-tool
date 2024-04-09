from flask import render_template
from ..models import dq_object_hdim
from datetime import datetime
from ..Logger.LogEvent import LogEvent
from . import AdminPanel


class AdminObjects(AdminPanel):
    def __init__(self, login, uk=None):
        self.login = login
        self.uk = uk
        self.log = LogEvent()

    def response(self):
        self.log.log_get(self.login, '/adm-objects')
        if self.uk is not None:
            object_n = dq_object_hdim.query.filter(dq_object_hdim.validto == '5999-12-31',
                                                   dq_object_hdim.uk == self.uk).first()
            return render_template('home/adm-change-object.html', object_n=object_n)
        else:
            return render_template('home/adm-objects.html')

    def add_object(self):
        parameters = {
            'obj': dq_object_hdim,
            'params': ['base_name', 'schema', 'table_name', 'description'],
            'seq_name': 'dq_object_hdim_seq',
            'seq_schema': 'SSDQ',
            'seq_id': 'uk'
        }
        self.uk = self.add_entity(**parameters)
        if self.uk == -1:
            response = {'message': 'Объект с введенным наименованием уже существует!'}
            return response, 200
        else:
            self.log.log_post(self.login, f'has created object', self.uk)
            return '', 204

    def update_object(self):
        parameters = {
            'obj': dq_object_hdim,
            'params': {
                'validto': datetime.now()
            },
            'obj_filter': {
                dq_object_hdim.uk: self.uk,
                dq_object_hdim.validto: '5999-12-31'
            }
        }
        self.update_entity(**parameters)

        parameters = {
            'obj': dq_object_hdim,
            'params': ['uk', 'base_name', 'schema', 'table_name', 'description']
        }
        self.add_entity(**parameters)
        self.log.log_post(self.login, f'has updated object', self.uk)
        return '', 204

    def delete_restore_object(self, restore=False):
        parameters = {
            'obj': dq_object_hdim,
            'obj_filter': {
                dq_object_hdim.uk: self.uk
            },
            'restore': restore
        }
        self.delete_restore_entity(**parameters)
        self.log.log_post(self.login, f"has {'restored' if restore else 'removed'} object", self.uk)
        return '', 204
