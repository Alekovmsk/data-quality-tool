from airflow.models import BaseOperator
import datetime
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import pandas as pd
from pandasql import sqldf
from sqlalchemy import create_engine
from airflow.utils.email import send_email
from .EmailClass import EmailBody


class DqControl(BaseOperator):
    def __init__(self, sql, source, dqi, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sql = sql
        self.source = source
        self.dqi = dqi

    def execute(self, context):
        start_time = datetime.now()
        st = [start_time]
        st = pd.DataFrame(st, columns=['start_time'])
        dest = PostgresHook(postgres_conn_id='SSDQ_POSTGRES')
        dest_conn = dest.get_conn()
        src_conn = self.source
        engine_dest = create_engine(dest.get_uri())

        res = pd.read_sql(self.sql, self.source)
        wf_id = pd.read_sql(f"""SELECT nextval('"SSDQ".dq_detailjournal_web__pm_workflow_run_id_seq') as PM_WORKFLOW_RUN_ID, {self.dqi} as "DQ_CONTROL_UK" """, dest_conn)
        r = res.merge(wf_id, how='cross')
        r.columns = r.columns.str.lower()
        r.to_sql(name='dq_detailjournal_web', schema='SSDQ', con=engine_dest, if_exists='append', index=False)
        end_time = datetime.now()
        et = [end_time]
        et = pd.DataFrame(et, columns=['end_time'])
        agg = sqldf("""select wf_id.dq_control_uk, wf_id.pm_workflow_run_id, ifnull(t.mistake_count,0) as mistake_count, st.start_time, et.end_time, et.end_time as report_date
        from wf_id
        left join (select count(*) as mistake_count from res) t on 1=1
        left join st on 1=1
        left join et on 1=1""", locals())
        agg.columns = agg.columns.str.lower()
        agg.to_sql(name='dq_detail_agg', schema='SSDQ', con=engine_dest, if_exists='append', index=False)

        if res.shape[0] > 0:
            mail_content = EmailBody(self.dqi)
            recipients = pd.read_sql(f"""select distinct duh.email
            from "SSDQ".dq_alerting_hdim dah
            join "SSDQ".dq_user_hdim duh 
            on dah.user_uk = duh.uk
            and duh.deleted_flag != 'Y'
            and duh.validto = date'5999-12-31'
            where dq_request_uk = {str(self.dqi)}""", dest_conn)
            recipient_emails = []
            for cur in recipients:
                recipient_emails.append(cur[0])

            send_email(recipient_emails, mail_content.subject, mail_content.html_content)
    

class DqControlCrdb(BaseOperator):
    def __init__(self, sql, src_info, dqi, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sql = sql
        self.src_info = src_info
        self.dqi = dqi

    def execute(self, context):
        start_time = datetime.now()
        st = [start_time]
        st = pd.DataFrame(st, columns=['start_time'])
        dest = PostgresHook(postgres_conn_id='SSDQ_POSTGRES')
        dest_conn = dest.get_conn()
        engine_dest = create_engine(dest.get_uri())

        src_res = {}

        for ind in range(len(self.src_info)):
            hook = PostgresHook(postgres_conn_id=self.src_info[ind]['source']).get_conn()
            locals()[self.src_info[ind]['src_name']] = pd.read_sql(self.src_info[ind]['sql'], hook)

        res = sqldf(self.sql, locals())
        wf_id = pd.read_sql(f"""SELECT nextval('"SSDQ".dq_detailjournal_web__pm_workflow_run_id_seq') as PM_WORKFLOW_RUN_ID, {self.dqi} as "DQ_CONTROL_UK" """, dest_conn)
        r = res.merge(wf_id, how='cross')
        r.columns = r.columns.str.lower()
        r.to_sql(name='dq_detailjournal_web', schema='SSDQ', con=engine_dest, if_exists='append', index=False)
        end_time = datetime.now()
        et = [end_time]
        et = pd.DataFrame(et, columns=['end_time'])
        agg = sqldf("""select wf_id.dq_control_uk, wf_id.pm_workflow_run_id, ifnull(t.mistake_count,0) as mistake_count, st.start_time, et.end_time, et.end_time as report_date
        from wf_id
        left join (select count(*) as mistake_count from res) t on 1=1
        left join st on 1=1
        left join et on 1=1""", locals())
        agg.columns = agg.columns.str.lower()
        agg.to_sql(name='dq_detail_agg', schema='SSDQ', con=engine_dest, if_exists='append', index=False)

        if res.shape[0] > 0:
            mail_content = EmailBody(self.dqi)
            recipients = pd.read_sql(f"""select distinct duh.email
            from "SSDQ".dq_alerting_hdim dah
            join "SSDQ".dq_user_hdim duh 
            on dah.user_uk = duh.uk
            and duh.deleted_flag != 'Y'
            and duh.validto = date'5999-12-31'
            where dq_request_uk = {str(self.dqi)}""", dest_conn)
            recipient_emails = []
            for cur in recipients:
                recipient_emails.append(cur[0])

            send_email(recipient_emails, mail_content.subject, mail_content.html_content)
