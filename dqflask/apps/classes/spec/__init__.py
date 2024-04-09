class Spec:
    def __init__(self, user_login, user_name, segment_id=None, ind_system_id=None, data_system_id=None,
                 quality_type_id=None, c_terms=None, alg_business=None, data_layer=None,
                 criterius=None, boundrymin_max=None, boundrymed_min=None, boundrymed_max=None, boundrymax_min=None,
                 alg_tech=None, schedule=None, error_type_id=None, met_owner1=None, cor_owner1=None, cor_owner2=None,
                 cor_owner3=None, cor_owner4=None, control_name=None, control_description=None, control_init=None,
                 client_dept_id=None, release_number=None, cr_number=None, cor_date=None, move_date=None, delay=None,
                 mail_type=None, ror_flag=None, mail_h_flag=None, auto_inc_flag=None, officer_uk=None, steward_uk=None,
                 officer_to_do=None, dq_object_uk=None, wiki_link=None, dq_status_uk=None, dq_ftp_path_uk=None,
                 customer_depts_t_id=None, control_type=None, components_t_id=None,
                 schedule_cron=None, sql_query=None, source=None, alg=None, detail_query=None,
                 control_critical_flag=None, alerting=None, teams=None,
                 request_uk=None, main_sql=None, src_count=None, check_crossdb=None):
        self.user_login = user_login
        self.user_name = user_name
        self.request_uk = request_uk

        # First page
        self.segment_id = segment_id
        self.ind_system_id = ind_system_id
        self.data_system_id = data_system_id
        self.quality_type_id = quality_type_id
        self.c_terms = c_terms
        self.alg_business = alg_business
        self.data_layer = data_layer
        self.criterius = criterius
        self.boundrymin_max = boundrymin_max
        self.boundrymed_min = boundrymed_min
        self.boundrymed_max = boundrymed_max
        self.boundrymax_min = boundrymax_min
        self.alg_tech = alg_tech
        self.schedule = schedule
        self.error_type_id = error_type_id
        self.met_owner1 = met_owner1
        self.cor_owner1 = cor_owner1
        self.cor_owner2 = cor_owner2
        self.cor_owner3 = cor_owner3
        self.cor_owner4 = cor_owner4

        # Second page
        self.control_name = control_name
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
        self.steward_uk = steward_uk
        self.officer_to_do = officer_to_do
        self.dq_object_uk = dq_object_uk
        self.wiki_link = wiki_link
        self.dq_status_uk = dq_status_uk
        self.dq_ftp_path_uk = dq_ftp_path_uk
        self.customer_depts_t_id = customer_depts_t_id
        self.control_type = control_type
        self.components_t_id = components_t_id
        self.teams = teams

        # Third page
        self.schedule_cron = schedule_cron
        self.sql_query = sql_query
        self.source = source
        self.alg = alg
        self.detail_query = detail_query
        self.control_critical_flag = control_critical_flag
        self.alerting = alerting

        # Cross DB attributes
        self.check_crossdb = check_crossdb
        self.src_name_list = []
        self.custom_name_list = []
        self.sql_list = []
        self.main_sql = main_sql
        self.src_count = src_count
