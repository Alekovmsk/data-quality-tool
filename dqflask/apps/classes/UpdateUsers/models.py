from sqlalchemy import Column, String
from ..database import DqConnection
from ..conf import ConfYaml


base = DqConnection('dqServer').Base_dqps
try:
    src_base = DqConnection('srcUsers').Base_dqps
except:
    src_base = DqConnection('dqServer').Base_dqps


class dq_department_delta(base):
    __tablename__ = 'dq_department_delta'
    __table_args__ = {"schema": "SSDQ"}
    name = Column(String(256), primary_key=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<dq_department_delta %r>' % self.name


class dq_user_delta(base):
    __tablename__ = 'dq_user_delta'
    __table_args__ = {"schema": "SSDQ"}
    login = Column(String(20), primary_key=True)
    full_name = Column(String(256))
    email = Column(String(256))
    department = Column(String(256))

    def __init__(self, login=None, full_name=None, email=None, department=None):
        self.login = login
        self.full_name = full_name
        self.email = email
        self.department = department

    def __repr__(self):
        return '<dq_department_delta %r %r %r %r>' % (self.login, self.full_name, self.email, self.department)


class DepartmentsTable(src_base):
    __tablename__ = ConfYaml.config['users']['users_table']
    __table_args__ = {"schema": ConfYaml.config['users']['users_schema']}
    name = Column(String(256), primary_key=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<departments %r>' % self.name


class UsersTable(src_base):
    __tablename__ = ConfYaml.config['users']['deps_table']
    __table_args__ = {"schema": ConfYaml.config['users']['deps_schema']}
    login = Column(String(20), primary_key=True)
    full_name = Column(String(256))
    email = Column(String(256))
    department = Column(String(256))

    def __init__(self, login=None, full_name=None, email=None, department=None):
        self.login = login
        self.full_name = full_name
        self.email = email
        self.department = department

    def __repr__(self):
        return f'<users %r %r %r %r>' % (self.login, self.full_name, self.email, self.department)
