from ..database import DqConnection
from ..models import view_controls_count, view_controls_error, dq_control_param_hdim, view_all_controls_bydate
from ..AdminPanel.AdminModels import dq_control2team_sdim
from flask import render_template, jsonify, request
from ..Logger.LogEvent import LogEvent
from sqlalchemy import or_


class DqAnalytics:
    dq_db_connection = DqConnection('dqServer')

    def __init__(self):
        self.db_object = None
        self.ind = False
        obj_name = request.args.get('obj')
        if obj_name == 'view_all_controls_bydate':
            self.db_object = view_all_controls_bydate
            self.ind = True
        elif obj_name == 'view_controls_error':
            self.db_object = view_controls_error
            self.ind = True

    def response(self, login, method, **access_matrix):
        if method == 'POST':
            return self.get_db_data(**access_matrix)
        elif method == 'GET':
            return self.render(login, **access_matrix)

    @staticmethod
    def render(login, is_admin: bool, user_id: int | str | None, teams: list | None):
        log = LogEvent()
        if is_admin:
            dq_mon = view_controls_count.query.filter().first()
            exp_cnt = int(dq_mon.exp_cnt) if dq_mon is not None else 0
            cncl_cnt = int(dq_mon.cncl_cnt) if dq_mon is not None else 0
            act_cnt = int(dq_mon.act_cnt) if dq_mon is not None else 0
            all_cnt = int(dq_mon.all_cnt) if dq_mon is not None else 0
        else:
            if teams is None:
                dq_mon = dq_control_param_hdim.query\
                    .filter(dq_control_param_hdim.deleted_flag != 'Y',
                            dq_control_param_hdim.validto == '5999-12-31',
                            dq_control_param_hdim.officer_uk == user_id).all()
            else:
                controls = dq_control2team_sdim.query.filter(dq_control2team_sdim.team_id.in_(teams)).all()
                controls_list = [control.control_id for control in controls]
                dq_mon = dq_control_param_hdim.query\
                    .filter(dq_control_param_hdim.deleted_flag != 'Y',
                            dq_control_param_hdim.validto == '5999-12-31',
                            or_(dq_control_param_hdim.officer_uk == user_id,
                                dq_control_param_hdim.dq_request_uk.in_(controls_list))
                            ).all()
            exp_cnt, cncl_cnt, act_cnt, all_cnt = 0, 0, 0, 0
            for cur in dq_mon:
                exp_cnt += 1 if cur.dq_status_uk == 4 else 0
                cncl_cnt += 1 if cur.dq_status_uk == 5 else 0
                act_cnt += 1 if cur.dq_status_uk == 6 else 0
                all_cnt += 1

        log.log_get(login, 'dq_analytics')
        return render_template('home/dq_analytics.html', cnt=all_cnt, exp=exp_cnt, act=act_cnt, cncl=cncl_cnt)

    def get_db_data(self, is_admin: bool, user_id: int | str | None, teams: list | None):
        if is_admin:
            db_data = self.db_object.query.filter().all()
        else:
            if teams is None:
                db_data = self.db_object.query.filter(self.db_object.officer_uk == user_id).all()
            else:
                team_controls = dq_control2team_sdim.query.filter(dq_control2team_sdim.team_id.in_(teams)).all()
                team_controls_list = [control.control_id for control in team_controls]
                db_data = self.db_object.query.filter(or_(
                    self.db_object.officer_uk == user_id,
                    self.db_object.uk.in_(team_controls_list)
                )).all()

        attr_list = [attr for attr in self.db_object.__dict__ if not attr.startswith("_")]

        data = []
        for row in db_data:
            krow = {}
            for key in attr_list:
                krow[key] = row.__getattribute__(key)
            data.append(krow)

        response = {
            'aaData': data
        }

        self.dq_db_connection.session_dq.close()
        return jsonify(response)
