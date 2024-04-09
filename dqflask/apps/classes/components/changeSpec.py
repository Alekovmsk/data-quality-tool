from ..models import dq_request_hdim, dq_spec_hdim, dq_control_param_hdim, dq_dag_hdim, dq_sql_detail_ldim, \
    dq_alerting_hdim, dq_dag_crossdb_hdim
from ..AdminPanel.AdminModels import dq_control2team_sdim
from .createSpec import CreateSpec
from datetime import datetime, timedelta
from sqlalchemy import update, insert, delete
from flask import request
from ..Logger.LogEvent import LogEvent
from .specContent import ChangeSpecContent


class ChangeSpec(CreateSpec):
    def __init__(self, login, name, uk, method):
        """
        Initialize Class with attributes of controls' specification.
        If method = POST then prepare variables for updating specification
        If method = GET then render page from ChangeSpecContent class
        Create connection to database
        :param login: login from run.py
        :param name:  name from run.py
        """
        super().__init__(login, name, method)

        self.method = method
        if method == 'POST':
            self.request_uk = uk
            self.current_date_plus = self.current_date + timedelta(seconds=1)
        else:
            version = request.args.get('ver') if request.args.get('ver') else 'V31-12-5999 00:00:00'
            self.content = ChangeSpecContent(uk, version)

        self.log = LogEvent()

    def response(self):
        if self.method == 'POST':
            return self.update()

        elif self.method == 'GET':
            if request.args.get('isCreated') == 'True':
                return self.created(self.user_login)
            else:
                return self.content.render_change()

    def update_spec(self):
        """
        Get changed entities from html form.
        Update changed entities in database
        """
        request_hdim = True if request.form.get('dq_request_hdim') == 'on' else False
        spec_hdim = True if request.form.get('dq_spec_hdim') == 'on' else False
        control_param_hdim = True if request.form.get('dq_control_param_hdim') == 'on' else False
        dag_hdim = True if request.form.get('dq_dag_hdim') == 'on' else False
        dag_crossdb_hdim = True if request.form.get('dq_dag_crossdb_hdim') == 'on' else False
        alerting_hdim = True if request.form.get('dq_alerting_hdim') == 'on' else False
        sql_detail_ldim = True if request.form.get('dq_sql_detail_ldim') == 'on' else False
        control2team_sdim = True if request.form.get('dq_control2team_sdim') == 'on' else False

        if request_hdim:
            stmt = update(dq_request_hdim).where(dq_request_hdim.uk == self.request_uk,
                                                 dq_request_hdim.validto == datetime.strptime(
                                                     '31.12.5999', '%d.%m.%Y'))\
                .values(validto=self.current_date)
            self.engine_dqps.execute(stmt)

            stmt = insert(dq_request_hdim).values(
                uk=self.request_uk,
                terms=self.control_name,
                validfrom=self.current_date,
                user_login=self.user_login,
                user_name=self.user_name
            )
            self.engine_dqps.execute(stmt)

        if spec_hdim:
            stmt = update(dq_spec_hdim).where(dq_spec_hdim.dq_request_uk == self.request_uk,
                                              dq_spec_hdim.validto == datetime.strptime(
                                                  '31.12.5999', '%d.%m.%Y')) \
                .values(validto=self.current_date)
            self.engine_dqps.execute(stmt)

            stmt = insert(dq_spec_hdim).values(
                dq_request_uk=self.request_uk,
                dqi_code=self.request_uk,
                segment_id=self.segment_id,
                ind_system_id=self.ind_system_id,
                data_system_id=self.data_system_id,
                quality_type_id=self.quality_type_id,
                c_terms=self.c_terms,
                alg_business=self.alg_business,
                data_layer=self.data_layer,
                criterius=self.criterius,
                boundrymax_min=self.boundrymax_min,
                boundrymed_max=self.boundrymed_max,
                boundrymed_min=self.boundrymed_min,
                boundrymin_max=self.boundrymin_max,
                alg_tech=self.alg_tech,
                schedule=self.schedule,
                error_type_id=self.error_type_id,
                met_owner1_id=self.met_owner1,
                cor_owner1_id=self.cor_owner1,
                cor_owner2_id=self.cor_owner2,
                cor_owner3_id=self.cor_owner3,
                cor_owner4_id=self.cor_owner4
            )
            self.engine_dqps.execute(stmt)

        if control_param_hdim:
            stmt = update(dq_control_param_hdim).where(dq_control_param_hdim.dq_request_uk == self.request_uk,
                                                       dq_control_param_hdim.validto == datetime.strptime(
                                                           '31.12.5999', '%d.%m.%Y')) \
                .values(validto=self.current_date)
            self.engine_dqps.execute(stmt)

            stmt = insert(dq_control_param_hdim).values(
                dq_request_uk=self.request_uk,
                control_name=self.control_name,
                control_description=self.control_description,
                control_init=self.control_init,
                client_dept_id=self.client_dept_id,
                release_number=self.release_number,
                cr_number=self.cr_number,
                cor_date=self.cor_date,
                move_date=self.move_date,
                delay=self.delay,
                mail_type=self.mail_type,
                ror_flag=self.ror_flag,
                mail_h_flag=self.mail_h_flag,
                auto_inc_flag=self.auto_inc_flag,
                officer_uk=self.officer_uk,
                officer_to_do=self.officer_to_do,
                dq_object_uk=self.dq_object_uk,
                wiki_link=self.wiki_link,
                dq_status_uk=self.dq_status_uk,
                dq_ftp_path_uk=self.dq_ftp_path_uk,
                customer_depts_t_id=self.customer_depts_t_id,
                components_t_id=self.components_t_id,
                validfrom=self.current_date,
                user_login=self.user_login,
                user_name=self.user_name,
                steward_uk=self.steward_uk,
                control_critical_flag=self.control_critical_flag
            )
            self.engine_dqps.execute(stmt)

        if sql_detail_ldim:
            stmt = update(dq_sql_detail_ldim).where(dq_sql_detail_ldim.dq_request_uk == self.request_uk,
                                                    dq_sql_detail_ldim.validto == datetime.strptime(
                                                        '31.12.5999', '%d.%m.%Y')) \
                .values(validto=self.current_date)
            self.engine_dqps.execute(stmt)

            stmt = insert(dq_sql_detail_ldim).values(
                dq_request_uk=self.request_uk,
                sql_query=self.detail_query,
                validfrom=self.current_date,
                user_login=self.user_login,
                user_name=self.user_name
            )
            self.engine_dqps.execute(stmt)

        if alerting_hdim:
            stmt = update(dq_alerting_hdim).where(dq_alerting_hdim.dq_request_uk == self.request_uk,
                                                  dq_alerting_hdim.validto == datetime.strptime(
                                                      '31.12.5999', '%d.%m.%Y')) \
                .values(validto=self.current_date)
            self.engine_dqps.execute(stmt)

            if self.alerting:
                for usr in self.alerting:
                    stmt = insert(dq_alerting_hdim).values(
                        dq_request_uk=self.request_uk,
                        user_uk=usr,
                        dq_mail_attachtype_uk=1,
                        validfrom=self.current_date
                    )
                    self.engine_dqps.execute(stmt)

        if control2team_sdim:
            stmt = delete(dq_control2team_sdim).where(dq_control2team_sdim.control_id == self.request_uk)
            self.engine_dqps.execute(stmt)

            if self.teams:
                for team in self.teams:
                    stmt = insert(dq_control2team_sdim).values(
                        control_id=self.request_uk,
                        team_id=team
                    )
                    self.engine_dqps.execute(stmt)

        if dag_crossdb_hdim or dag_hdim:
            stmt = update(dq_dag_crossdb_hdim).where(dq_dag_crossdb_hdim.dq_request_uk == self.request_uk,
                                                     dq_dag_crossdb_hdim.validto == datetime.strptime(
                                                        '31.12.5999', '%d.%m.%Y')) \
                .values(validto=self.current_date)
            self.engine_dqps.execute(stmt)

            stmt = update(dq_dag_hdim).where(dq_dag_hdim.dq_request_uk == self.request_uk,
                                             dq_dag_hdim.validto == datetime.strptime(
                                                 '31.12.5999', '%d.%m.%Y')) \
                .values(validto=self.current_date)
            self.engine_dqps.execute(stmt)

            if self.check_crossdb == 'Y':
                stmt = insert(dq_dag_hdim).values(
                    dq_request_uk=self.request_uk,
                    crossdb_flag='Y',
                    validfrom=self.current_date,
                    cron=self.schedule_cron
                )
                self.engine_dqps.execute(stmt)

                for ind in range(self.src_count):
                    stmt = insert(dq_dag_crossdb_hdim).values(
                        dq_request_uk=self.request_uk,
                        sql=self.sql_list[ind],
                        source=self.src_name_list[ind],
                        custom_source_name=self.custom_name_list[ind],
                        validfrom=self.current_date
                    )
                    self.engine_dqps.execute(stmt)

                stmt = insert(dq_dag_crossdb_hdim).values(
                    dq_request_uk=self.request_uk,
                    sql=self.main_sql,
                    main_sql='Y',
                    validfrom=self.current_date
                )
                self.engine_dqps.execute(stmt)

            else:
                stmt = insert(dq_dag_hdim).values(
                    dq_request_uk=self.request_uk,
                    sql=self.sql_query,
                    alg=self.alg,
                    cron=self.schedule_cron,
                    validfrom=self.current_date,
                    source=self.source
                )
                self.engine_dqps.execute(stmt)

        self.dqps_session.close()

    def update(self):
        self.request_form()
        self.update_spec()
        #self.deploy_dag()
        self.log.log_post(self.user_login, 'updated', f'specification {str(self.request_uk)}')

        return '', 204
