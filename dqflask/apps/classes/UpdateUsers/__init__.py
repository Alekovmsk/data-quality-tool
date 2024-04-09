from .models import dq_user_delta, dq_department_delta, UsersTable, DepartmentsTable
from ..user_model import Users
from ..database import DqConnection
from sqlalchemy.orm import Session
from .custom_src import get_users, get_departments
from ..conf import ConfYaml
from apscheduler.schedulers.background import BackgroundScheduler


class UsersInfo:

    def __init__(self):
        self.conn = DqConnection('dqServer')
        self.admin_conn = DqConnection('flaskDb')

    def set_schedule(self):
        scheduler = BackgroundScheduler()

        if ConfYaml.config['users']['load_users']:
            scheduler.add_job(func=self.update_users, trigger="cron", hour='23', minute='59')

        return scheduler

    def update_users(self):
        engine = self.conn.engine_dq.raw_connection()
        cur = engine.cursor()
        cur.execute("""truncate table "SSDQ".dq_department_delta;""")
        cur.execute("""truncate table "SSDQ".dq_user_delta;""")
        cur.close()
        engine.commit()
        engine.close()

        admin_engine = self.admin_conn.engine_dq.raw_connection()
        admin_cur = admin_engine.cursor()
        admin_cur.execute("""truncate table public."Users";""")
        admin_cur.close()
        admin_engine.commit()
        admin_engine.close()

        self.upload_delta()

        engine = self.conn.engine_dq.raw_connection()
        cur = engine.cursor()
        cur.execute("""CALL "SSDQ".update_users_proc();""")
        cur.close()
        engine.commit()
        engine.close()

    def upload_delta(self):
        dq_session = Session(bind=self.conn.engine_dq)
        admin_session = Session(bind=self.admin_conn.engine_dq)

        users = []
        admin_users = []
        deps = []

        # Default loading with parameters from config.yaml
        # deps_nfo = UsersTable.query.filter().all()
        # users_info = UsersTable.query.filter().all()

        # Custom loading
        deps_nfo = get_departments()

        for row in deps_nfo:
            deps.append(dq_department_delta(
                name=row['department']  # row.name  with standart loading
            ))

        dq_session.add_all(deps)

        # Custom loading
        users_info = get_users()

        for row in users_info:
            users.append(dq_user_delta(
                login=row['username'],  # row.username, with standart loading
                full_name=row['full_name'],  # row.full_name, with standart loading
                email=row['email'],  # row.email, with standart loading
                department=row['department']  # row.department with standart loading
            ))
            admin_users.append(Users(
                id=row['username'],
                email=row['email'],
                name=row['full_name'],
                login=row['username']
            ))

        dq_session.add_all(users)
        admin_session.add_all(admin_users)

        admin_session.commit()
        dq_session.commit()
