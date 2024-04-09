from sqlalchemy import Column, Integer, String, Numeric, Date, CLOB, Text, Sequence, DateTime, ARRAY
from datetime import datetime
from ..database import DqConnection


dq_connection = DqConnection('dqServer')
Base_dqps = dq_connection.Base_dqps

dq_connection = DqConnection('flaskDb')
Base_flask = dq_connection.Base_dqps


class user_w_role(Base_flask):
    __tablename__ = 'user_w_role'

    user_id = Column(String(255), primary_key=True)
    name = Column(String(255), unique=True)
    login = Column(String(255), unique=True)
    email = Column(String(64), unique=True)
    role = Column(ARRAY(String(255)), unique=True)

    def __init__(self, user_id=None, name=None, login=None, email=None, role=None):
        self.user_id = user_id
        self.name = name
        self.login = login
        self.email = email
        self.role = role

    def __repr__(self):
        return '<user_w_role %r %r %r %r %r>' % (self.user_id, self.name, self.login, self.email, self.role)


class view_specification_list(Base_dqps):
    __tablename__ = 'view_specification_list'
    __table_args__ = {"schema": "SSDQ"}
    code = Column(String(30))
    name = Column(String(255))
    description = Column(String(4000))
    id = Column(Integer, primary_key=True)

    def __init__(self, code=None, name=None, description=None, id=None):
        self.code = code
        self.name = name
        self.description = description
        self.id = id

    def __repr__(self):
        return '<view_specification_list %r %r %r %r>' % (self.code, self.name, self.description, self.id)


class view_specification_change(Base_dqps):
    __tablename__ = 'view_specification_change'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer)
    dqi_name = Column(String(4000))
    dq_description = Column(String(4000))
    dq_rule_description = Column(String(4000))
    level_name = Column(String(255))
    segment_id = Column(String(30))
    segment_type_name = Column(String(24))
    quality_type_name = Column(String(255))
    control_system_name = Column(String(255))
    data_system_name = Column(String(255))
    error_type_name = Column(String(100))
    metod1_full_name = Column(String(255))
    met_owner1_email = Column(String(255))
    owner1_name_full = Column(String(255))
    owner2_name_full = Column(String(255))
    owner3_name_full = Column(String(255))
    owner4_name_full = Column(String(255))
    cor_owner1_email = Column(String(255))
    cor_owner2_email = Column(String(255))
    cor_owner3_email = Column(String(255))
    cor_owner4_email = Column(String(255))
    b_0_01 = Column(Numeric)
    b_boundrymin = Column(Integer)
    b_boundrymin_p_1 = Column(Integer)
    b_boundrymax = Column(Integer)
    b_boundrymax_p_1 = Column(Integer)
    b_param_boundry = Column(String(255))
    schedule = Column(String(4000))
    alg_tech = Column(String(4000))
    c_terms = Column(String(4000))
    DQI_ID = Column(Integer, primary_key=True)
    control_name = Column(String(500))
    control_description = Column(String(4000))
    control_init = Column(String(400))
    client_dept_id = Column(String(100))
    release_number = Column(String(100))
    cr_number = Column(String(100))
    cor_date = Column(Date)
    move_date = Column(String(20))
    delay = Column(String(100))
    mail_type = Column(String(100))
    ror_flag = Column(String(1))
    mail_h_flag = Column(String(1))
    auto_inc_flag = Column(String(1))
    officer_uk = Column(Integer)
    officer_to_do = Column(String(4000))
    dq_object_uk = Column(Integer)
    wiki_link = Column(String(400))
    dq_status_uk = Column(Integer)
    dq_ftp_path_uk = Column(Integer)
    components_t_id = Column(String(100))
    customer_depts_t_id = Column(String(100))
    bi_depts_t_id = Column(String(100))
    source_query = Column(CLOB)
    alg = Column(String(4000))
    source_name = Column(String(100))
    cron = Column(String(100))
    ready_start_object_uk = Column(Integer)
    load_end = Column(String(100))
    ver = Column(String(50), primary_key=True)
    validto = Column(Date)
    steward_uk = Column(Integer)
    control_critical_flag = Column(String(1))
    crossdb_flag = Column(String(1))

    def __init__(self, uk=None, dqi_name=None, dq_description=None, dq_rule_description=None, level_name=None,
                 segment_id=None, segment_type_name=None, quality_type_name=None, control_system_name=None,
                 data_system_name=None, error_type_name=None, metod1_full_name=None, met_owner1_email=None,
                 owner1_name_full=None, owner2_name_full=None, owner3_name_full=None, owner4_name_full=None,
                 cor_owner1_email=None, cor_owner2_email=None, cor_owner3_email=None, cor_owner4_email=None,
                 b_0_01=None, b_boundrymin=None, b_boundrymin_p_1=None, b_boundrymax=None, b_boundrymax_p_1=None,
                 b_param_boundry=None, schedule=None, alg_tech=None, c_terms=None, dqi_id=None,
                 control_description=None, control_init=None, client_dept_id=None, release_number=None, cr_number=None,
                 cor_date=None, move_date=None, delay=None, mail_type=None, ror_flag=None, mail_h_flag=None,
                 auto_inc_flag=None, officer_uk=None, officer_to_do=None, dq_object_uk=None, wiki_link=None,
                 dq_status_uk=None, dq_ftp_path_uk=None, components_t_id=None, customer_depts_t_id=None,
                 bi_depts_t_id=None, source_query=None, alg=None, source_name=None, cron=None,
                 ready_start_object_uk=None, load_end=None, ver=None, validto=None, steward_uk=None,
                 control_critical_flag=None, crossdb_flag=None):
        self.uk = uk
        self.dqi_name = dqi_name
        self.dq_description = dq_description
        self.dq_rule_description = dq_rule_description
        self.level_name = level_name
        self.segment_id = segment_id
        self.segment_type_name = segment_type_name
        self.quality_type_name = quality_type_name
        self.control_system_name = control_system_name
        self.data_system_name = data_system_name
        self.error_type_name = error_type_name
        self.metod1_full_name = metod1_full_name
        self.met_owner1_email = met_owner1_email
        self.owner1_name_full = owner1_name_full
        self.owner2_name_full = owner2_name_full
        self.owner3_name_full = owner3_name_full
        self.owner4_name_full = owner4_name_full
        self.cor_owner1_email = cor_owner1_email
        self.cor_owner2_email = cor_owner2_email
        self.cor_owner3_email = cor_owner3_email
        self.cor_owner4_email = cor_owner4_email
        self.b_0_01 = b_0_01
        self.b_boundrymin = b_boundrymin
        self.b_boundrymin_p_1 = b_boundrymin_p_1
        self.b_boundrymax = b_boundrymax
        self.b_boundrymax_p_1 = b_boundrymax_p_1
        self.b_param_boundry = b_param_boundry
        self.schedule = schedule
        self.alg_tech = alg_tech
        self.c_terms = c_terms
        self.dqi_id = dqi_id
        self.control_description = control_description
        self.control_init = control_init
        self.client_dept_id = client_dept_id
        self.release_number = release_number
        self.cr_number = cr_number
        self.cor_date = cor_date
        self.move_date = move_date
        self.delay = delay
        self.mail_type = mail_type
        self.ror_flag = ror_flag
        self.mail_h_flag = mail_h_flag
        self.auto_inc_flag = auto_inc_flag
        self.officer_uk = officer_uk
        self.officer_to_do = officer_to_do
        self.dq_object_uk = dq_object_uk
        self.wiki_link = wiki_link
        self.dq_status_uk = dq_status_uk
        self.dq_ftp_path_uk = dq_ftp_path_uk
        self.components_t_id = components_t_id
        self.customer_depts_t_id = customer_depts_t_id
        self.bi_depts_t_id = bi_depts_t_id
        self.source_query = source_query
        self.alg = alg
        self.source_name = source_name
        self.cron = cron
        self.ready_start_object_uk = ready_start_object_uk
        self.load_end = load_end
        self.ver = ver
        self.validto = validto
        self.steward_uk = steward_uk
        self.control_critical_flag = control_critical_flag
        self.crossdb_flag = crossdb_flag

    def __repr__(self):
        return '<view_specification_change %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r ' \
               '%r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r ' \
               '%r %r %r %r %r %r>' % (
                self.uk, self.dqi_name, self.dq_description, self.dq_rule_description, self.level_name, self.segment_id,
                self.segment_type_name, self.quality_type_name, self.control_system_name, self.data_system_name,
                self.error_type_name, self.metod1_full_name, self.met_owner1_email,
                self.owner1_name_full, self.owner2_name_full, self.owner3_name_full, self.owner4_name_full,
                self.cor_owner1_email, self.cor_owner2_email, self.cor_owner3_email, self.cor_owner4_email,
                self.b_0_01, self.b_boundrymin, self.b_boundrymin_p_1,
                self.b_boundrymax, self.b_boundrymax_p_1, self.b_param_boundry, self.schedule, self.alg_tech,
                self.c_terms, self.control_name, self.control_description, self.control_init, self.client_dept_id,
                self.release_number, self.cr_number, self.cor_date, self.move_date, self.delay, self.mail_type,
                self.ror_flag, self.mail_h_flag, self.auto_inc_flag, self.officer_uk, self.officer_to_do,
                self.dq_object_uk, self.wiki_link, self.dq_status_uk, self.dq_ftp_path_uk, self.components_t_id,
                self.customer_depts_t_id, self.bi_depts_t_id, self.source_query, self.alg, self.source_name,
                self.cron, self.ready_start_object_uk, self.load_end, self.ver, self.validto, self.steward_uk,
                self.control_critical_flag, self.crossdb_flag)


class view_specification_versions(Base_dqps):
    __tablename__ = 'view_specification_versions'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, primary_key=True)
    ver = Column(String(50), primary_key=True)
    validto = Column(Date)

    def __init__(self, uk=None, ver=None, validto=None):
        self.uk = uk
        self.ver = ver
        self.validto = validto

    def __repr__(self):
        return '<view_specification_versions %r %r %r>' % (self.uk, self.ver, self.validto)


class view_specification_info(Base_dqps):
    __tablename__ = 'view_specification_info'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer)
    dqi_name = Column(String(4000))
    dq_description = Column(String(4000))
    dq_rule_description = Column(String(4000))
    level_name = Column(String(255))
    segment_id = Column(String(30))
    segment_type_name = Column(String(24))
    quality_type_name = Column(String(255))
    control_system_name = Column(String(255))
    data_system_name = Column(String(255))
    error_type_name = Column(String(100))
    metod1_full_name = Column(String(255))
    met_owner1_email = Column(String(255))
    owner1_name_full = Column(String(255))
    owner2_name_full = Column(String(255))
    owner3_name_full = Column(String(255))
    owner4_name_full = Column(String(255))
    cor_owner1_email = Column(String(255))
    cor_owner2_email = Column(String(255))
    cor_owner3_email = Column(String(255))
    cor_owner4_email = Column(String(255))
    b_0_01 = Column(Numeric)
    b_boundrymin = Column(Integer)
    b_boundrymin_p_1 = Column(Integer)
    b_boundrymax = Column(Integer)
    b_boundrymax_p_1 = Column(Integer)
    b_param_boundry = Column(String(255))
    schedule = Column(String(4000))
    alg_tech = Column(String(4000))
    c_terms = Column(String(4000))
    DQI_ID = Column(Integer, primary_key=True)
    ver = Column(String(50), primary_key=True)
    validto = Column(Date)

    def __init__(self, uk=None, dqi_name=None, dq_description=None, dq_rule_description=None, level_name=None,
                 segment_id=None, segment_type_name=None, quality_type_name=None,
                 control_system_name=None, data_system_name=None, error_type_name=None,
                 metod1_full_name=None, met_owner1_email=None, owner1_name_full=None, owner2_name_full=None,
                 owner3_name_full=None, owner4_name_full=None, cor_owner1_email=None, cor_owner2_email=None,
                 cor_owner3_email=None, cor_owner4_email=None, b_0_01=None, b_boundrymin=None, b_boundrymin_p_1=None,
                 b_boundrymax=None, b_boundrymax_p_1=None, b_param_boundry=None, schedule=None, alg_tech=None,
                 c_terms=None, dqi_id=None, ver=None, validto=None):
        self.uk = uk
        self.dqi_name = dqi_name
        self.dq_description = dq_description
        self.dq_rule_description = dq_rule_description
        self.level_name = level_name
        self.segment_id = segment_id
        self.segment_type_name = segment_type_name
        self.quality_type_name = quality_type_name
        self.control_system_name = control_system_name
        self.data_system_name = data_system_name
        self.error_type_name = error_type_name
        self.metod1_full_name = metod1_full_name
        self.met_owner1_email = met_owner1_email
        self.owner1_name_full = owner1_name_full
        self.owner2_name_full = owner2_name_full
        self.owner3_name_full = owner3_name_full
        self.owner4_name_full = owner4_name_full
        self.cor_owner1_email = cor_owner1_email
        self.cor_owner2_email = cor_owner2_email
        self.cor_owner3_email = cor_owner3_email
        self.cor_owner4_email = cor_owner4_email
        self.b_0_01 = b_0_01
        self.b_boundrymin = b_boundrymin
        self.b_boundrymin_p_1 = b_boundrymin_p_1
        self.b_boundrymax = b_boundrymax
        self.b_boundrymax_p_1 = b_boundrymax_p_1
        self.b_param_boundry = b_param_boundry
        self.schedule = schedule
        self.alg_tech = alg_tech
        self.c_terms = c_terms
        self.dqi_id = dqi_id
        self.ver = ver
        self.validto = validto

    def __repr__(self):
        return '<view_specification_info %r %r %r %r %r %r %r %r %r %r %r %r r %r %r %r %r %r %r %r %r %r %r %r %r %r %r ' \
               '%r %r %r %r %r %r>' % (
                self.uk, self.dqi_name, self.dq_description, self.dq_rule_description, self.level_name, self.segment_id,
                self.segment_type_name, self.quality_type_name, self.control_system_name, self.data_system_name,
                self.error_type_name, self.metod1_full_name, self.met_owner1_email, self.owner1_name_full,
                self.owner2_name_full, self.owner3_name_full, self.owner4_name_full,
                self.cor_owner1_email, self.cor_owner2_email, self.cor_owner3_email, self.cor_owner4_email,
                self.b_0_01, self.b_boundrymin, self.b_boundrymin_p_1, self.b_boundrymax, self.b_boundrymax_p_1,
                self.b_param_boundry, self.schedule, self.alg_tech, self.c_terms, self.ver, self.validto)


class dq_object_hdim(Base_dqps):
    __tablename__ = 'dq_object_hdim'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, Sequence('dq_object_hdim_seq', schema="SSDQ"), primary_key=True)
    base_name = Column(String(255))
    schema = Column(String(255))
    table_name = Column(String(255))
    description = Column(String(255))
    loaddq_flag = Column(String(1))
    reglament_uk = Column(Integer)
    entity_id = Column(Integer)
    deleted_flag = Column(String(1))
    validfrom = Column(Date)
    validto = Column(Date)

    def __init__(self, uk=None, base_name=None, schema=None, table_name=None, description=None, loaddq_flag=None,
                 reglament_uk=None, entity_id=None, deleted_flag="N", validfrom=datetime.now(),
                 validto=datetime.strptime('31.12.5999', '%d.%m.%Y')):
        self.uk = uk
        self.base_name = base_name
        self.schema = schema
        self.table_name = table_name
        self.description = description
        self.loaddq_flag = loaddq_flag
        self.reglament_uk = reglament_uk
        self.entity_id = entity_id
        self.deleted_flag = deleted_flag
        self.validfrom = validfrom
        self.validto = validto

    def __repr__(self):
        return '<dq_object_hdim %r %r %r %r %r %r %r %r %r %r %r>' % (
        self.uk, self.base_name, self.schema, self.table_name, self.description, self.loaddq_flag, self.reglament_uk,
        self.entity_id, self.deleted_flag, self.validfrom, self.validto)


class dq_user_hdim(Base_dqps):
    __tablename__ = 'dq_user_hdim'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, Sequence('dq_user_hdim_seq', schema="SSDQ"), primary_key=True)
    ad_login = Column(String(20))
    full_name = Column(String(255))
    email = Column(String(255))
    status = Column(String(64))
    deleted_flag = Column(String(1))
    validfrom = Column(Date)
    validto = Column(Date)

    def __init__(self, uk=None, ad_login=None, full_name=None, email=None, status=None, deleted_flag=None,
                 validfrom=None, validto=None):
        self.uk = uk
        self.ad_login = ad_login
        self.full_name = full_name
        self.email = email
        self.status = status
        self.deleted_flag = deleted_flag
        self.validfrom = validfrom
        self.validto = validto

    def __repr__(self):
        return '<dq_user_hdim %r %r %r %r %r>' % (
            self.uk, self.deleted_flag, self.full_name, self.ad_login, self.validto)


class dq_owner_sdim(Base_dqps):
    __tablename__ = 'dq_owner_sdim'
    __table_args__ = {"schema": "SSDQ"}
    id = Column(Integer, primary_key=True)
    owner_name_short = Column(String(20))
    owner_name_full = Column(String(255))
    email = Column(String(255))

    def __init__(self, id=None, owner_name_short=None, owner_name_full=None, email=None):
        self.id = id
        self.owner_name_short = owner_name_short
        self.owner_name_full = owner_name_full
        self.email = email

    def __repr__(self):
        return '<dq_owner_sdim %r %r %r %r>' % (
            self.id, self.owner_name_short, self.owner_name_full, self.email)


class dq_error_type_sdim(Base_dqps):
    __tablename__ = 'dq_error_type_sdim'
    __table_args__ = {"schema": "SSDQ"}
    id = Column(Integer, primary_key=True)
    error_type_name = Column(String(100))

    def __init__(self, id=None, error_type_name=None):
        self.id = id
        self.error_type_name = error_type_name

    def __repr__(self):
        return '<dq_error_type_sdim %r %r>' % (self.id, self.error_type_name)


class dq_quality_type_sdim(Base_dqps):
    __tablename__ = 'dq_quality_type_sdim'
    __table_args__ = {"schema": "SSDQ"}
    id = Column(Integer, primary_key=True)
    quality_type_name = Column(String(100))

    def __init__(self, id=None, quality_type_name=None):
        self.id = id
        self.quality_type_name = quality_type_name

    def __repr__(self):
        return '<dq_quality_type_sdim %r %r>' % (self.id, self.quality_type_name)


class dq_systems_sdim(Base_dqps):
    __tablename__ = 'dq_systems_sdim'
    __table_args__ = {"schema": "SSDQ"}
    id = Column(Integer, primary_key=True)
    system_name = Column(String(255))
    system_short = Column(String(255))

    def __init__(self, id=None, system_name=None, system_short=None):
        self.id = id
        self.system_name = system_name
        self.system_short = system_short

    def __repr__(self):
        return '<dq_systems_sdim %r %r %r>' % (self.id, self.system_name, self.system_short)


class dq_status_lov(Base_dqps):
    __tablename__ = 'dq_status_lov'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(4000))

    def __init__(self, uk=None, name=None, description=None):
        self.uk = uk
        self.name = name
        self.description = description

    def __repr__(self):
        return '<dq_status_lov %r %r %r>' % (self.uk, self.name, self.description)


class dq_bireport_department_lov(Base_dqps):
    __tablename__ = 'dq_bireport_department_lov'
    __table_args__ = {"schema": "SSDQ"}
    id = Column(String(46), primary_key=True)
    business_category = Column(String(48))
    dept_name = Column(String(93))

    def __init__(self, id=None, business_category=None, dept_name=None):
        self.id = id
        self.business_category = business_category
        self.dept_name = dept_name

    def __repr__(self):
        return '<dq_bireport_department_lov %r %r %r>' % (self.id, self.business_category, self.description)


class dq_ftp_path_ldim(Base_dqps):
    __tablename__ = 'dq_ftp_path_ldim'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, Sequence('dq_ftp_path_ldim_seq', schema="SSDQ"), primary_key=True)
    path_name = Column(String(255))
    host = Column(String(255))

    def __init__(self, uk=None, path_name=None, host=None):
        self.uk = uk
        self.path_name = path_name
        self.host = host

    def __repr__(self):
        return '<dq_ftp_path_ldim %r %r %r >' % (self.uk, self.path_name, self.host)


class customer_depts_t(Base_dqps):
    __tablename__ = 'customer_depts_t'
    __table_args__ = {"schema": "SSDQ"}
    id = Column(String(100), primary_key=True)
    department = Column(String(1000))
    disabled = Column(String(1))
    as_of_day = Column(Date)

    def __init__(self, id=None, department=None, disabled=None, as_of_day=None):
        self.id = id
        self.department = department
        self.disabled = disabled
        self.as_of_day = as_of_day

    def __repr__(self):
        return '<customer_depts_t %r %r %r %r >' % (self.id, self.department, self.disabled, self.as_of_day)


class bi_depts_t(Base_dqps):
    __tablename__ = 'bi_depts_t'
    __table_args__ = {"schema": "SSDQ"}
    id = Column(String(100), primary_key=True)
    department = Column(String(1000))
    disabled = Column(String(1))
    as_of_day = Column(Date)

    def __init__(self, id=None, department=None, disabled=None, as_of_day=None):
        self.id = id
        self.department = department
        self.disabled = disabled
        self.as_of_day = as_of_day

    def __repr__(self):
        return '<bi_depts_t %r %r %r %r >' % (self.id, self.department, self.disabled, self.as_of_day)


class components_t(Base_dqps):
    __tablename__ = 'components_t'
    __table_args__ = {"schema": "SSDQ"}
    project = Column(String(100))
    component_id = Column(String(100), primary_key=True)
    component_name = Column(String(2000))
    component_lead = Column(String(100))
    archived = Column(String(1))
    as_of_day = Column(Date)

    def __init__(self, project=None, component_id=None, component_name=None, component_lead=None, archived=None,
                 as_of_day=None):
        self.project = project
        self.component_id = component_id
        self.component_name = component_name
        self.component_lead = component_lead
        self.archived = archived
        self.as_of_day = as_of_day

    def __repr__(self):
        return '<components_t %r %r %r %r %r %r>' % (
            self.project, self.component_id, self.component_name, self.component_lead, self.archived, self.as_of_day)


class dq_request_hdim(Base_dqps):
    __tablename__ = 'dq_request_hdim'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, primary_key=True)
    terms = Column(String(4000))
    owner = Column(String(50))
    validfrom = Column(Date)
    validto = Column(Date, primary_key=True)
    deleted_flag = Column(String(1))
    default_flag = Column(String(1))
    user_login = Column(String(20))
    user_name = Column(String(100))

    def __init__(self, uk=None, terms=None, owner=None, validfrom=None,
                 validto=datetime.strptime('31.12.5999', '%d.%m.%Y'), deleted_flag="N",
                 default_flag="N", user_login=None, user_name=None):
        self.uk = uk
        self.terms = terms
        self.owner = owner
        self.validfrom = validfrom
        self.validto = validto
        self.deleted_flag = deleted_flag
        self.default_flag = default_flag
        self.user_login = user_login
        self.user_name = user_name

    def __repr__(self):
        return '<dq_request_hdim %r %r %r %r %r %r %r %r %r >' % (
            self.uk, self.terms, self.owner, self.validfrom, self.validto, self.deleted_flag, self.default_flag,
            self.user_login, self.user_name)


class dq_source_hdim(Base_dqps):
    __tablename__ = 'dq_source_hdim'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, primary_key=True)
    name = Column(String(255))
    connection_type = Column(String(255))
    schema = Column(String(255))
    host = Column(String(255))
    port = Column(Integer)
    description = Column(String(4000))
    validfrom = Column(Date)
    validto = Column(Date)
    deleted_flag = Column(String(1))
    default_flag = Column(String(1))

    def __init__(self, uk=None, name=None, connection_type=None, schema=None, host=None, port=None, description=None,
                 validfrom=None, validto=None, deleted_flag=None, default_flag=None):
        self.uk = uk
        self.name = name
        self.connection_type = connection_type
        self.schema = schema
        self.host = host
        self.port = port
        self.description = description
        self.validfrom = validfrom
        self.validto = validto
        self.deleted_flag = deleted_flag
        self.default_flag = default_flag

    def __repr__(self):
        return '<dq_source_hdim %r %r %r %r %r %r %r %r %r %r %r >' % (
            self.uk, self.name, self.connection_type, self.schema, self.host, self.port, self.description,
            self.validfrom,
            self.validto, self.deleted_flag, self.default_flag)


class dq_monitoring_view(Base_dqps):
    __tablename__ = 'dq_monitoring_view'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, primary_key=True)
    name = Column(String(4000))
    object_name = Column(String(255))
    officer_name = Column(String(255))
    status_name = Column(String(100))
    run_id = Column(Integer)
    last_start = Column(Date)
    last_result = Column(String(255))
    overflow_start = Column(Date)
    overflow_result = Column(String(255))
    description = Column(String(255))
    rule_description = Column(String(4000))
    defect = Column(String(20))
    proj = Column(String(4000))
    overflow_run_id = Column(Integer)
    control_type = Column(String(255))
    need_act = Column(String(3))
    dept_name = Column(String(200))
    dqi_id = Column(String(20), primary_key=True)
    dq_status_uk = Column(Integer)

    def __init__(self, uk=None, name=None, object_name=None, officer_name=None, status_name=None,
                 run_id=None, last_start=None, last_result=None, overflow_start=None, overflow_result=None,
                 description=None, rule_description=None, defect=None, proj=None, overflow_run_id=None,
                 control_type=None, need_act=None, dept_name=None, dqi_id=None, dq_status_uk=None):
        self.uk = uk
        self.name = name
        self.object_name = object_name
        self.officer_name = officer_name
        self.status_name = status_name
        self.run_id = run_id
        self.last_start = last_start
        self.last_result = last_result
        self.overflow_start = overflow_start
        self.overflow_result = overflow_result
        self.description = description
        self.rule_description = rule_description
        self.defect = defect
        self.proj = proj
        self.overflow_run_id = overflow_run_id
        self.control_type = control_type
        self.need_act = need_act
        self.dept_name = dept_name
        self.dqi_id = dqi_id
        self.dq_status_uk = dq_status_uk

    def __repr__(self):
        return '<dq_monitoring_view %r >' % self.uk


class dq_sql_detail_ldim(Base_dqps):
    __tablename__ = 'dq_sql_detail_ldim'
    __table_args__ = {"schema": "SSDQ"}
    dq_request_uk = Column(Integer, primary_key=True)
    sql_query = Column(Text)
    validfrom = Column(Date)
    validto = Column(Date)
    user_login = Column(String(20))
    user_name = Column(String(100))

    def __init__(self, dq_request_uk=None, sql_query=None, validfrom=None,
                 validto=datetime.strptime('31.12.5999', '%d.%m.%Y'), user_login=None, user_name=None):
        self.dq_request_uk = dq_request_uk
        self.sql_query = sql_query
        self.validfrom = validfrom
        self.validto = validto
        self.user_login = user_login
        self.user_name = user_name

    def __repr__(self):
        return '<dq_sql_detail_ldim %r %r %r %r %r %r >' % (
            self.dq_request_uk, self.sql_query, self.validfrom, self.validto, self.user_login, self.user_name)


class dq_detail_agg(Base_dqps):
    __tablename__ = 'dq_detail_agg'
    __table_args__ = {"schema": "SSDQ"}
    description = Column(String(255))
    dq_control_uk = Column(Integer, primary_key=True)
    end_time = Column(Date)
    mistake_count = Column(Integer)
    report_date = Column(Date)
    start_time = Column(Date)
    max_result = Column(Integer)
    pm_workflow_run_id = Column(String(255), primary_key=True)
    script_finished = Column(String(1))
    error_flag = Column(String(1))
    out_of_margins_flag = Column(String(1))
    workflow_name = Column(String(155))
    error_name = Column(String(250))
    report_mistake_count = Column(Integer)
    read_rows_count = Column(Integer)

    def __init__(self, description=None, dq_control_uk=None, end_time=None, mistake_count=None, report_date=None,
                 start_time=None, max_result=None, pm_workflow_run_id=None, script_finished=None, error_flag=None,
                 out_of_margins_flag=None, workflow_name=None, error_name=None, report_mistake_count=None,
                 read_rows_count=None):
        self.description = description
        self.dq_control_uk = dq_control_uk
        self.end_time = end_time
        self.mistake_count = mistake_count
        self.report_date = report_date
        self.start_time = start_time
        self.max_result = max_result
        self.pm_workflow_run_id = pm_workflow_run_id
        self.script_finished = script_finished
        self.error_flag = error_flag
        self.out_of_margins_flag = out_of_margins_flag
        self.workflow_name = workflow_name
        self.error_name = error_name
        self.report_mistake_count = report_mistake_count
        self.read_rows_count = read_rows_count

    def __repr__(self):
        return '<dq_detail_agg %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>' % (
            self.description, self.dq_control_uk, self.end_time, self.mistake_count, self.report_date, self.start_time,
            self.max_result, self.pm_workflow_run_id, self.script_finished, self.error_flag, self.out_of_margins_flag,
            self.workflow_name, self.error_name, self.report_mistake_count, self.read_rows_count)


class dq_alerting_hdim(Base_dqps):
    __tablename__ = 'dq_alerting_hdim'
    __table_args__ = {"schema": "SSDQ"}
    dq_request_uk = Column(Integer, primary_key=True)
    user_uk = Column(Integer, primary_key=True)
    dq_mail_attachtype_uk = Column(Integer, primary_key=True)
    validfrom = Column(Date)
    validto = Column(Date)
    deleted_flag = Column(String(1))

    def __init__(self, dq_request_uk=None, user_uk=None, dq_mail_attachtype_uk=None, validfrom=None,
                 validto=datetime.strptime('31.12.5999', '%d.%m.%Y'),
                 deleted_flag="N"):
        self.dq_request_uk = dq_request_uk
        self.user_uk = user_uk
        self.dq_mail_attachtype_uk = dq_mail_attachtype_uk
        self.validfrom = validfrom
        self.validto = validto
        self.deleted_flag = deleted_flag

    def __repr__(self):
        return '<dq_alerting_hdim %r %r %r %r %r %r>' % (
            self.dq_request_uk, self.user_uk, self.dq_mail_attachtype_uk, self.validfrom, self.validto,
            self.deleted_flag)


class dq_dag_hdim(Base_dqps):
    __tablename__ = 'dq_dag_hdim'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(String(100), Sequence('dq_dag_hdim_seq', schema="SSDQ"), primary_key=True)
    dq_request_uk = Column(Integer)
    sql = Column(Text)
    alg = Column(Text)
    cron = Column(String(100))
    ready_start_object_uk = Column(Integer)
    load_end = Column(String(100))
    source = Column(String(100))
    validfrom = Column(Date)
    validto = Column(Date)
    deleted_flag = Column(String(1))
    crossdb_flag = Column(String(1))

    def __init__(self, uk=None, dq_request_uk=None, sql=None, alg=None,
                 cron=None, ready_start_object_uk=None, source=None, load_end=None, validfrom=None,
                 validto=datetime.strptime('31.12.5999', '%d.%m.%Y'), deleted_flag="N", crossdb_flag="N"):
        self.uk = uk
        self.dq_request_uk = dq_request_uk
        self.alg = alg
        self.sql = sql
        self.cron = cron
        self.ready_start_object_uk = ready_start_object_uk
        self.load_end = load_end
        self.source = source
        self.validfrom = validfrom
        self.validto = validto
        self.deleted_flag = deleted_flag
        self.crossdb_flag = crossdb_flag

    def __repr__(self):
        return '<dq_dag_hdim %r %r %r %r %r %r %r %r %r %r %r %r>' % (
            self.uk, self.dq_request_uk, self.sql, self.alg, self.cron,
            self.ready_start_object_uk, self.source, self.load_end, self.validfrom, self.validto, self.deleted_flag,
            self.crossdb_flag)


class dq_dag_crossdb_hdim(Base_dqps):
    __tablename__ = 'dq_dag_crossdb_hdim'
    __table_args__ = {"schema": "SSDQ"}
    dq_request_uk = Column(Integer, primary_key=True)
    sql = Column(Text)
    source = Column(String(100), primary_key=True)
    custom_source_name = Column(String(100), primary_key=True)
    main_sql = Column(String(1), primary_key=True)
    validfrom = Column(Date)
    validto = Column(Date, primary_key=True)
    deleted_flag = Column(String(1), primary_key=True)

    def __init__(self, dq_request_uk=None, sql=None, source=None, custom_source_name=None, main_sql=None,
                 validfrom=None, validto=None, deleted_flag=None):
        self.dq_request_uk = dq_request_uk
        self.sql = sql
        self.source = source
        self.custom_source_name = custom_source_name
        self.main_sql = main_sql
        self.validfrom = validfrom
        self.validto = validto
        self.deleted_flag = deleted_flag

    def __repr__(self):
        return '<dq_dag_crossdb_hdim %r %r %r %r %r %r %r %r>' % (
            self.dq_request_uk, self.sql, self.source, self.custom_source_name, self.main_sql, self.validfrom,
            self.validto, self.deleted_flag)


class dq_spec_hdim(Base_dqps):
    __tablename__ = 'dq_spec_hdim'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, Sequence('dq_spec_hdim_seq', schema="SSDQ"), primary_key=True)
    dq_request_uk = Column(Integer)
    dqi_code = Column(String(200))
    segment_id = Column(String(200))
    ind_system_id = Column(Integer)
    data_system_id = Column(Integer)
    quality_type_id = Column(Integer)
    ind_version = Column(String(500))
    c_terms = Column(String(4000))
    alg_business = Column(String(4000))
    data_layer = Column(String(200))
    criterius = Column(String(4000))
    boundrymax_min = Column(Integer)
    boundrymed_max = Column(Integer)
    boundrymed_min = Column(Integer)
    boundrymin_max = Column(Integer)
    alg_tech = Column(String(4000))
    schedule = Column(String(4000))
    error_type_id = Column(Integer)
    met_owner1_id = Column(Integer)
    met_owner2_id = Column(Integer)
    met_owner3_id = Column(Integer)
    met_owner4_id = Column(Integer)
    met_owner5_id = Column(Integer)
    met_owner1_email = Column(String(200))
    met_owner2_email = Column(String(200))
    met_owner3_email = Column(String(200))
    met_owner4_email = Column(String(200))
    met_owner5_email = Column(String(200))
    cor_owner1_id = Column(Integer)
    cor_owner2_id = Column(Integer)
    cor_owner3_id = Column(Integer)
    cor_owner4_id = Column(Integer)
    cor_owner5_id = Column(Integer)
    cor_owner6_id = Column(Integer)
    cor_owner7_id = Column(Integer)
    cor_owner8_id = Column(Integer)
    cor_owner9_id = Column(Integer)
    cor_owner10_id = Column(Integer)
    cor_owner1_email = Column(String(200))
    cor_owner2_email = Column(String(200))
    cor_owner3_email = Column(String(200))
    cor_owner4_email = Column(String(200))
    cor_owner5_email = Column(String(200))
    cor_owner6_email = Column(String(200))
    cor_owner7_email = Column(String(200))
    cor_owner8_email = Column(String(200))
    cor_owner9_email = Column(String(200))
    cor_owner10_email = Column(String(200))
    validfrom = Column(Date)
    validto = Column(Date)
    deleted_flag = Column(String(1))
    default_flag = Column(String(1))
    user_login = Column(String(20))
    user_name = Column(String(100))

    def __init__(self, uk=None, dq_request_uk=None, dqi_code=None, segment_id=None, ind_system_id=None,
                 data_system_id=None, quality_type_id=None, ind_version=None,
                 c_terms=None, alg_business=None, data_layer=None, criterius=None,
                 boundrymax_min=None, boundrymed_max=None, boundrymed_min=None, boundrymin_max=None, alg_tech=None,
                 schedule=None, error_type_id=None, met_owner1_id=None, met_owner2_id=0, met_owner3_id=0,
                 met_owner4_id=0, met_owner5_id=0, met_owner1_email=None, met_owner2_email=None, met_owner3_email=None,
                 met_owner4_email=None, met_owner5_email=None, cor_owner1_id=None, cor_owner2_id=None,
                 cor_owner3_id=None, cor_owner4_id=None, cor_owner5_id=None, cor_owner6_id=None, cor_owner7_id=None,
                 cor_owner8_id=None, cor_owner9_id=None, cor_owner10_id=None, cor_owner1_email=None,
                 cor_owner2_email=None, cor_owner3_email=None, cor_owner4_email=None, cor_owner5_email=None,
                 cor_owner6_email=None, cor_owner7_email=None, cor_owner8_email=None, cor_owner9_email=None,
                 cor_owner10_email=None, validfrom=None, validto=datetime.strptime('31.12.5999', '%d.%m.%Y'),
                 deleted_flag='N', default_flag='N', user_login=None, user_name=None):
        self.uk = uk
        self.dq_request_uk = dq_request_uk
        self.dqi_code = dqi_code
        self.segment_id = segment_id
        self.ind_system_id = ind_system_id
        self.data_system_id = data_system_id
        self.quality_type_id = quality_type_id
        self.ind_version = ind_version
        self.c_terms = c_terms
        self.alg_business = alg_business
        self.data_layer = data_layer
        self.criterius = criterius
        self.boundrymax_min = boundrymax_min
        self.boundrymed_max = boundrymed_max
        self.boundrymed_min = boundrymed_min
        self.boundrymin_max = boundrymin_max
        self.alg_tech = alg_tech
        self.schedule = schedule
        self.error_type_id = error_type_id
        self.met_owner1_id = met_owner1_id
        self.met_owner2_id = met_owner2_id
        self.met_owner3_id = met_owner3_id
        self.met_owner4_id = met_owner4_id
        self.met_owner5_id = met_owner5_id
        self.met_owner1_email = met_owner1_email
        self.met_owner2_email = met_owner2_email
        self.met_owner3_email = met_owner3_email
        self.met_owner4_email = met_owner4_email
        self.met_owner5_email = met_owner5_email
        self.cor_owner1_id = cor_owner1_id
        self.cor_owner2_id = cor_owner2_id
        self.cor_owner3_id = cor_owner3_id
        self.cor_owner4_id = cor_owner4_id
        self.cor_owner5_id = cor_owner5_id
        self.cor_owner6_id = cor_owner6_id
        self.cor_owner7_id = cor_owner7_id
        self.cor_owner8_id = cor_owner8_id
        self.cor_owner9_id = cor_owner9_id
        self.cor_owner10_id = cor_owner10_id
        self.cor_owner1_email = cor_owner1_email
        self.cor_owner2_email = cor_owner2_email
        self.cor_owner3_email = cor_owner3_email
        self.cor_owner4_email = cor_owner4_email
        self.cor_owner5_email = cor_owner5_email
        self.cor_owner6_email = cor_owner6_email
        self.cor_owner7_email = cor_owner7_email
        self.cor_owner8_email = cor_owner8_email
        self.cor_owner9_email = cor_owner9_email
        self.cor_owner10_email = cor_owner10_email
        self.validfrom = validfrom
        self.validto = validto
        self.deleted_flag = deleted_flag
        self.default_flag = default_flag
        self.user_login = user_login
        self.user_name = user_name

    def __repr__(self):
        return '<dq_spec_hdim %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r' \
               '%r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>' % (
            self.uk, self.dq_request_uk, self.dqi_code, self.segment_id, self.ind_system_id,
            self.data_system_id, self.quality_type_id, self.ind_version, self.c_terms,
            self.alg_business, self.data_layer, self.criterius, self.boundrymax_min, self.boundrymed_max,
            self.boundrymed_min, self.boundrymin_max, self.alg_tech, self.schedule, self.error_type_id,
            self.met_owner1_id, self.met_owner2_id, self.met_owner3_id, self.met_owner4_id, self.met_owner5_id,
            self.met_owner1_email, self.met_owner2_email, self.met_owner3_email, self.met_owner4_email,
            self.met_owner5_email, self.cor_owner1_id, self.cor_owner2_id, self.cor_owner3_id,
            self.cor_owner4_id, self.cor_owner5_id, self.cor_owner6_id, self.cor_owner7_id, self.cor_owner8_id,
            self.cor_owner9_id, self.cor_owner10_id, self.cor_owner1_email, self.cor_owner2_email,
            self.cor_owner3_email, self.cor_owner4_email, self.cor_owner5_email, self.cor_owner6_email,
            self.cor_owner7_email, self.cor_owner8_email, self.cor_owner9_email, self.cor_owner10_email, self.validfrom,
            self.validto, self.deleted_flag, self.default_flag, self.user_login, self.user_name)


class dq_control_param_hdim(Base_dqps):
    __tablename__ = 'dq_control_param_hdim'
    __table_args__ = {"schema": "SSDQ"}
    uk = Column(Integer, Sequence('dq_control_param_hdim_seq', schema="SSDQ"), primary_key=True)
    dq_request_uk = Column(Integer)
    control_name = Column(String(500))
    control_description = Column(String(4000))
    control_init = Column(String(400))
    client_dept_id = Column(String(100))
    release_numeric = Column(String(100))
    cr_numeric = Column(String(100))
    cor_date = Column(Date)
    move_date = Column(String(20))
    delay = Column(String(100))
    mail_type = Column(String(100))
    ror_flag = Column(String(1))
    mail_h_flag = Column(String(1))
    auto_inc_flag = Column(String(1))
    officer_uk = Column(Integer)
    officer_to_do = Column(String(4000))
    dq_object_uk = Column(Integer)
    wiki_link = Column(String(400))
    dq_status_uk = Column(Integer)
    dq_ftp_path_uk = Column(Integer)
    customer_depts_t_id = Column(String(100))
    bi_depts_t_id = Column(String(100))
    components_t_id = Column(String(100))
    validfrom = Column(Date)
    validto = Column(Date, primary_key=True)
    deleted_flag = Column(String(1))
    default_flag = Column(String(1))
    user_login = Column(String(20))
    release_number = Column(String(100))
    cr_number = Column(String(100))
    user_name = Column(String(100))
    steward_uk = Column(Integer)
    control_critical_flag = Column(String(1))

    def __init__(self, uk=None, dq_request_uk=None, control_name=None, control_description=None, control_init=None,
                 client_dept_id=None, release_numeric=None, cr_numeric=None, cor_date=None,
                 move_date=None, delay=None, mail_type=None, ror_flag='N',
                 mail_h_flag='N', auto_inc_flag='N', officer_uk=None, officer_to_do=None,
                 dq_object_uk=None, wiki_link=None, dq_status_uk=None, dq_ftp_path_uk=None,
                 customer_depts_t_id=None, bi_depts_t_id=None, components_t_id=None, validfrom=None,
                 validto=datetime.strptime('31.12.5999', '%d.%m.%Y'), deleted_flag='N', default_flag='N',
                 user_login=None,
                 release_number=None, cr_number=None, user_name=None, steward_uk=None, control_critical_flag=None):
        self.uk = uk
        self.dq_request_uk = dq_request_uk
        self.control_name = control_name
        self.control_description = control_description
        self.control_init = control_init
        self.client_dept_id = client_dept_id
        self.release_numeric = release_numeric
        self.cr_numeric = cr_numeric
        self.cor_date = cor_date
        self.move_date = move_date
        self.delay = delay
        self.mail_type = mail_type
        self.ror_flag = ror_flag
        self.mail_h_flag = mail_h_flag
        self.auto_inc_flag = auto_inc_flag
        self.officer_uk = officer_uk
        self.officer_to_do = officer_to_do
        self.dq_object_uk = dq_object_uk
        self.wiki_link = wiki_link
        self.dq_status_uk = dq_status_uk
        self.dq_ftp_path_uk = dq_ftp_path_uk
        self.customer_depts_t_id = customer_depts_t_id
        self.bi_depts_t_id = bi_depts_t_id
        self.components_t_id = components_t_id
        self.validfrom = validfrom
        self.validto = validto
        self.deleted_flag = deleted_flag
        self.default_flag = default_flag
        self.user_login = user_login
        self.release_number = release_number
        self.cr_number = cr_number
        self.user_name = user_name
        self.steward_uk = steward_uk
        self.control_critical_flag = control_critical_flag

    def __repr__(self):
        return '<dq_control_param_hdim %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>' % (
            self.uk, self.dq_request_uk, self.control_name, self.control_description, self.control_init,
            self.client_dept_id,
            self.release_numeric, self.cr_numeric, self.cor_date, self.move_date, self.delay, self.mail_type,
            self.ror_flag, self.mail_h_flag, self.auto_inc_flag, self.officer_uk, self.officer_to_do, self.dq_object_uk,
            self.wiki_link, self.dq_status_uk, self.dq_ftp_path_uk, self.customer_depts_t_id, self.bi_depts_t_id,
            self.components_t_id,
            self.validfrom, self.validto, self.deleted_flag, self.default_flag, self.user_login, self.release_number,
            self.cr_number, self.user_name, self.steward_uk, self.control_critical_flag)


class dq_segment_sdim(Base_dqps):
    __tablename__ = 'dq_segment_sdim'
    __table_args__ = {"schema": "SSDQ"}
    id = Column(Integer, Sequence('dq_object_hdim_seq', schema="SSDQ"), primary_key=True)
    name = Column(String(255))
    description = Column(String(4000))
    deleted_flag = Column(String(1))

    def __init__(self, id=None, name=None, description=None, deleted_flag=None):
        self.id = id
        self.name = name
        self.description = description
        self.deleted_flag = deleted_flag

    def __repr__(self):
        return '<dq_segment_sdim %r %r %r %r>' % (self.id, self.name, self.description, self.deleted_flag)


class user_roles(Base_flask):
    __tablename__ = 'user_roles'

    user_id = Column(String(255), primary_key=True)
    role_id = Column(Integer)

    def __init__(self, user_id=None, role_id=None):
        self.user_id = user_id
        self.role_id = role_id

    def __repr__(self):
        return '<user_roles %r %r>' % (self.user_id, self.role_id)


class view_controls_count(Base_dqps):
    __tablename__ = 'view_controls_count'
    __table_args__ = {"schema": "SSDQ"}

    all_cnt = Column(Integer, primary_key=True)
    exp_cnt = Column(Integer, primary_key=True)
    cncl_cnt = Column(Integer, primary_key=True)
    act_cnt = Column(Integer, primary_key=True)

    def __init__(self, all_cnt=None, exp_cnt=None, cncl_cnt=None, act_cnt=None):
        self.all_cnt = all_cnt
        self.exp_cnt = exp_cnt
        self.cncl_cnt = cncl_cnt
        self.act_cnt = act_cnt

    def __repr__(self):
        return '<view_controls_count %r %r %r %r>' % (self.all_cnt, self.exp_cnt, self.cncl_cnt, self.act_cnt)


class view_all_controls_bydate(Base_dqps):
    __tablename__ = 'view_all_controls_bydate'
    __table_args__ = {"schema": "SSDQ"}

    thedate = Column(Date, primary_key=True)
    uk = Column(Integer, primary_key=True)
    dq_status_uk = Column(Integer)
    officer_uk = Column(Integer)

    def __init__(self, thedate=None, uk=None, dq_status_uk=None, officer_uk=None):
        self.thedate = thedate
        self.uk = uk
        self.dq_status_uk = dq_status_uk
        self.officer_uk = officer_uk

    def __repr__(self):
        return '<view_all_controls_bydate %r %r %r %r>' % (self.thedate, self.uk, self.dq_status_uk, self.officer_uk)


class view_controls_error(Base_dqps):
    __tablename__ = 'view_controls_error'
    __table_args__ = {"schema": "SSDQ"}

    report_date = Column(Date, primary_key=True)
    uk = Column(Integer)
    officer_uk = Column(Integer)
    segment_id = Column(Integer)

    def __init__(self, report_date=None, uk=None, officer_uk=None, segment_id=None):
        self.report_date = report_date
        self.uk = uk
        self.officer_uk = officer_uk
        self.segment_id = segment_id

    def __repr__(self):
        return '<view_controls_error %r %r %r %r>' % (
            self.report_date, self.uk, self.officer_uk, self.segment_id)


class Log(Base_flask):
    __tablename__ = 'ssdq_logs'

    id = Column(Integer, primary_key=True)
    logger = Column(String(100))
    level = Column(String(100))
    trace = Column(String(4096))
    login = Column(String(20))
    msg = Column(String(4096))
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, logger=None, level=None, trace=None, login=None, msg=None, created_at=None):
        self.logger = logger
        self.level = level
        self.trace = trace
        self.login = login
        self.msg = msg
        self.created_at = created_at

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return '<ssdq_logs: %s - %s>' % (self.created_at.strftime('%m%d%Y-%H:%M:%S'), self.msg[:50])
