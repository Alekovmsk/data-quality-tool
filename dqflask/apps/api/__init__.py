from flask import Blueprint, request
from .Ajax import Select2API, DataTableAPI
from .airflowAPI import AirflowAPI
from ..classes.AdminPanel.AdminModels import view_team_users, view_teams_requests
from ..classes.AdminPanel.DqTeams import DqTeamUser, DqTeams, DqTeamRequest
from ..classes.AdminPanel.DqObjects import AdminObjects
from ..classes.CheckAccess import CheckAccess
from ..classes.Logger.LogEvent import LogEvent
from ..classes.CheckAccess.TeamAccess import TeamAccess


log = LogEvent()
api_routes = Blueprint('api_routes', __name__, template_folder='templates')


@api_routes.route('/api/spec/officers', methods=['GET'])
def get_officers():
    return Select2API('dq_user_hdim').response()


@api_routes.route('/api/spec/objects', methods=['GET'])
def get_objects():
    return Select2API('dq_object_hdim').response()


@api_routes.route('/api/spec/teams', methods=['GET'])
def get_teams():
    return Select2API('dq_teams_sdim').response()


@api_routes.route('/api/admin/adm-users', methods=['POST'])
def get_users():
    return DataTableAPI('users').response()


@api_routes.route('/api/admin/adm-objects', methods=['POST'])
def get_admin_objects():
    return DataTableAPI('dq_object_hdim').response()


@api_routes.route('/api/admin/adm-teams', methods=['POST'])
def get_admin_teams():
    return DataTableAPI('dq_teams_sdim').response()


@api_routes.route('/api/admin/team-requests', methods=['POST'])
def get_teams_requests():
    login = request.args.get('login')
    user_id = TeamAccess.get_user_id(login)
    if request.args.get('myRequests') == 'false':
        team_list = TeamAccess.get_team_list(user_id, is_owner=True)
        filters = [view_teams_requests.team_id.in_(team_list)]
    else:
        filters = [view_teams_requests.user_id == user_id]
    return DataTableAPI('view_teams_requests').response(*filters)


@api_routes.route('/api/admin/get_team_users', methods=['POST'])
def get_team_users():
    team_id = request.args.get('team_id')
    filters = [view_team_users.team_id == team_id]
    return DataTableAPI('view_team_users').response(*filters)


@api_routes.route('/api/admin/addUser', methods=['POST'])
def add_user():
    return DqTeamUser(request.args.get('login')).add_user()


@api_routes.route('/api/admin/updateUser', methods=['POST'])
def update_user():
    return DqTeamUser(request.args.get('login')).update_user()


@api_routes.route('/api/admin/removeUser', methods=['POST'])
def remove_user():
    return DqTeamUser(request.args.get('login')).remove_user()


@api_routes.route('/api/admin/acceptUser', methods=['POST'])
def accept_user():
    return DqTeamRequest(request.args.get('login')).accept_user()


@api_routes.route('/api/admin/declineUser', methods=['POST'])
def decline_user():
    return DqTeamRequest(request.args.get('login')).decline_user()


@api_routes.route('/api/admin/addTeam', methods=['POST'])
def add_team():
    return DqTeams(request.args.get('login')).add_team()


@api_routes.route('/api/admin/updateTeam', methods=['POST'])
def update_team():
    return DqTeams(request.args.get('login'), request.form.get('team_id')).update_team()


@api_routes.route('/api/admin/removeTeam', methods=['POST'])
def remove_team():
    return DqTeams(request.args.get('login'), request.form.get('team_id')).delete_restore_team()


@api_routes.route('/api/admin/hardRemoveTeam', methods=['POST'])
def hard_remove_team():
    return DqTeams(request.args.get('login'), request.form.get('team_id')).hard_delete_team()


@api_routes.route('/api/admin/restoreTeam', methods=['POST'])
def restore_team():
    return DqTeams(request.args.get('login'), request.form.get('team_id')).delete_restore_team(restore=True)


@api_routes.route('/api/admin/requestToTeam', methods=['POST'])
def request_to_team():
    return DqTeams(request.args.get('login'), request.form.get('team_id')).request_to_team()


@api_routes.route('/api/admin/exitTeam', methods=['POST'])
def exit_team():
    login = request.args.get('login')
    user_id = TeamAccess.get_user_id(login)
    return DqTeamUser(login, user_id=user_id).remove_user()


@api_routes.route('/api/admin/addObject', methods=['POST'])
def add_object():
    return AdminObjects(request.args.get('login')).add_object()


@api_routes.route('/api/admin/updateObject', methods=['POST'])
def update_object():
    return AdminObjects(request.args.get('login'), request.form.get('uk')).update_object()


@api_routes.route('/api/admin/removeObject', methods=['POST'])
def remove_object():
    return AdminObjects(request.args.get('login'), request.form.get('uk')).delete_restore_object()


@api_routes.route('/api/admin/restoreObject', methods=['POST'])
def restore_object():
    return AdminObjects(request.args.get('login'), request.form.get('uk')).delete_restore_object(restore=True)


@api_routes.route('/api/dags/triggerDag', methods=['POST'])
def trigger_dag():
    uk = request.args.get('uk')
    login = request.args.get('login')
    if not CheckAccess(login).check_edit_spec(uk):
        log.log_insufficient_privileges(login, f'/trigger Dag {uk}')
        response = {'message': 'Недостаточно привелегий для выполнения данного действия!'}
        return response, 200
    AirflowAPI().trigger_dag(uk)
    log.log_post(login, 'triggered', f'dag {str(id)}')
    return '', 204


@api_routes.route('/api/dags/killDag', methods=['POST'])
def kill_dag():
    uk = request.args.get('uk')
    login = request.args.get('login')
    if not CheckAccess(login).check_edit_spec(uk):
        log.log_insufficient_privileges(login, f'/kill Dag {uk}')
        response = {'message': 'Недостаточно привелегий для выполнения данного действия!'}
        return response, 200
    AirflowAPI().kill_dag(uk)
    log.log_post(login, 'killed', f'dag {uk}')
    return '', 204


@api_routes.route('/api/dags/pauseDag', methods=['POST'])
def pause_dag():
    uk = request.args.get('uk')
    login = request.args.get('login')
    if not CheckAccess(login).check_edit_spec(uk):
        log.log_insufficient_privileges(login, f'/pause Dag {uk}')
        response = {'message': 'Недостаточно привелегий для выполнения данного действия!'}
        return response, 200
    AirflowAPI().pause_dag(uk)
    log.log_post(login, 'paused', f'dag {uk}')
    return '', 204


@api_routes.route('/api/dags/unpauseDag', methods=['POST'])
def unpause_dag():
    uk = request.args.get('uk')
    login = request.args.get('login')
    if not CheckAccess(login).check_edit_spec(uk):
        log.log_insufficient_privileges(login, f'/unpause Dag {uk}')
        response = {'message': 'Недостаточно привелегий для выполнения данного действия!'}
        return response, 200
    AirflowAPI().unpause_dag(uk)
    log.log_post(login, 'unpaused', f'dag {uk}')
    return '', 204
