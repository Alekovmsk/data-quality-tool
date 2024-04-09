from .AdminModels import dq_teams_sdim, dq_user2team_sdim, dq_user2team_request, view_teams_requests
from ..models import dq_user_hdim
from flask import request, render_template
from . import AdminPanel
from ..Logger.LogEvent import LogEvent
from ..database import DqConnection
from ..CheckAccess.TeamAccess import TeamAccess
from sqlalchemy.orm import Session


class DqTeams(AdminPanel):
    def __init__(self, login, team_id=None):
        """
        :param login: authorized User
        :param team_id: team ID
        """
        self.login = login
        self.user_id = dq_user_hdim.query.filter(dq_user_hdim.ad_login == self.login,
                                                 dq_user_hdim.validto == '5999-12-31',
                                                 dq_user_hdim.deleted_flag != 'Y').first().uk
        self.team_id = team_id
        self.log = LogEvent()

    def response(self):
        if self.team_id is None:
            team_list = TeamAccess.get_team_list(self.user_id)
            if team_list is not None:
                team_list = [int(row) for row in team_list]
            return render_template('home/adm-teams.html', team_list=team_list)
        else:
            is_admin = TeamAccess.is_team_admin(self.user_id, self.team_id)
            team = dq_teams_sdim.query.filter(dq_teams_sdim.id == self.team_id).first()
            return render_template('home/adm-change-teams.html', teams=team, is_admin=is_admin)

    def add_team(self):
        parameters = {
            'obj': dq_teams_sdim,
            'params': ['name', 'description', 'edit_mode'],
            'seq_name': 'dq_teams_sdim_seq',
            'seq_schema': 'SSDQ',
            'seq_id': 'id'
        }
        self.team_id = self.add_entity(**parameters)
        if self.team_id == -1:
            response = {'message': 'Команда с введенным наименованием уже существует!'}
            return response, 200
        else:
            user2team = dq_user2team_sdim(
                team_id=self.team_id,
                user_id=self.user_id,
                is_owner='Y'
            )
            session = Session(bind=DqConnection('dqServer').engine_dq)
            session.add(user2team)
            session.commit()
            session.close()
            self.log.log_post(self.login, f'has created team', self.team_id)
            return '', 204

    def update_team(self):
        parameters = {
            'obj': dq_teams_sdim,
            'params': ['name', 'description', 'edit_mode'],
            'obj_filter': {
                dq_teams_sdim.id: self.team_id
            }
        }
        response = self.update_entity(**parameters)
        if response:
            self.log.log_post(self.login, f'has updated team', self.team_id)
            return '', 204
        else:
            response = {'message': 'Команда с введенным наименованием уже существует!'}
            return response, 200

    def delete_restore_team(self, restore=False):
        parameters = {
            'obj': dq_teams_sdim,
            'obj_filter': {
                dq_teams_sdim.id: self.team_id
            },
            'restore': restore
        }
        self.delete_restore_entity(**parameters)
        self.log.log_post(self.login, f"has {'restored' if restore else 'removed'} team", self.team_id)
        return '', 204

    def hard_delete_team(self):
        parameters = {
            'obj': dq_teams_sdim,
            'obj_filter': {
                dq_teams_sdim.id: self.team_id
            }
        }
        self.hard_delete_entity(**parameters)

        parameters = {
            'obj': dq_user2team_sdim,
            'obj_filter': {
                dq_user2team_sdim.team_id: self.team_id
            }
        }
        self.hard_delete_entity(**parameters)

        self.log.log_post(self.login, 'has deleted (hard) team', self.team_id)
        return '', 204

    def request_to_team(self):
        parameters = {
            'obj': dq_user2team_request,
            'params': None,
            'user_id': self.user_id,
            'team_id': self.team_id
        }
        self.team_id = self.add_entity(**parameters)
        if self.team_id == -1:
            response = {'message': 'Запрос на вступление в данную команду уже отправлен!'}
            return response, 200
        else:
            return '', 204


class DqTeamUser(AdminPanel):
    def __init__(self, login, team_id=None, user_id=None):
        self.login = login
        self.team_id = request.form.get('team_id') if team_id is None else team_id
        self.user_id = request.form.get('user_id') if user_id is None else user_id
        self.log = LogEvent()

    def add_user(self):
        response = self._add_user()
        if response is None:
            self.log.log_post(self.login, f'has added user {self.user_id} to team', self.team_id)
            return '', 204
        else:
            return response, 200

    def update_user(self):
        self.__update_user()
        self.log.log_post(self.login, f'has updated user {self.user_id} in team', self.team_id)
        return '', 204

    def remove_user(self):
        self.__remove_user()
        self.log.log_post(self.login, f'has removed user {self.user_id} from team', self.team_id)
        return '', 204

    def _add_user(self):
        parameters = {
            'obj': dq_user2team_sdim,
            'params': ['team_id', 'user_id', 'is_owner']
        }
        uk = self.add_entity(**parameters)
        if uk == -1:
            return {'message': 'Данный пользователь уже состоит в команде.'}
        else:
            return None

    def __update_user(self):
        parameters = {
            'obj': dq_user2team_sdim,
            'params': ['is_owner'],
            'obj_filter': {
                dq_user2team_sdim.team_id: self.team_id,
                dq_user2team_sdim.user_id: self.user_id
            }
        }
        self.update_entity(**parameters)

    def __remove_user(self):
        parameters = {
            'obj': dq_user2team_sdim,
            'obj_filter': {
                dq_user2team_sdim.team_id: self.team_id,
                dq_user2team_sdim.user_id: self.user_id
            }
        }
        self.hard_delete_entity(**parameters)


class DqTeamRequest(DqTeamUser):
    def __init__(self, login):
        """
        :param login: authorized User
        """
        super().__init__(login)

    def accept_user(self):
        response = self._add_user()
        self.__remove_request()
        self.log.log_post(self.login, f'accepted user {self.user_id} request to Team', self.team_id)
        if response is None:
            return '', 204
        else:
            return response

    def decline_user(self):
        self.__remove_request()
        self.log.log_post(self.login, f'declined user {self.user_id} request to Team', self.team_id)
        return '', 204

    def __remove_request(self):
        parameters = {
            'obj': dq_user2team_request,
            'obj_filter': {
                dq_user2team_request.team_id: self.team_id,
                dq_user2team_request.user_id: self.user_id
            }
        }
        self.hard_delete_entity(**parameters)

    @staticmethod
    def render(my_requests=False):
        return render_template('home/adm-teams-request.html', my_requests=my_requests)

    @staticmethod
    def has_requests(team_list):
        requests = dq_user2team_request.query.filter(dq_user2team_request.team_id.in_(team_list)).first()
        if requests is None:
            return False
        else:
            return True

