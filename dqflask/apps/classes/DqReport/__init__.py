from flask import render_template, jsonify, request
from ..database import DqConnection
from ..models import dq_detail_agg, dq_sql_detail_ldim
import pandas as pd
import re
import json


class Report:
    dq_db_connection = DqConnection('dqServer')

    def __init__(self, uk, wf_id=None):
        """
        Initialize a class instance with connection to database and get dq control's info from database.
        If wf_id is None then get last run's info.
        :param uk: dq control ID
        :param wf_id: workflow run ID
        """
        self.dqps_session = self.dq_db_connection.session_dq
        self.connection = self.dq_db_connection.engine_dq.raw_connection()

        self.uk = uk
        self.agg_report = dq_detail_agg.query.filter(dq_detail_agg.dq_control_uk == uk)\
            .order_by(dq_detail_agg.report_date.desc()).all()

        for i, row in enumerate(self.agg_report, 0):
            self.ind_wf = i if row.pm_workflow_run_id == str(wf_id) else 0

        if len(self.agg_report) > 0:
            self.__no_results = False
            self.max_wf_id = self.agg_report[0].pm_workflow_run_id
            self.current_wf_id = wf_id if wf_id is not None else self.max_wf_id
            sql_tab = dq_sql_detail_ldim.query.filter(dq_sql_detail_ldim.dq_request_uk == uk,
                                                      dq_sql_detail_ldim.validto == '5999-12-31').first()

            if sql_tab.sql_query.strip().upper().endswith('DQ_DETAILJOURNAL_WEB'):
                query = f'{sql_tab.sql_query.strip()} WHERE DQ_CONTROL_UK = {uk} '
            else:
                query = f'{sql_tab.sql_query.strip()} AND DQ_CONTROL_UK = {uk} '
            sql = re.sub("^\n|\r", ' ', query)
            self.max_rep_date = self.agg_report[0].report_date

            self.columns_name = pd.read_sql(sql + """ limit 1""", self.connection)
            self.cnt_col = len(self.columns_name.axes[1])
            self.column_list = self.columns_name.columns.values
            self.columns = ', '.join(map(str, self.column_list))

            self.current_mistake_count = self.agg_report[self.ind_wf].mistake_count
            self.current_date = self.agg_report[self.ind_wf].report_date
        else:
            self.__no_results = True

        self.dqps_session.close()

    def render(self, is_editing):
        """
        render template with instance's params
        :return: if there is no runs then render error page
        """
        if self.__no_results:
            return render_template('home/dq_report_err.html', dqi=self.uk, is_editing=is_editing)

        else:
            return render_template('home/dq_report.html', dqi=self.uk, agg_rep=self.agg_report,
                                   max_rep_date=self.max_rep_date, pm_workflow_run_id=self.max_wf_id,
                                   columns=self.columns, cnt_col=self.cnt_col,
                                   col=self.column_list, current_mistake_count=self.current_mistake_count,
                                   current_date=self.current_date, current_wf=self.current_wf_id, is_editing=is_editing)


class ReportAjax:
    """
    Class used to ajax query by changing workflow run id in UI
    """
    dq_db_connection = DqConnection('dqServer')

    def __init__(self, dqi, wf_id):
        """
        Initialize a class instance with connection to database and get dq control's info from database to render
        data-grid (DataTable from bootstrap)
        :param dqi: dq control ID
        :param wf_id: workflow run ID
        """
        self.connection = self.dq_db_connection.engine_dq.raw_connection()
        self.dqps_session = self.dq_db_connection.session_dq

        self.dqi = dqi
        self.wf_id = wf_id
        self.row = int(request.form['start'])
        self.rowperpage = int(request.form['length'])
        order_id = int(request.form['order[0][column]']) + 1
        order_dir = request.form['order[0][dir]']
        self.order = f'{str(order_id)} {order_dir}'

        sql_tab = dq_sql_detail_ldim.query.filter(dq_sql_detail_ldim.dq_request_uk == self.dqi,
                                                  dq_sql_detail_ldim.validto == '5999-12-31').first()

        if sql_tab.sql_query.strip().upper().endswith('DQ_DETAILJOURNAL_WEB'):
            query = f'{sql_tab.sql_query.strip()} WHERE DQ_CONTROL_UK = {self.dqi} ' \
                    f'AND pm_workflow_run_id = {self.wf_id}::varchar'
        else:
            query = f'{sql_tab.sql_query.strip()} AND DQ_CONTROL_UK = {self.dqi} ' \
                    f'AND pm_workflow_run_id = {self.wf_id}::varchar'
        self.sql = re.sub("^\n|\r", ' ', query)

    def get_total_records(self, flt=''):
        """
        Get count of all rows according selected workflow run id
        :param flt: entered filter string from UI
        :return:
        """
        if flt == '':
            rsallcount = self.dqps_session.execute(f'select count(*) as cnt from "SSDQ".dq_detailjournal_web '
                                                   f'where dq_control_uk = {self.dqi} '
                                                   f'and pm_workflow_run_id = {self.wf_id}::varchar').one()
        else:
            rsallcount = self.dqps_session.execute(f'select count(*) as cnt from ({self.sql}) t {flt}').one()

        return rsallcount['cnt']

    def get_dataset(self, flt=''):
        """
        get sql response from database
        :param flt:
        :return:
        """
        report = pd.read_sql(f'select * from ({self.sql}) t {flt} order by {self.order} '
                             f'limit {self.rowperpage} offset {self.row}', self.connection)
        return json.loads(report.to_json(orient='values', date_format='iso'))

    def get_report(self):
        """
        generate json with data for rendering data-grid
        :return: json with data for rendering data-grid
        """
        draw = request.form['draw']
        search_value = request.form['search[value]']
        columns = request.form['columns']
        column_list = columns.split(',')

        if search_value != '':
            search_value = f'%%{search_value}%%'
            flt = f"""::varchar like '{search_value}' OR""".join(map(str, column_list))
            flt = f"""where ({flt}::varchar like '{search_value}')"""
        else:
            flt = ''

        total_records = self.get_total_records()
        total_record_filtered = self.get_total_records(flt) if flt != '' else total_records

        data = self.get_dataset(flt)
        response = {
            'draw': draw,
            'iTotalRecords': total_records,
            'iTotalDisplayRecords': total_record_filtered,
            'aaData': data,
        }
        return jsonify(response)
