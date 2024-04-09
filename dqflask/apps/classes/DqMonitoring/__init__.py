from flask import render_template, request
from ..database import DqConnection
from ..models import dq_monitoring_view
from ..components.dq_status import DqStatus
from ..Logger.LogEvent import LogEvent


class DqMonitoring(DqStatus):
    dq_db_connection = DqConnection('dqServer')

    def __init__(self, flt, dqps_session=None, attr_list=None, filter_status=None):
        """
        :param flt: filter with control status from endpoint
        """
        self.flt = flt
        self.dqps_session = dqps_session
        self.attr_list = attr_list
        self.filter_status = filter_status

    def render(self, login):
        """
        :return: rendering template with controls status
        """
        log = LogEvent()
        log.log_get(login, 'dq_monitoring')
        return render_template('home/dq_monitoring.html', flt=self.dq_status[self.flt],
                               name=self.dq_status_desc[self.flt])

    def get_report(self, is_admin: bool, user_id: int | str | None, teams: list | None):
        """
        Get dq controls info from database.
        Called by ajax in DataTable (bootstrap)
        :return: json response to ajax
        """
        self.dqps_session = self.dq_db_connection.session_dq
        # attributes of dq_monitoring_view
        self.attr_list = [attr for attr in dq_monitoring_view.__dict__ if not attr.startswith("_")]
        if is_admin:
            self.filter_status = '1=1' if self.flt == 'all' else 'dq_status_uk = ' + self.dq_status[self.flt]
        else:
            filter_st = '1=1' if self.flt == 'all' else 'dq_status_uk = ' + self.dq_status[self.flt]
            if teams is None:
                access_flt = f""" and (officer_uk = {user_id}::numeric)"""
            else:
                access_flt = f""" and (officer_uk = {user_id}::numeric or uk in (
                    select control_id from "SSDQ".dq_control2team_sdim where team_id in ({', '.join(map(str, teams))})
                ))"""
            self.filter_status = filter_st + access_flt

        draw = request.form['draw']
        # filtering by entered string from UI
        search_value = request.form['search[value]']
        filter_str = self.get_filter_str(search_value)

        total_records = self.get_total_records()
        total_record_filtered = self.get_total_records(filter_str) if search_value != '' else total_records
        data = self.get_dataset(filter_str)

        self.dqps_session.close()

        response = {
            'draw': draw,
            'iTotalRecords': total_records,
            'iTotalDisplayRecords': total_record_filtered,
            'aaData': data,
        }
        return response

    def get_filter_str(self, search_value):
        """
        Generate filter string for sql
        :param search_value: search value from UI (DataTable)
        :return: filter string
        """
        if search_value != '':
            search_value = f'%%{search_value}%%'

            search = f"""::varchar like '{search_value}' OR """.join(map(str, self.attr_list))
            search = f"""and ({search}::varchar like '{search_value}')"""
        else:
            search = ''

        return search

    def get_total_records(self, flt=''):
        """
        Get count of all rows from "SSDQ".dq_monitoring_view
        :param flt: entered filter string from UI including status
        :return: count rows
        """
        cnt = self.dqps_session.execute(f'select count(*) as cnt from "SSDQ".dq_monitoring_view '
                                        f'where {self.filter_status} {flt}').one()

        return cnt['cnt']

    def get_dataset(self, flt=''):
        """
        Get sql response from database.
        In the end sql response converts to json.
        :param flt:
        :return:
        """
        row = int(request.form['start'])
        rowperpage = int(request.form['length'])

        order_id = int(request.form['order[0][column]']) + 1
        order_dir = request.form['order[0][dir]']
        order = f'{str(order_id)} {order_dir}'

        dataset = self.dqps_session.execute(f'select * from "SSDQ".dq_monitoring_view '
                                            f'where {self.filter_status} {flt} order by {order} '
                                            f'limit {rowperpage} offset {row}').fetchall()
        data = []
        for row in dataset:
            krow = {}
            for key in self.attr_list:
                krow[key] = row[key]
            data.append(krow)

        return data

    def response(self, login, method, **access_matrix):
        """
        Return html template or sql response according request method
        :param login: authorized user
        :param method: POST (ajax) or GET
        """
        if method == 'POST':
            return self.get_report(**access_matrix)
        else:
            return self.render(login)
