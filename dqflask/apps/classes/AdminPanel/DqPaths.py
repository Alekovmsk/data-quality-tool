from ..database import DqConnection
from flask import request, redirect, render_template
from sqlalchemy import insert, update, Sequence
from ..Logger.LogEvent import LogEvent


class AdminPaths:
    dq_db_connection = DqConnection('dqServer')

    def __init__(self, method, uk=None):
        """
        initialize class and get form from html
        :param method: "GET", "POST" - request.method
        :param uk: path ID
        """
        self.dqps_session = self.dq_db_connection.session_dq
        self.uk = uk
        self.method = method

        if method == 'GET':
            self.paths = dq_ftp_path_ldim.query.filter().all()
            if uk is not None:
                self.path_n = dq_ftp_path_ldim.query.filter(dq_ftp_path_ldim.uk == uk).all()[0]

        else:
            self.path_name = request.form.get('path_name')
            self.host = request.form.get('host')

        self.log = LogEvent()

    def add_path(self):
        """
        add a new path
        :return: redirect to edit path page
        """
        seq = Sequence('dq_ftp_path_ldim_seq', schema="SSDQ")
        self.uk = self.dqps_session.execute(seq)

        stmt = insert(dq_ftp_path_ldim).values(
            uk=self.uk,
            path_name=self.path_name,
            host=self.host
        )
        self.dqps_session.execute(stmt)

        self.dqps_session.close()
        return redirect('/admin/adm-paths/' + str(self.uk))

    def update_path(self):
        """
        Update path's info according selected action in UI
        action: selected action (delete or update)
        :return: redirect to edit object page
        """
        action = request.form.get('action')

        if action == 'Сохранить':
            stmt = update(dq_ftp_path_ldim).where(dq_ftp_path_ldim.uk == self.uk).values(
                path_name=self.path_name,
                host=self.host
            )
            self.dqps_session.execute(stmt)

        elif action == 'Удалить':
            stmt = delete(dq_ftp_path_ldim).where(dq_ftp_path_ldim.uk == self.uk)
            self.dqps_session.execute(stmt)

        self.dqps_session.close()
        dir = f'/admin/adm-paths/{self.uk}' if action == 'Сохранить' else f'/admin/adm-paths'

        return redirect(dir)

    def render(self):
        """
        render html page
        :return: rendered template
        """
        if self.uk is not None:
            return render_template('home/adm-change-path.html', paths=self.paths, path_n=self.path_n)
        else:
            return render_template('home/adm-paths.html', paths=self.paths)

    def response(self, login):
        if self.method == 'POST':
            self.log.log_post(login, 'created' if self.uk is None else 'updated', f'path {str(self.uk)}')
            return self.add_path() if self.uk is None else self.update_path()
        else:
            self.log.log_get(login, 'adm-paths')
            return self.render()