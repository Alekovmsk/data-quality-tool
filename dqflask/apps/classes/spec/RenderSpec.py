from ..database import DqConnection
from ..models import view_specification_list, view_specification_info, view_specification_versions, \
    dq_control_param_hdim
from ..AdminPanel.AdminModels import dq_control2team_sdim
from flask import request, render_template
from sqlalchemy import or_


class SpecHtml:
    def __init__(self, is_admin: bool, user_id: int | str | None, teams: list | None):
        self.session = DqConnection('dqServer').session_dq
        if is_admin:
            self.filters = None
        else:
            self.filters = []
            if user_id is not None:
                sq = self.session.query(dq_control_param_hdim.dq_request_uk)\
                    .filter(dq_control_param_hdim.officer_uk == int(user_id),
                            dq_control_param_hdim.deleted_flag != 'Y',
                            dq_control_param_hdim.validto == '5999-12-31')\
                    .subquery()
                self.filters.append(sq)
            if teams is not None:
                sq = self.session.query(dq_control2team_sdim.control_id)\
                    .filter(dq_control2team_sdim.team_id.in_(teams)) \
                    .subquery()
                self.filters.append(sq)

    def render(self):
        if self.filters is None:
            specs = view_specification_list.query.filter().order_by(view_specification_list.code).all()
        else:
            specs = self.session.query(view_specification_list)\
                .filter(or_(view_specification_list.id.in_(sq) for sq in self.filters))\
                .order_by(view_specification_list.code).all()

        uk = request.args.get('uk')
        version = request.args.get('ver')

        if version:
            sp = view_specification_info.query.filter(view_specification_info.DQI_ID == uk,
                                                      view_specification_info.ver == version).all()
            s_ver = view_specification_versions.query.filter(view_specification_versions.uk == uk).all()
            return render_template('home/spec.html', sp=sp, specs=specs, s_ver=s_ver)
        elif not version and uk:
            sp = view_specification_info.query.filter(view_specification_info.DQI_ID == uk,
                                                      view_specification_info.ver == 'V31-12-5999 00:00:00').all()
            s_ver = view_specification_versions.query.filter(view_specification_versions.uk == uk).all()
            return render_template('home/spec.html', sp=sp, specs=specs, s_ver=s_ver)
        else:
            return render_template('home/spec.html', specs=specs)

