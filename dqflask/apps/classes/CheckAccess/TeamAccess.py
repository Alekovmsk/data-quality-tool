from ..AdminPanel.AdminModels import dq_user2team_sdim, dq_control2team_sdim, dq_teams_sdim
from ..models import dq_user_hdim
from sqlalchemy import or_, and_


class TeamAccess:
    @staticmethod
    def get_teams(user_id, is_owner=False):
        if is_owner:
            teams = dq_user2team_sdim.query.filter(dq_user2team_sdim.user_id == user_id,
                                                   dq_user2team_sdim.is_owner == 'Y').all()
        else:
            teams = dq_user2team_sdim.query.filter(dq_user2team_sdim.user_id == user_id).all()
        return teams

    @staticmethod
    def get_team_list(user_id, is_owner=False):
        if is_owner:
            teams = dq_user2team_sdim.query.filter(dq_user2team_sdim.user_id == user_id,
                                                   dq_user2team_sdim.is_owner == 'Y').all()
        else:
            teams = dq_user2team_sdim.query.filter(dq_user2team_sdim.user_id == user_id).all()
        return [row.team_id for row in teams] if len(teams) > 0 else None

    @staticmethod
    def get_user_id(login):
        try:
            return dq_user_hdim.query.filter(dq_user_hdim.ad_login == login,
                                             dq_user_hdim.deleted_flag != 'Y',
                                             dq_user_hdim.validto == '5999-12-31').first().uk
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def is_team_admin(user_id, team_id):
        is_admin = dq_user2team_sdim.query.filter(dq_user2team_sdim.user_id == user_id,
                                                  dq_user2team_sdim.team_id == team_id,
                                                  dq_user2team_sdim.is_owner == 'Y').first()
        return False if is_admin is None else True

    def check_spec_by_team(self, user_id, dqi):
        teams = self.get_teams(user_id)

        if teams is None:
            return False
        else:
            owner_team = []
            all_team = []
            for cur in teams:
                if cur.is_owner == 'Y':
                    owner_team.append(cur.team_id)
                else:
                    all_team.append(cur.team_id)

            teams_info = dq_teams_sdim.query.filter(dq_teams_sdim.deleted_flag != 'Y',
                                                    or_(
                                                        and_(dq_teams_sdim.id.in_(all_team),
                                                             dq_teams_sdim.edit_mode == 'all'),
                                                        and_(dq_teams_sdim.id.in_(owner_team),
                                                             dq_teams_sdim.edit_mode == 'owners')
                                                    )).all()
            if teams_info is None:
                return False
            else:
                accessed_list = [row.id for row in teams_info]

            controls = dq_control2team_sdim.query.filter(dq_control2team_sdim.team_id.in_(accessed_list),
                                                         dq_control2team_sdim.control_id == dqi).first()
            return False if controls is None else True

    @staticmethod
    def check_owner(user_id, team_id):
        team = dq_user2team_sdim.query.filter(dq_user2team_sdim.user_id == user_id,
                                              dq_user2team_sdim.team_id == team_id,
                                              dq_user2team_sdim.is_owner == 'Y').first()
        return False if team is None else True
