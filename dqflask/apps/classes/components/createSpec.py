import datetime
import time
from sqlalchemy import Sequence, insert
from ..models import dq_request_hdim, dq_sql_detail_ldim, dq_spec_hdim, dq_control_param_hdim, \
    dq_dag_hdim, dq_alerting_hdim, dq_dag_crossdb_hdim
from ..AdminPanel.AdminModels import dq_control2team_sdim
from flask import render_template, request
from ..cronParse import to_cron
from ..spec import Spec
from ..database import DqConnection
from ..dags import Dag
from .specContent import SpecContent
from ..Logger.LogEvent import LogEvent


class CreateSpec(Spec):
    def __init__(self, login, name, method):
        """
        Initialize Class with attributes of controls' specification.
        If method = POST then prepare variables for creating specification
        If method = GET then render page from ChangeSpecContent class
        Create connection to database
        :param login: login from run.py
        :param name:  name from run.py
        """
        super().__init__(login, name)

        self.method = method
        if method == 'POST':
            self.current_date = datetime.datetime.now()
            self.dq_connection = DqConnection('dqServer')
            self.engine_dqps = self.dq_connection.engine_dq
            self.dqps_session = self.dq_connection.session_dq

        else:
            self.content = SpecContent()

        self.log = LogEvent()

    def response(self):
        if self.method == 'POST':
            return self.create()

        elif self.method == 'GET':
            if request.args.get('isCreated') == 'True':
                return self.created(self.user_login)
            else:
                return self.content.render()

    def request_form(self):
        """
        request attributes from html form
        """
        # First page
        self.segment_id = request.form.get('segment_id')
        self.ind_system_id = int(request.form.get('ind_system'))
        self.data_system_id = int(request.form.get('data_system'))
        self.quality_type_id = int(request.form.get('quality_type_name'))
        self.c_terms = request.form['c_terms']
        self.alg_business = request.form['alg_business']
        self.data_layer = request.form['data_layer']
        self.criterius = request.form['criterius']
        self.boundrymin_max = float(request.form['boundrymin_max'])
        self.boundrymed_min = float(request.form['boundrymed_min'])
        self.boundrymed_max = float(request.form['boundrymed_max'])
        self.boundrymax_min = float(request.form['boundrymax_min'])
        self.alg_tech = request.form['alg_tech']
        self.schedule = request.form['schedule']
        self.error_type_id = int(request.form.get('error_type'))
        self.met_owner1 = int(request.form.get('met_owner1'))
        self.cor_owner1 = int(request.form.get('cor_owner1'))
        self.cor_owner2 = int(request.form.get('cor_owner2'))
        self.cor_owner3 = int(request.form.get('cor_owner3'))
        self.cor_owner4 = int(request.form.get('cor_owner4'))

        # Second page
        self.control_name = request.form.get('control_name')
        self.control_description = request.form.get('control_description')
        self.control_init = request.form.get('control_init')
        self.client_dept_id = request.form.get('client_dept_id')
        self.release_number = request.form.get('release_number')
        self.cr_number = request.form.get('cr_number')
        cd = request.form.get('cor_date')
        self.cor_date = None if cd == '' else datetime.datetime.strptime(cd, '%m/%d/%Y').date()
        self.move_date = request.form.get('move_date')
        self.delay = request.form.get('delay')
        self.mail_type = request.form.get('mail_type')
        self.ror_flag = 'Y' if request.form.get('ror_flag') == 'on' else 'N'
        self.mail_h_flag = 'Y' if request.form.get('mail_h_flag') == 'on' else 'N'
        self.auto_inc_flag = 'Y' if request.form.get('auto_inc_flag') == 'on' else 'N'
        self.officer_uk = request.form.get('officer_uk')
        self.steward_uk = request.form.get('steward_uk')
        self.officer_to_do = request.form.get('officer_to_do')
        self.dq_object_uk = int(request.form.get('dq_object_uk'))
        self.wiki_link = request.form.get('wiki_link')
        self.dq_status_uk = int(request.form.get('dq_status_uk'))
        self.dq_ftp_path_uk = int(request.form.get('dq_ftp_path_uk'))
        self.customer_depts_t_id = request.form.get('customer_depts_t_id')
        self.control_type = request.form.get('control_type')
        self.components_t_id = request.form.get('components_t_id')

        # Third page
        cron_schedule = to_cron(request.form.get('select_sch'), request.form.get('minute_select'),
                                request.form.get('hour_select'), request.form.get('time_hour_day_select'),
                                request.form.get('time_minute_day_select'),
                                request.form.get('time_hour_week_select'),
                                request.form.get('time_minute_week_select'),
                                request.form.get('day_of_week_select'),
                                request.form.get('time_minute_month_select'),
                                request.form.get('time_hour_month_select'),
                                request.form.get('day_of_month_select')
                                )

        self.schedule_cron = f"'{cron_schedule}'" if cron_schedule is not None else 'None'
        self.alg = request.form.get('alg')
        self.detail_query = request.form.get('detail_query')
        self.control_critical_flag = 'Y' if request.form.get('control_critical_flag') == 'on' else 'N'
        self.alerting = request.form.getlist('alerting')
        self.teams = request.form.getlist('teams')

        self.check_crossdb = 'Y' if request.form.get('check_crossdb') == 'on' else 'N'

        if self.check_crossdb == 'Y':
            self.src_count = int(request.form.get('srcCount'))

            for cur in range(self.src_count):
                self.src_name_list.append(request.form.get(f'src{cur+1}'))
                self.custom_name_list.append(request.form.get(f'custom_name{cur + 1}'))
                self.sql_list.append(request.form.get(f'src_query{cur + 1}'))

            self.main_sql = request.form.get('main_query')

        else:
            self.sql_query = request.form.get('sql_query')
            self.source = request.form.get('source')

        return True

    def insert_spec(self):
        """
            insert new data-quality control into DataBase
        """
        seq = Sequence('dq_request_hdim_seq', schema="SSDQ")
        self.request_uk = self.engine_dqps.execute(seq)

        stmt = insert(dq_request_hdim).values(
            uk=self.request_uk,
            terms=self.control_name,
            validfrom=self.current_date,
            user_login=self.user_login,
            user_name=self.user_name
        )
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

        stmt = insert(dq_sql_detail_ldim).values(
            dq_request_uk=self.request_uk,
            sql_query=self.detail_query,
            validfrom=self.current_date,
            user_login=self.user_login,
            user_name=self.user_name
        )
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

        if self.teams:
            for team in self.teams:
                stmt = insert(dq_control2team_sdim).values(
                    control_id=self.request_uk,
                    team_id=team
                )
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

    def deploy_dag(self):
        """
        deploying dag into airflow
        """
        dag = Dag(
            dqi=str(self.request_uk),
            source=self.source if self.check_crossdb != 'Y' else None,
            sql=self.sql_query if self.check_crossdb != 'Y' else self.main_sql,
            cron=self.schedule_cron,
            crossdb=True if self.check_crossdb == 'Y' else False,
            src_cnt=self.src_count,
            sql_list=self.sql_list,
            source_list=self.src_name_list,
            custom_name_list=self.custom_name_list
        )

        return dag.deploy_dag()

    def create(self):
        self.request_form()
        self.insert_spec()
        #self.deploy_dag()
        self.log.log_post(self.user_login, 'created', f'specification {str(self.request_uk)}')
        return '', 204


    @staticmethod
    def created(login):
        """
        Static method to return successful message to create-spec page
        """
        time.sleep(8)  # wait until created
        uk = dq_request_hdim.query.filter(dq_request_hdim.user_login == login) \
                            .order_by(dq_request_hdim.validfrom.desc()).first().uk
        return render_template('home/create-done.html', uk=uk)
