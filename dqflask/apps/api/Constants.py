from ..classes.models import dq_object_hdim, user_w_role
from ..classes.AdminPanel.AdminModels import dq_teams_sdim, view_team_users, view_teams_requests


class Const:
    objects = {
        'users': user_w_role,
        'dq_object_hdim': dq_object_hdim,
        'dq_teams_sdim': dq_teams_sdim,
        'view_team_users': view_team_users,
        'view_teams_requests': view_teams_requests
    }
    attributes = {
        'users': {
            1: user_w_role.user_id,
            2: user_w_role.name,
            3: user_w_role.email,
            4: user_w_role.role
        },
        'dq_object_hdim': {
            1: dq_object_hdim.uk,
            2: dq_object_hdim.schema,
            3: dq_object_hdim.table_name,
            4: dq_object_hdim.description,
            5: dq_object_hdim.deleted_flag
        },
        'dq_teams_sdim': {
            1: dq_teams_sdim.id,
            2: dq_teams_sdim.name,
            3: dq_teams_sdim.description,
            4: dq_teams_sdim.edit_mode,
            5: dq_teams_sdim.deleted_flag
        },
        'view_team_users': {
            1: view_team_users.user_id,
            2: view_team_users.full_name,
            3: view_team_users.email,
            4: view_team_users.is_owner
        },
        'view_teams_requests': {
            1: view_teams_requests.team_id,
            2: view_teams_requests.team_name,
            3: view_teams_requests.user_id,
            4: view_teams_requests.login,
            5: view_teams_requests.full_name
        }
    }
    attributes_flt = {
        'users': {
            1: user_w_role.user_id,
            2: user_w_role.name,
            3: user_w_role.email
        },
        'dq_object_hdim': {
            1: dq_object_hdim.uk,
            2: dq_object_hdim.schema,
            3: dq_object_hdim.table_name,
            4: dq_object_hdim.description
        },
        'dq_teams_sdim': {
            1: dq_teams_sdim.id,
            2: dq_teams_sdim.name,
            3: dq_teams_sdim.description
        },
        'view_team_users': {
            1: view_team_users.user_id,
            2: view_team_users.full_name,
            3: view_team_users.email
        },
        'view_teams_requests': {
            1: view_teams_requests.team_id,
            2: view_teams_requests.team_name,
            3: view_teams_requests.user_id,
            4: view_teams_requests.login,
            5: view_teams_requests.full_name
        }
    }
