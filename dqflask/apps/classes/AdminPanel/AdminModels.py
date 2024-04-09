from sqlalchemy import Column, Integer, String
from ..database import DqConnection


dq_connection = DqConnection('dqServer')
Base_dqps = dq_connection.Base_dqps


class dq_teams_sdim(Base_dqps):
    __tablename__ = 'dq_teams_sdim'
    __table_args__ = {"schema": "SSDQ"}

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(1000))
    edit_mode = Column(String(10))
    deleted_flag = Column(String(1))

    def __init__(self, id=None, name=None, description=None, edit_mode=None, deleted_flag=None):
        self.id = id
        self.name = name
        self.description = description
        self.edit_mode = edit_mode
        self.deleted_flag = deleted_flag

    def __repr__(self):
        return '<dq_teams_sdim %r %r %r %r %r>' % (
            self.id, self.name, self.description, self.edit_mode, self.deleted_flag)


class dq_user2team_sdim(Base_dqps):
    __tablename__ = 'dq_user2team_sdim'
    __table_args__ = {"schema": "SSDQ"}

    user_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, primary_key=True)
    is_owner = Column(String(1))

    def __init__(self, user_id=None, team_id=None, is_owner=None):
        self.user_id = user_id
        self.team_id = team_id
        self.is_owner = is_owner

    def __repr__(self):
        return '<dq_user2team_sdim %r %r %r>' % (self.user_id, self.team_id, self.is_owner)


class dq_user2team_request(Base_dqps):
    __tablename__ = 'dq_user2team_request'
    __table_args__ = {"schema": "SSDQ"}

    user_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, primary_key=True)

    def __init__(self, user_id=None, team_id=None):
        self.user_id = user_id
        self.team_id = team_id

    def __repr__(self):
        return '<dq_user2team_request %r %r>' % (self.user_id, self.team_id)


class view_team_users(Base_dqps):
    __tablename__ = 'view_team_users'
    __table_args__ = {"schema": "SSDQ"}

    user_id = Column(Integer, primary_key=True)
    full_name = Column(String(255))
    email = Column(String(255))
    team_id = Column(Integer, primary_key=True)
    is_owner = Column(String(1))

    def __init__(self, user_id=None, full_name=None, email=None, team_id=None, is_owner=None):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.team_id = team_id
        self.is_owner = is_owner

    def __repr__(self):
        return '<view_team_users %r %r %r %r %r>' % (self.user_id, self.full_name, self.email, self.team_id,
                                                     self.is_owner)


class dq_control2team_sdim(Base_dqps):
    __tablename__ = 'dq_control2team_sdim'
    __table_args__ = {"schema": "SSDQ"}

    control_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, primary_key=True)

    def __init__(self, control_id=None, team_id=None):
        self.control_id = control_id
        self.team_id = team_id

    def __repr__(self):
        return '<dq_control2team_sdim %r %r>' % (self.control_id, self.team_id)


class view_teams_requests(Base_dqps):
    __tablename__ = 'view_teams_requests'
    __table_args__ = {"schema": "SSDQ"}

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(255))
    user_id = Column(Integer, primary_key=True)
    login = Column(String(20))
    full_name = Column(String(255))

    def __init__(self, team_id=None, team_name=None, user_id=None, login=None, full_name=None):
        self.team_id = team_id
        self.team_name = team_name
        self.user_id = user_id
        self.login = login
        self.full_name = full_name

    def __repr__(self):
        return '<view_teams_requests %r %r %r %r %r>' % (self.team_id, self.team_name, self.user_id, self.login,
                                                         self.full_name)
