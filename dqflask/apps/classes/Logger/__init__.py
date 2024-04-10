import re
from datetime import datetime, timedelta
from ..models import Log
from ..database import DqConnection
from ..conf import ConfYaml
from sqlalchemy.orm import Session
from apscheduler.schedulers.background import BackgroundScheduler


class LogLoad:
    def __init__(self):
        dq_conn = DqConnection('flaskDb')
        self.dq_session = Session(bind=dq_conn.engine_dq)

    def set_schedule(self):
        scheduler = BackgroundScheduler()

        if ConfYaml.config['logging']['upload_schedule']['upload_midnight']:
            scheduler.add_job(func=self.insert_logs, trigger="cron", hour='23', minute='59')

        if ConfYaml.config['logging']['upload_schedule']['upload_frequency'] != 0:
            scheduler.add_job(func=self.insert_logs, trigger="interval",
                              seconds=ConfYaml.config['logging']['upload_schedule']['upload_frequency'])

        scheduler.add_job(func=self.delete_logs, trigger="cron", hour='23', minute='59')

        return scheduler

    def insert_logs(self):
        logs = self.parse_logs()
        self.dq_session.add_all(logs)
        self.dq_session.commit()

    def delete_logs(self):
        storage_depth = datetime.now() - timedelta(days=365*int(Conf-Yaml.config['logging']['storage_depth']))
        self.dq_session.query(Log).filter(Log.created_at < storage_depth).delete()

    @staticmethod
    def parse_logs():
        last_row: Log | None = Log.query.filter().order_by(Log.created_at.desc()).first()
        last_date = last_row.created_at if last_row is not None else datetime(2000, 1, 1, 0, 0, 0)
        logs = []

        f = open(ConfYaml.logging_conf['handlers']['file']['filename'], 'r')
        for row in f:
            search = re.search('\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d*\]', row)
            date = datetime.strptime(search.group(0), '[%Y-%m-%d %H:%M:%S,%f]') if search is not None else None

            if date is None or date <= last_date:
                continue

            search = re.search(r'\bgpbu\d+ \b', row)
            login = search.group(0).strip() if search is not None else None

            search = re.search('\] \w+\:', row)
            log_level = search.group(0)[2:-1] if search is not None else None

            search = re.search('\] \w+\:.*', row)
            msg = search.group(0)[8:] if search is not None else None

            logs.append(Log(
                logger='root',
                level=log_level,
                login=login,
                msg=msg,
                created_at=date
            ))

        return logs
