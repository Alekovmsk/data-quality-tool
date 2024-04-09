import datetime
from sqlalchemy import update
from ..database import DqConnection
from ..models import dq_request_hdim, dq_control_param_hdim, dq_spec_hdim, dq_dag_hdim, dq_alerting_hdim, \
    dq_sql_detail_ldim, dq_dag_crossdb_hdim
from ..dags import Dag


class DeleteSpec:
    @staticmethod
    def delete_spec(uk):
        dq_connection = DqConnection('dqServer')
        dqps_session = dq_connection.session_dq
        
        current_date = datetime.datetime.now()
        
        stmt = update(dq_request_hdim).where(dq_request_hdim.uk == uk,
                                             dq_request_hdim.validto == datetime.datetime.strptime(
                                                 '31.12.5999', '%d.%m.%Y')).values(validto=current_date,
                                                                                   deleted_flag='Y')
        dqps_session.execute(stmt)
        
        stmt = update(dq_spec_hdim).where(dq_spec_hdim.dq_request_uk == uk,
                                          dq_spec_hdim.validto == datetime.datetime.strptime(
                                              '31.12.5999', '%d.%m.%Y')).values(validto=current_date,
                                                                                deleted_flag='Y')
        dqps_session.execute(stmt)

        stmt = update(dq_control_param_hdim).where(dq_control_param_hdim.dq_request_uk == uk,
                                                   dq_control_param_hdim.validto == datetime.datetime.strptime(
                                                       '31.12.5999', '%d.%m.%Y')).values(validto=current_date,
                                                                                         deleted_flag='Y')
        dqps_session.execute(stmt)

        stmt = update(dq_dag_hdim).where(dq_dag_hdim.dq_request_uk == uk,
                                         dq_dag_hdim.validto == datetime.datetime.strptime(
                                             '31.12.5999', '%d.%m.%Y')).values(validto=current_date,
                                                                               deleted_flag='Y')
        dqps_session.execute(stmt)

        stmt = update(dq_dag_crossdb_hdim).where(dq_dag_crossdb_hdim.dq_request_uk == uk,
                                                 dq_dag_crossdb_hdim.validto == datetime.datetime.strptime(
                                                     '31.12.5999', '%d.%m.%Y')).values(validto=current_date,
                                                                                       deleted_flag='Y')
        dqps_session.execute(stmt)

        stmt = update(dq_sql_detail_ldim).where(dq_sql_detail_ldim.dq_request_uk == uk,
                                                dq_sql_detail_ldim.validto == datetime.datetime.strptime(
                                                    '31.12.5999', '%d.%m.%Y')).values(validto=current_date)
        dqps_session.execute(stmt)

        stmt = update(dq_alerting_hdim).where(dq_alerting_hdim.dq_request_uk == uk,
                                              dq_alerting_hdim.validto == datetime.datetime.strptime(
                                                  '31.12.5999', '%d.%m.%Y')).values(validto=current_date,
                                                                                    deleted_flag='Y')
        dqps_session.execute(stmt)

        dqps_session.close()

        #dag = Dag(uk)
        #dag.remove_dag()

        return '', 204
        