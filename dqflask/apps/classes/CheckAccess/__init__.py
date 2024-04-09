from ..models import dq_control_param_hdim, user_w_role
from .TeamAccess import TeamAccess


class CheckAccess(TeamAccess):
    _create_roles = ['DQ_ADMIN', 'DQ_OFFICER']

    def __init__(self, login):
        self.login = login
        self.user_id = self.get_user_id(login)

    def check_role(self, roles=None):
        users = user_w_role.query.filter(user_w_role.user_id == self.login).first()
        roles = self._create_roles if roles is None else roles

        if users:
            res = list(set(roles) & set(users.role))
            response = True if len(res) > 0 else False
        else:
            response = False

        return response

    def is_admin(self):
        try:
            users = user_w_role.query.filter(user_w_role.user_id == self.login).first()
            for cur in users.role:
                if cur == 'DQ_ADMIN':
                    return True
            return False
        except Exception as ex:
            print(ex)
            return False

    def check_officer(self, dqi):
        try:
            officer_uk = dq_control_param_hdim.query.filter(dq_control_param_hdim.validto == '5999-12-31',
                                                            dq_control_param_hdim.deleted_flag != 'Y',
                                                            dq_control_param_hdim.dq_request_uk == dqi)\
                .first().officer_uk
            return True if officer_uk == self.user_id else False
        except Exception as ex:
            print(ex)
            return False

    def check_edit_spec(self, dqi):
        if self.is_admin():
            return True
        elif self.check_officer(dqi):
            return True
        elif self.check_spec_by_team(self.user_id, dqi):
            return True
        else:
            return False

    def check_edit_team(self, team_id):
        if self.is_admin():
            return True
        elif self.check_owner(self.user_id, team_id):
            return True
        else:
            return False

    def get_access_matrix(self):
        if self.is_admin():
            response = {
                'is_admin': True,
                'teams': None,
                'user_id': None
            }
            return response
        else:
            team_list = self.get_team_list(self.user_id)
            response = {
                'is_admin': False,
                'teams': team_list,
                'user_id': self.user_id
            }
            return response
