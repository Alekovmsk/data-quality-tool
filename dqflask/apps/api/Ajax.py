from ..classes.database import DqConnection
from ..classes.models import dq_user_hdim, dq_object_hdim
from ..classes.AdminPanel.AdminModels import dq_teams_sdim
from sqlalchemy import or_, func, and_, cast, String
from flask import jsonify, request
from .Constants import Const


class Select2API:
    objects = {
        'dq_user_hdim': dq_user_hdim,
        'dq_object_hdim': dq_object_hdim,
        'dq_teams_sdim': dq_teams_sdim
    }
    attributes = {
        'dq_user_hdim': [dq_user_hdim.full_name, dq_user_hdim.email],
        'dq_object_hdim': [dq_object_hdim.table_name, dq_object_hdim.schema],
        'dq_teams_sdim': [dq_teams_sdim.name]
    }
    obj_key = {
        'dq_user_hdim': 'uk',
        'dq_object_hdim': 'uk',
        'dq_teams_sdim': 'id'
    }

    def __init__(self, object_name: str):
        self.dq_db_connection = DqConnection('dqServer')
        self.object_name = object_name

        try:
            self.obj = self.objects[object_name]
            self.attr = self.attributes[object_name]
        except KeyError:
            self.obj = None
            self.attr = None

    def response(self):
        if self.obj is None:
            return 'No objects found', 500

        search_string = request.args.get('search')
        search_like = f'%%{search_string}%%'

        page = int(request.args.get('page'))
        if page == 1:
            offset = 0
            limit = 11
        else:
            offset = page * 10 - 10
            limit = page * 10 + 1

        return self.get_db_data(search_like, offset, limit)

    def get_db_data(self, search: str, offset: int, limit: int):

        db_data = self.obj.query.filter(
            self.obj.deleted_flag != 'Y',
            or_(func.upper(at).like(func.upper(search)) for at in self.attr)
        ).order_by(getattr(self.obj, self.obj_key[self.object_name])).limit(limit).offset(offset).all()

        data = []
        more = 'false'
        ind = 0
        for row in db_data:
            ind += 1
            if ind == 11:
                more = 'true'
                break

            data.append(self.__get_resp(row))

        response = {
            'results': data,
            'pagination': {
                'more': more
            }
        }

        self.dq_db_connection.session_dq.close()
        return jsonify(response)

    def __get_resp(self, row):
        if self.object_name == 'dq_user_hdim':
            resp = {
                'id': getattr(row, self.obj_key[self.object_name]),
                'text': f"{row.full_name} ({row.email})"
            }
        elif self.object_name == 'dq_object_hdim':
            resp = {
                'id': getattr(row, self.obj_key[self.object_name]),
                'text': f"{row.schema}.{row.table_name}"
            }
        else:
            text = ''
            for key in self.attributes[self.object_name]:
                text += getattr(row, str(key).split('.')[1]) + ' '
            resp = {
                'id': getattr(row, self.obj_key[self.object_name]),
                'text': text
            }

        return resp


class DataTableAPI(Const):
    def __init__(self, object_name: str):
        self.dq_db_connection = DqConnection('dqServer')
        self.object_name = object_name

        try:
            self.obj = self.objects[object_name]
        except KeyError:
            self.obj = None

    def response(self, *filters):
        draw = request.form['draw']
        search_value = request.form['search[value]']
        search_like = None if search_value is None or search_value == '' else f'%%{search_value.upper()}%%'

        data = self.__get_db_data(search_like, *filters)

        total_records = self.__get_total_rows(*filters)
        total_record_filtered = total_records if search_like is None else len(data)

        response = {
            'draw': draw,
            'iTotalRecords': total_records,
            'iTotalDisplayRecords': total_record_filtered,
            'aaData': data,
        }

        return response

    def __get_db_data(self, search: str | None = None, *filters):
        attr_list = [attr for attr in self.obj.__dict__ if not attr.startswith("_")]

        row = int(request.form['start'])
        rowperpage = int(request.form['length'])

        order_id = self.attributes[self.object_name][int(request.form['order[0][column]']) + 1]
        order_dir = request.form['order[0][dir]']

        order = order_id if order_dir == 'asc' else order_id.desc()

        try:
            if search is None:
                dataset = self.obj.query.filter(*filters)\
                    .order_by(order).limit(int(rowperpage)).offset(int(row)).all()
            else:
                dataset = self.obj.query.filter(and_(
                    *filters,
                    or_(
                        func.upper(cast(self.attributes_flt[self.object_name][attr], String)).like(search) for attr in
                        self.attributes_flt[self.object_name]
                    )
                )).order_by(order).limit(int(rowperpage)).offset(int(row)).all()
        except KeyError:
            if search is None:
                dataset = self.obj.query.order_by(order).limit(int(rowperpage)).offset(int(row)).all()
            else:
                dataset = self.obj.query.filter(
                    or_(
                        func.upper(cast(self.attributes_flt[self.object_name][attr], String)).like(search) for attr in
                        self.attributes_flt[self.object_name]
                    )
                ).order_by(order).limit(int(rowperpage)).offset(int(row)).all()

        data = []
        for row in dataset:
            krow = {}
            for key in attr_list:
                krow[key] = getattr(row, key)
            data.append(krow)

        return data

    def __get_total_rows(self, *filters):
        """
        count rows in database object
        :param filters: kwargs with key attribute_flt (attribute for filtering) and value attribute_val (filter value)
        :return: rows count
        """
        try:
            return self.obj.query.filter(*filters).count()
        except KeyError:
            return self.obj.query.count()
