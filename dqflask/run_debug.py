import os
from flask_migrate import Migrate
from flask_minify import Minify
from sys import exit
from apps.config import config_dict
from apps import create_app
from flask import render_template, redirect
import json
from apps.classes import user_model
from apps.classes.user_model import Users
from flask_login import logout_user
from apps import db, login_manager
from flask_login import login_required
from flask import g, request
from flask_oidc import OpenIDConnect
from apps.classes.spec.RenderSpec import SpecHtml
from apps.classes.DqReport import Report, ReportAjax
from apps.classes.components import deleteSpec, changeSpec, createSpec
from apps.classes.AdminPanel import DqUsers, DqObjects, DqPaths, DqTeams
from apps.classes.DqMonitoring import DqMonitoring
from apps.classes.DqAnalytics import DqAnalytics
from apps.classes.CheckAccess import CheckAccess
from apps.classes.conf import ConfYaml
from apps.classes.Logger import LogLoad
from apps.classes.Logger.LogEvent import LogEvent

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)
oidc = OpenIDConnect(app)
log = LogEvent()


@app.route('/spec', methods=['GET'])
# @login_required
def spec():
    # log.log_get(oidc.user_getfield('preferred_username'), '/spec')
    login = 'admin'
    access = CheckAccess(login).get_access_matrix()
    return SpecHtml(**access).render()


@app.route('/create-spec', methods=['POST', 'GET'])
# @login_required
def create_spec():
    login = 'admin' # oidc.user_getfield('preferred_username')
    name = 'admin' # f"{oidc.user_getfield('given_name')} {oidc.user_getfield('family_name')}"
    return createSpec.CreateSpec(login, name, request.method).response()


@app.route('/change-spec/<int:id>', methods=['POST', 'GET'])
# @login_required
def change_spec(id):
    login = 'admin' # oidc.user_getfield('preferred_username')
    name = 'admin' # f"{oidc.user_getfield('given_name')} {oidc.user_getfield('family_name')}"
    if not CheckAccess(login).check_edit_spec(id):
        log.log_insufficient_privileges(login, f'/change-spec/{str(id)}')
        return render_template('home/insufficient-privileges.html')

    return changeSpec.ChangeSpec(login, name, id, request.method).response()


@app.route('/delete-spec/<int:id>', methods=['POST', 'GET'])
@login_required
def delete_spec(id):
    login = oidc.user_getfield('preferred_username')

    deleteSpec.DeleteSpec.delete_spec(id)
    log.log_post(login, 'deleted', f'specification {str(id)}')
    return redirect('/spec')


@app.route('/dq_monitoring/<flt>', methods=['POST', 'GET'])
# @login_required
def dq_monitoring(flt):
    #login = oidc.user_getfield('preferred_username')
    login = "admin"
    access = CheckAccess(login).get_access_matrix() if request.method == 'POST' else {}
    return DqMonitoring(flt).response(login, request.method, **access)


@app.route('/dq_analytics', methods=['POST', 'GET'])
#@login_required
def dqan():
    login = 'admin' #oidc.user_getfield('preferred_username')
    access = CheckAccess(login).get_access_matrix()
    return DqAnalytics().response(login, request.method, **access)


@app.route('/dq_report/<int:id>', methods=['POST', 'GET'])
# @login_required
def report(id):
    # login = oidc.user_getfield('preferred_username')
    login = 'admin'
    wf = request.args.get('wf')
    is_editing = CheckAccess(login).check_edit_spec(id)
    if request.method == 'GET':
        log.log_get(login, f'dq_report {str(id)}')
        return Report(id, wf).render(is_editing)
    else:
        return ReportAjax(id, wf).get_report()


"""Admin routes"""


@app.route('/admin/adm-objects', methods=['POST', 'GET'])
# @login_required
def adm_objects():
    login = 'admin' # oidc.user_getfield('preferred_username')
    #if not CheckAccess(login).is_admin():
    #    log.log_insufficient_privileges(login, f'/adm-objects')
    #    return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'adm-objects')
    return DqObjects.AdminObjects(login).response()


@app.route('/admin/adm-objects/<id>', methods=['POST', 'GET'])
# @login_required
def adm_change_object(id):
    login = 'admin' #oidc.user_getfield('preferred_username')
    #if not CheckAccess(login).is_admin():
    #    log.log_insufficient_privileges(login, f'/adm-objects {str(id)}')
    #    return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'adm-objects/{id}')
    return DqObjects.AdminObjects(login, id).response()


@app.route('/admin/adm-users', methods=['GET'])
# @login_required
def adm_users():
    login = 'admin' # oidc.user_getfield('preferred_username')
    # if not CheckAccess(login).is_admin():
        # log.log_insufficient_privileges(login, f'/adm-users')
        # return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'adm-users')
    return DqUsers.AdminUsers(request.method).render(login)


@app.route('/admin/adm-users/<id>', methods=['POST', 'GET'])
# @login_required
def adm_change_user(id):
    login = 'admin' # oidc.user_getfield('preferred_username')
    #if not CheckAccess(login).is_admin():
    #    log.log_insufficient_privileges(login, f'/adm-users/{id}')
    #    return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'adm-users/{id}')
    return DqUsers.AdminUsers(request.method, id).response(login)


@app.route('/admin/adm-teams', methods=['POST', 'GET'])
# @login_required
def adm_teams():
    login = 'admin' # oidc.user_getfield('preferred_username')
    log.log_get(login, f'adm-teams')
    return DqTeams.DqTeams(login).response()


@app.route('/admin/adm-teams/<id>', methods=['POST', 'GET'])
# @login_required
def adm_change_team(id):
    login = 'admin' # oidc.user_getfield('preferred_username')
    if not CheckAccess(login).check_edit_team(id):
        log.log_insufficient_privileges(login, f'/adm-teams/{id}')
        return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'adm-teams/{id}')
    return DqTeams.DqTeams(login, id).response()


@app.route('/admin/teams-requests', methods=['POST', 'GET'])
# @login_required
def adm_team_requests():
    login = 'admin' # oidc.user_getfield('preferred_username')
    users_requests = bool(request.args.get('myRequests'))
    if not Users(login=login).has_notification() and not users_requests:
        log.log_insufficient_privileges(login, f'/teams-requests')
        return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'teams-requests')
    return DqTeams.DqTeamRequest.render(users_requests)


@app.route('/admin/adm-paths', methods=['POST', 'GET'])
@login_required
def adm_paths():
    login = oidc.user_getfield('preferred_username')
    if not CheckAccess(login).is_admin():
        log.log_insufficient_privileges(login, f'/adm-paths')
        return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'adm-paths')
    return DqPaths.AdminPaths(request.method).response(login)


@app.route('/admin/adm-paths/<id>', methods=['POST', 'GET'])
@login_required
def adm_change_paths(id):
    login = oidc.user_getfield('preferred_username')
    if not CheckAccess(login).is_admin():
        log.log_insufficient_privileges(login, f'/adm-paths/{id}')
        return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'adm-paths/{id}')
    return DqPaths.AdminPaths(request.method, id).response(login)


@app.route('/admin', methods=['GET'])
# @login_required
def admin_pn():
    login = 'admin' # oidc.user_getfield('preferred_username')
    #if not CheckAccess(login).is_admin():
    #    log.log_insufficient_privileges(login, f'/admin')
    #    return render_template('home/insufficient-privileges.html')
    log.log_get(login, f'admin')
    return render_template('home/admin.html')


@app.route('/login')
def hello_world():
    b = oidc.user_loggedin
    return user_model.hello_world(b)


@app.route('/')
def red():
    return redirect('/private')


@app.route('/private')
#@oidc.require_login
def hello_me():
    info = None #oidc.user_getinfo(['preferred_username', 'email', 'given_name', 'family_name'])
    #token_id = oidc.get_access_token()
    token_id=None
    return user_model.hello_me(info, token_id)


@app.route('/logout')
def logout():
    """Performs local logout by removing the session cookie."""
    logout_user()
    oidc.logout()
    return redirect('/login')


@app.route('/api', methods=['POST'])
@login_required
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def hello_api():
    """OAuth 2.0 protected API endpoint accessible via AccessToken"""

    return json.dumps({'hello': 'Welcome %s' % g.oidc_token_info['sub']})


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    try:
        #info = oidc.user_getinfo(['preferred_username', 'email', 'sub', 'name'])
        #email = info.get('email')
        email = 'admin@example.ru'
        user = Users.query.filter_by(email=email).first()
    except:
        user = None
    return user if user else None


@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect('/private')


if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG))
    app.logger.info('FLASK_ENV        = ' + os.getenv('FLASK_ENV'))
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE')
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)
    app.logger.info('ASSETS_ROOT      = ' + app_config.ASSETS_ROOT)

port = ConfYaml.config['ssdq']['port']

try:
    ssl = (ConfYaml.config['ssl']['cert'], ConfYaml.config['ssl']['key'])

except (TypeError, KeyError):
    print('App started without ssl')
    ssl = None


def upload_logs():
    LogLoad().insert_logs()


if __name__ == "__main__":

    # Adding scheduler for uploading logs into database. Configure scheduler in the config.yaml
    # scheduler = LogLoad().set_schedule()
    # scheduler.start()

    # Adding scheduler for updating users info in database. Configure scheduler in the config.yaml
    # scheduler_users = UsersInfo().set_schedule()
    # scheduler_users.start()

    # Start SSDQ Application
    app.logger.info('App SSDQ started')
    app.run(host='0.0.0.0', port=port, ssl_context=ssl, use_reloader=False)
    app.logger.info('App SSDQ stopped')

    # scheduler.shutdown()
    # scheduler_users.shutdown()
