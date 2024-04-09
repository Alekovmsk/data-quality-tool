from ..database import DqConnection
from flask import request
from sqlalchemy import Sequence, insert, update, delete, exc


class AdminPanel:
    @staticmethod
    def add_entity(obj, params: list | None, seq_name=None, seq_schema=None, seq_id=None, **init_values):
        session = DqConnection('dqServer').session_dq

        values = {}

        if seq_name is not None:
            seq = Sequence(seq_name, schema=seq_schema)
            uk = session.execute(seq)
            values[seq_id] = uk
        else:
            uk = None

        if params is None:
            stmt = insert(obj).values(**init_values)
        else:
            for p in params:
                values[p] = request.form.get(p)
            stmt = insert(obj).values(**values)

        try:
            session.execute(stmt)
        except exc.IntegrityError as er:
            print(er)
            uk = -1
        finally:
            session.close()

        return uk

    @staticmethod
    def update_entity(obj, params: list | dict, obj_filter: dict):
        session = DqConnection('dqServer').session_dq

        filter_list = []
        for key in obj_filter:
            filter_list.append(key == obj_filter[key])

        if isinstance(params, list):
            values = {}
            for p in params:
                values[p] = request.form.get(p)
            stmt = update(obj).where(*filter_list).values(**values)
        else:
            stmt = update(obj).where(*filter_list).values(**params)

        try:
            session.execute(stmt)
            return True
        except exc.IntegrityError as er:
            print(er)
            return False
        finally:
            session.close()

    @staticmethod
    def delete_restore_entity(obj, obj_filter: dict, restore=False):
        session = DqConnection('dqServer').session_dq

        filter_list = []
        for key in obj_filter:
            filter_list.append(key == obj_filter[key])

        stmt = update(obj).where(*filter_list).values(deleted_flag='N' if restore else 'Y')
        session.execute(stmt)

        session.close()

    @staticmethod
    def hard_delete_entity(obj, obj_filter: dict):
        session = DqConnection('dqServer').session_dq

        filter_list = []
        for key in obj_filter:
            filter_list.append(key == obj_filter[key])

        stmt = delete(obj).where(*filter_list)
        session.execute(stmt)

        session.close()
