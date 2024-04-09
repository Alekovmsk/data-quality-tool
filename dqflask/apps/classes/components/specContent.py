from ..models import dq_object_hdim, dq_user_hdim, dq_owner_sdim, dq_error_type_sdim, \
    dq_quality_type_sdim, dq_systems_sdim, dq_segment_sdim, dq_status_lov, dq_bireport_department_lov, \
    dq_ftp_path_ldim, components_t, customer_depts_t, dq_source_hdim, view_specification_change, \
    view_specification_versions, dq_sql_detail_ldim, dq_alerting_hdim, dq_dag_crossdb_hdim
from ..AdminPanel.AdminModels import dq_control2team_sdim, dq_teams_sdim
from ..database import DqConnection
from ..cronParse import from_cron
from flask import render_template


class SpecContent:
    def __init__(self):
        self.dq_connection = DqConnection('dqServer')
        self.dqps_session = self.dq_connection.session_dq
        self.sources = dq_source_hdim.query.filter(dq_source_hdim.validto == '5999-12-31',
                                                   dq_source_hdim.deleted_flag != 'Y').all()
        self.cdts = customer_depts_t.query.filter(customer_depts_t.disabled != 'Y').all()
        self.comps_t = components_t.query.filter(components_t.archived != 'Y', components_t.project == 'BIRM').all()
        self.ftps = dq_ftp_path_ldim.query.filter().all()
        self.deps = dq_bireport_department_lov.query.filter().all()
        self.statuses = dq_status_lov.query.filter().all()
        self.segments = dq_segment_sdim.query.all()
        self.systems = dq_systems_sdim.query.filter().all()
        self.qts = dq_quality_type_sdim.query.filter().all()
        self.errors = dq_error_type_sdim.query.filter().all()
        self.owners = dq_owner_sdim.query.filter().all()
        self.minutes, self.hours, self.days_in_month = [], [], []
        for x in range(60):
            self.minutes.append(str(x).zfill(2))
        for x in range(24):
            self.hours.append(str(x).zfill(2))
        for x in range(1, 32):
            self.days_in_month.append(str(x).zfill(2))
        self.dqps_session.close()

    def render(self):
        return render_template('home/create-spec.html', owners=self.owners, errors=self.errors, qts=self.qts,
                               systems=self.systems, segments=self.segments, statuses=self.statuses, deps=self.deps,
                               ftps=self.ftps, cdts=self.cdts, comps_t=self.comps_t, sources=self.sources,
                               minutes=self.minutes, hours=self.hours, days_in_month=self.days_in_month)


class ChangeSpecContent(SpecContent):
    def __init__(self, uk, ver='V31-12-5999 00:00:00'):
        super().__init__()
        self.spec = view_specification_change.query.filter(view_specification_change.DQI_ID == uk,
                                                           view_specification_change.ver == ver).all()[0]
        self.spec_versions = view_specification_versions.query.filter(view_specification_versions.uk == uk).all()
        self.det_sql = dq_sql_detail_ldim.query.filter(dq_sql_detail_ldim.dq_request_uk == uk,
                                                       dq_sql_detail_ldim.validto == '5999-12-31').first()
        self.sc = from_cron(self.spec.cron)
        if self.spec.cor_date is not None:
            self.datef = f"{str(self.spec.cor_date.month)}-{str(self.spec.cor_date.day)}-" \
                         f"{str(self.spec.cor_date.year)}"
        else:
            self.datef = None
        self.alerting = dq_alerting_hdim.query.filter(dq_alerting_hdim.dq_request_uk == uk,
                                                      dq_alerting_hdim.validto == '5999-12-31',
                                                      dq_alerting_hdim.deleted_flag != 'Y').all()
        self.request_uk = uk

        if self.spec.crossdb_flag == 'Y':
            self.cdb_info = dq_dag_crossdb_hdim.query.filter(dq_dag_crossdb_hdim.dq_request_uk == uk,
                                                             dq_dag_crossdb_hdim.validto == '5999-12-31',
                                                             dq_dag_crossdb_hdim.deleted_flag != 'Y',
                                                             dq_dag_crossdb_hdim.main_sql == 'N').all()
            self.main_sql = dq_dag_crossdb_hdim.query.filter(dq_dag_crossdb_hdim.dq_request_uk == uk,
                                                             dq_dag_crossdb_hdim.validto == '5999-12-31',
                                                             dq_dag_crossdb_hdim.deleted_flag != 'Y',
                                                             dq_dag_crossdb_hdim.main_sql == 'Y').all()[0]
        else:
            self.cdb_info = []
            self.main_sql = None

        self.object = dq_object_hdim.query\
            .filter(dq_object_hdim.deleted_flag != 'Y',
                    dq_object_hdim.validto == '5999-12-31',
                    dq_object_hdim.uk == self.spec.dq_object_uk).first()

        officers_list = [self.spec.officer_uk, self.spec.steward_uk]
        for cur in self.alerting:
            officers_list.append(cur.user_uk)
        self.officers = dq_user_hdim.query\
            .filter(dq_user_hdim.deleted_flag != 'Y',
                    dq_user_hdim.validto == '5999-12-31',
                    dq_user_hdim.uk.in_(officers_list))\
            .all()

        control2teams = dq_control2team_sdim.query\
            .filter(dq_control2team_sdim.control_id == self.request_uk).all()

        teams_list = []
        for cur in control2teams:
            teams_list.append(cur.team_id)

        self.teams = dq_teams_sdim.query\
            .filter(dq_teams_sdim.deleted_flag != 'Y',
                    dq_teams_sdim.id.in_(teams_list)).all()

        self.dqps_session.close()

    def render_change(self):
        return render_template('home/change-spec.html', object=self.object, officers=self.officers,
                               owners=self.owners, errors=self.errors, qts=self.qts, systems=self.systems,
                               segments=self.segments, statuses=self.statuses, deps=self.deps, ftps=self.ftps,
                               cdts=self.cdts, comps_t=self.comps_t, sources=self.sources,
                               spec=self.spec, datef=self.datef, sid=self.request_uk, s_ver=self.spec_versions,
                               hours=self.hours, minutes=self.minutes, sc=self.sc, det_sql=self.det_sql,
                               days_in_month=self.days_in_month, alerting=self.alerting, cdb_info=self.cdb_info,
                               main_sql=self.main_sql, src_count=len(self.cdb_info), teams=self.teams)
