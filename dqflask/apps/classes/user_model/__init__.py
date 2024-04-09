# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from ... import db
from ..AdminPanel.DqTeams import DqTeamRequest
from ..CheckAccess.TeamAccess import TeamAccess
from flask import redirect
import datetime


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(255))
    login = db.Column(db.String(255), unique=True)

    # timestamp = db.Column(db.Date, unique=True)

    def __init__(self, id=None, email=None, name=None, login=None):
        self.id = id
        self.email = email
        self.name = name
        self.login = login

    def __repr__(self):
        return str(self.email)

    def has_notification(self):
        user_id = TeamAccess.get_user_id(self.login)
        teams = TeamAccess.get_team_list(user_id, is_owner=True)
        if teams is None:
            return False
        else:
            return DqTeamRequest.has_requests(teams)


class user_login(db.Model):
    __tablename__ = 'user_login'

    user_id = db.Column(db.String(255), primary_key=True)
    login_timestamp = db.Column(db.DateTime, unique=True)
    access_token = db.Column(db.String(3000))

    def __init__(self, user_id=None, login_timestamp=None, access_token=None):
        self.user_id = user_id
        self.login_timestamp = login_timestamp
        self.access_token = access_token

    def __repr__(self):
        return '<user_login %r %r>' % (self.user_id, self.login_timestamp)


def hello_world(b):
    if b:
        return redirect('dq_analytics')
    else:
        # return render_template('accounts/login.html')
        return redirect('private')


def hello_me(info, token_id):
    # name  = f"{info.get('given_name')} {info.get('family_name')}"
    # login = info.get('preferred_username')
    # email = info.get('email')
    id = "gpbu0001"
    name = "admin"
    login = "admin"
    email = "admin3@example.ru"
    # id = info.get('sub')
    # Check usename exists
    user = Users.query.filter_by(id=login).first()
    current_date = datetime.datetime.now()
    user_login_info = user_login(login, current_date, token_id)
    if user:
        db.session.add(user_login_info)
        db.session.commit()
        return redirect('dq_analytics')
    else:
        # else we can create the user
        user = Users(login, email, name, login)
        db.session.add(user)
        db.session.add(user_login_info)
        db.session.commit()

        # user = dq_user_hdim(ad_login=login, full_name=name, email=email, status='WORK', deleted_flag='N',
        #                     validfrom=current_date, validto='5999-12-31')
        # dq_conn = DqConnection('dqServer')
        # dq_session = Session(bind=dq_conn.engine_dq)
        # dq_session.add(user)
        # dq_session.commit()

        return redirect('dq_analytics')


class user_roles(db.Model):
    __tablename__ = 'user_roles'

    user_id = db.Column(db.String(255), primary_key=True)
    role_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, user_id=None, role_id=None):
        self.user_id = user_id
        self.role_id = role_id

    def __repr__(self):
        return '<user_login %r %r>' % (self.user_id, self.role_id)