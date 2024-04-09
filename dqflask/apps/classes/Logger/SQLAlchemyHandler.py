import logging
import traceback
from ..models import Log
from ..database import DqConnection
from sqlalchemy.orm import Session


class SQLAlchemyHandler(logging.Handler):

    def emit(self, record):
        dq_conn = DqConnection('flaskDb')
        dq_session = Session(bind=dq_conn.engine_dq)

        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc()
        log = Log(
            logger=record.__dict__['name'],
            level=record.__dict__['levelname'],
            trace=trace,
            msg=record.__dict__['msg']
        )
        dq_session.add(log)
        dq_session.commit()