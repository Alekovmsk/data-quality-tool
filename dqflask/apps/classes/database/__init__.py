from sqlalchemy import create_engine, MetaData
import urllib.parse
from ..conf import DqConfigDB
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DqConnection(DqConfigDB):
    def __init__(self, server_name):
        super().__init__(server_name)
        self.conn_string = f'{self.type}://' \
                           f'{self.user}:' \
                           f'{urllib.parse.quote_plus(self.password)}@' \
                           f'{self.host}:{self.port}/{self.db}'
        self.engine_dq = create_engine(self.conn_string, convert_unicode=True)
        self.con_dq = self.engine_dq.connect()
        self.metadata_dq = MetaData(bind=self.engine_dq)
        # self.session_dq = Session(bind=self.engine_dq)

        self.session_dq = scoped_session(
            sessionmaker(
                autocommit=True,
                autoflush=True,
                bind=self.engine_dq
            )
        )
        self.Base_dqps = declarative_base()
        self.Base_dqps.query = self.session_dq.query_property()

    @staticmethod
    def init_db():
        from .. import models
