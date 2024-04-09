from ..database import DqConnection
from flask import request, render_template
from sqlalchemy import insert, delete
from ..models import user_roles, user_w_role
from ..Logger.LogEvent import LogEvent


class AdminUsers:
    """
    Class with users
    """
    dq_db_connection = DqConnection('flaskDb')

    def __init__(self, method, uk=None):
        """
        initialize class and get form from html
        :param method: "GET", "POST" - request.method
        :param uk: user ID
        """
        self.dqps_session = self.dq_db_connection.session_dq
        self.uk = uk
        self.method = method
        self.role_ids = []

        if method == 'GET':
            if uk is not None:
                self.users = user_w_role.query.filter(user_w_role.user_id == uk).all()[0]

        else:
            if request.form.get('Readonly') == 'on':
                self.role_ids.append(1)
            if request.form.get('DQ_OFFICER') == 'on':
                self.role_ids.append(2)
            if request.form.get('DQ_ADMIN') == 'on':
                self.role_ids.append(3)
            if request.form.get('DQ_STEWARD') == 'on':
                self.role_ids.append(4)

        self.log = LogEvent()
        self.dqps_session.close()

    def update_user(self):
        """
        delete all roles for init user and insert selected in UI roles
        """
        stmt = delete(user_roles).where(user_roles.user_id == self.uk)

        self.dqps_session.execute(stmt)

        for cur in self.role_ids:
            stmt = insert(user_roles).values(
                user_id=self.uk,
                role_id=cur
            )
            self.dqps_session.execute(stmt)

        self.dqps_session.close()

        return '', 204

    def render(self, login):
        """
        render html page
        :return: rendered template
        """
        self.log.log_get(login, 'adm-users')
        if self.uk is not None:
            return render_template('home/adm-change-user.html', user=self.users)
        else:
            return render_template('home/adm-users.html')

    def response(self, login):
        if self.method == 'POST':
            self.log.log_post(login, 'updated', f'user {str(self.uk)}')
            return self.update_user()
        else:
            return self.render(login)




