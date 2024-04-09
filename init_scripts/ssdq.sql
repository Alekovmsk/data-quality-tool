--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER DATABASE ssdq OWNER TO ssdq_admin;

\connect ssdq

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: SSDQ; Type: SCHEMA; Schema: -; Owner: ssdq_admin
--

CREATE SCHEMA "SSDQ";


ALTER SCHEMA "SSDQ" OWNER TO ssdq_admin;

--
-- Name: SCHEMA "SSDQ"; Type: COMMENT; Schema: -; Owner: ssdq_admin
--

COMMENT ON SCHEMA "SSDQ" IS 'Self-service Data Quality';


--
-- Name: get_mail_header(numeric); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".get_mail_header(in_dq_control_uk numeric) RETURNS character
    LANGUAGE plpgsql
    AS $$
  BEGIN
    IF in_dq_control_uk!=0 THEN 
    RETURN 'Добрый день!'||chr(13)||chr(13)||
           'В рамках процесса выявления и исправления данных в системе Loan Manager отработали контроли,  имеются ошибки.'||chr(13)||
           'Перечень клиентов/сделок/расчетов, по которым обнаружены ошибки, в прилагаемом файле.'||chr(13)||
           'Ответственные за исправление указаны в колонке "Сотруд., ответ.за испр.данных".'||chr(13)||
           'При возникновении вопросов можно обращаться к Офицеру КД контроля, Хитрикову Андрею (для сделок КБ), Пальтову Д (для сделок СБ).';
    END IF;
  END;
  $$;


ALTER FUNCTION "SSDQ".get_mail_header(in_dq_control_uk numeric) OWNER TO ssdq_admin;

--
-- Name: nvl(date, date); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".nvl(var1 date, var2 date) RETURNS date
    LANGUAGE plpgsql
    AS $$
begin
return case when var1 is null then var2 else var1 end;
end;
$$;


ALTER FUNCTION "SSDQ".nvl(var1 date, var2 date) OWNER TO ssdq_admin;

--
-- Name: nvl(integer, integer); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".nvl(var1 integer, var2 integer) RETURNS integer
    LANGUAGE plpgsql
    AS $$
begin
return case when var1 is null then var2 else var1 end;
end;
$$;


ALTER FUNCTION "SSDQ".nvl(var1 integer, var2 integer) OWNER TO ssdq_admin;

--
-- Name: nvl(numeric, numeric); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".nvl(var1 numeric, var2 numeric) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
begin
return case when var1 is null then var2 else var1 end;
end;
$$;


ALTER FUNCTION "SSDQ".nvl(var1 numeric, var2 numeric) OWNER TO ssdq_admin;

--
-- Name: nvl(text, text); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".nvl(var1 text, var2 text) RETURNS text
    LANGUAGE plpgsql
    AS $$
begin
return case when var1 is null then var2 else var1 end;
end;
$$;


ALTER FUNCTION "SSDQ".nvl(var1 text, var2 text) OWNER TO ssdq_admin;

--
-- Name: nvl(timestamp without time zone, timestamp without time zone); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".nvl(var1 timestamp without time zone, var2 timestamp without time zone) RETURNS timestamp without time zone
    LANGUAGE plpgsql
    AS $$
begin
return case when var1 is null then var2 else var1 end;
end;
$$;


ALTER FUNCTION "SSDQ".nvl(var1 timestamp without time zone, var2 timestamp without time zone) OWNER TO ssdq_admin;

--
-- Name: nvl(character varying, character varying); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".nvl(var1 character varying, var2 character varying) RETURNS character varying
    LANGUAGE plpgsql
    AS $$
begin
return case when var1 is null then var2 else var1 end;
end;
$$;


ALTER FUNCTION "SSDQ".nvl(var1 character varying, var2 character varying) OWNER TO ssdq_admin;

--
-- Name: regexp_substr(text, text); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".regexp_substr(str text, pattern text) RETURNS text
    LANGUAGE sql
    AS $$
SELECT (regexp_matches(str, pattern))[1]
$$;


ALTER FUNCTION "SSDQ".regexp_substr(str text, pattern text) OWNER TO ssdq_admin;

--
-- Name: regexp_substr(character varying, character varying); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".regexp_substr(str character varying, pattern character varying) RETURNS text
    LANGUAGE sql
    AS $$
SELECT (regexp_matches(str, pattern))[1]
$$;


ALTER FUNCTION "SSDQ".regexp_substr(str character varying, pattern character varying) OWNER TO ssdq_admin;

--
-- Name: trunc(date, character varying); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".trunc(dt date, formatstr character varying) RETURNS date
    LANGUAGE plpgsql
    AS $$
begin
return date_trunc(formatstr,dt);
end;
$$;


ALTER FUNCTION "SSDQ".trunc(dt date, formatstr character varying) OWNER TO ssdq_admin;

--
-- Name: trunc(timestamp without time zone, character varying); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".trunc(dt timestamp without time zone, formatstr character varying) RETURNS date
    LANGUAGE plpgsql
    AS $$
begin
return date_trunc(formatstr,dt);
end;
$$;


ALTER FUNCTION "SSDQ".trunc(dt timestamp without time zone, formatstr character varying) OWNER TO ssdq_admin;

--
-- Name: trunc(timestamp with time zone, character varying); Type: FUNCTION; Schema: SSDQ; Owner: ssdq_admin
--

CREATE FUNCTION "SSDQ".trunc(dt timestamp with time zone, formatstr character varying) RETURNS date
    LANGUAGE plpgsql
    AS $$
begin
return date_trunc(formatstr,dt);
end;
$$;


ALTER FUNCTION "SSDQ".trunc(dt timestamp with time zone, formatstr character varying) OWNER TO ssdq_admin;

--
-- Name: update_users_proc(); Type: PROCEDURE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE PROCEDURE "SSDQ".update_users_proc()
    LANGUAGE plpgsql
    AS $$
begin
	/* Insert new records */
	insert into "SSDQ".dq_department_sdim(name)
	select dl.name
	from "SSDQ".dq_department_delta dl
	left join "SSDQ".dq_department_sdim d
	on dl.name = d.name
	and d.deleted_flag != 'Y'
	where d.id is null;
	
	/* delete records */
	update "SSDQ".dq_department_sdim
	set deleted_flag = 'Y'
	where id in (select id
				from "SSDQ".dq_department_sdim d 
				left join "SSDQ".dq_department_delta dl
				on d.name = dl.name
				where dl.name is null);
			
	/* Restore deleted records */
	update "SSDQ".dq_department_sdim
	set deleted_flag = 'N'
	where id in (select d.id
				from "SSDQ".dq_department_delta dl
				join "SSDQ".dq_department_sdim d
				on d.name = dl.name
				and d.deleted_flag = 'Y');
			
	/* Insert new users */
	insert into "SSDQ".dq_user_hdim (ad_login, full_name, email)
	select ud.login, ud.full_name, ud.email 
	from "SSDQ".dq_user_delta ud
	left join "SSDQ".dq_user_hdim u
	on ud.login = u.ad_login
	where u.uk is null;

	/* Update and restore changed (restored) users */
	update "SSDQ".dq_user_hdim u
	set ad_login = del.login,
		full_name = del.full_name,
		email = del.email,
		deleted_flag = 'N'
	from (select dud.login, dud.full_name, dud.email
		  from "SSDQ".dq_user_delta dud
		  left join "SSDQ".dq_user_hdim duh
		  on dud.login = duh.ad_login
		  and duh.deleted_flag != 'Y'
		  and (dud.full_name != duh.full_name
		  	or dud.email != duh.email)
		  union all
		  select dud.login, dud.full_name, dud.email
		  from "SSDQ".dq_user_delta dud
		  join "SSDQ".dq_user_hdim duh
		  on dud.login = duh.ad_login
		  and duh.deleted_flag = 'Y') del
	where u.ad_login = del.login;

	/* Delete users */
	update "SSDQ".dq_user_hdim u
	set deleted_flag = 'Y'
	from (select uk
		  from "SSDQ".dq_user_hdim u
		  left join "SSDQ".dq_user_delta ud
		  on u.ad_login = ud.login
		  where ud.login is null) del
	where u.uk = del.uk;
		 
	/* Insert new links */
	insert into "SSDQ".dq_user2department_sdim (user_id, department_id)
	select usr.user_id, d.id as department_id
	from (select u.uk as user_id, ud.department
		from "SSDQ".dq_user_delta ud
		join "SSDQ".dq_user_hdim u
		on ud.login = u.ad_login) usr
	join "SSDQ".dq_department_sdim d
	on usr.department = d.name
	and d.deleted_flag != 'Y'
	left join "SSDQ".dq_user2department_sdim u2d
	on usr.user_id = u2d.user_id
	and d.id = u2d.department_id
	where u2d.user_id is null;
	
	/* Delete links  */
	update "SSDQ".dq_user2department_sdim ud
	set deleted_flag = 'Y'
	from (select u2d.user_id, u2d.department_id
		from "SSDQ".dq_user2department_sdim u2d
		left join (select usr.user_id, d.id as department_id
			from (select u.uk as user_id, ud.department
				from "SSDQ".dq_user_delta ud
				join "SSDQ".dq_user_hdim u
				on ud.login = u.ad_login) usr
			join "SSDQ".dq_department_sdim d
			on usr.department = d.name) del
		on u2d.user_id = del.user_id
		and u2d.department_id = del.department_id
		where del.user_id is null) t
	where ud.user_id = t.user_id
	and ud.department_id = t.department_id;
	
	/* Restore links */
	update "SSDQ".dq_user2department_sdim ud
	set deleted_flag = 'N'
	from (select usr.user_id, d.id as department_id
		from (select u.uk as user_id, ud.department
			from "SSDQ".dq_user_delta ud
			join "SSDQ".dq_user_hdim u
			on ud.login = u.ad_login) usr
		join "SSDQ".dq_department_sdim d
		on usr.department = d.name
		join "SSDQ".dq_user2department_sdim u2d
		on usr.user_id = u2d.user_id
		and d.id = u2d.department_id
		and u2d.deleted_flag = 'Y') t
	where ud.user_id = t.user_id
	and ud.department_id = t.department_id;

end;
$$;


ALTER PROCEDURE "SSDQ".update_users_proc() OWNER TO ssdq_admin;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alerting_attachments_for_mail; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".alerting_attachments_for_mail (
    wf_run_id character varying(255),
    c_uk numeric,
    res_o text,
    mail_header text,
    c_report_time timestamp without time zone,
    filename character varying(255),
    attach_mimetype character varying(100),
    send_uk numeric
);


ALTER TABLE "SSDQ".alerting_attachments_for_mail OWNER TO ssdq_admin;

--
-- Name: alerting_sends_for_mail_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".alerting_sends_for_mail_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 1;


ALTER TABLE "SSDQ".alerting_sends_for_mail_seq OWNER TO ssdq_admin;

--
-- Name: alerting_sends_for_mail; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".alerting_sends_for_mail (
    mailto text,
    subject text,
    message text,
    mimetype text,
    res_i_tab_flag character(1),
    pm_workflow_run_id character varying(255),
    dq_control_uk numeric,
    uk numeric DEFAULT nextval('"SSDQ".alerting_sends_for_mail_seq'::regclass),
    sent_flag character(1) DEFAULT 'N'::bpchar
);


ALTER TABLE "SSDQ".alerting_sends_for_mail OWNER TO ssdq_admin;

--
-- Name: alert_sends_to_do; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".alert_sends_to_do AS
 SELECT asfm.mailto,
    asfm.subject,
    asfm.message,
    asfm.mimetype,
    asfm.res_i_tab_flag,
    asfm.pm_workflow_run_id,
    asfm.dq_control_uk,
    asfm.uk,
    asfm.sent_flag,
    aafm.wf_run_id,
    aafm.c_uk,
    aafm.res_o,
    aafm.mail_header,
    aafm.c_report_time,
    aafm.filename,
    aafm.attach_mimetype,
    aafm.send_uk,
        CASE
            WHEN (aafm.c_uk IS NOT NULL) THEN 'Y'::text
            ELSE 'N'::text
        END AS attach_flg
   FROM ("SSDQ".alerting_sends_for_mail asfm
     LEFT JOIN "SSDQ".alerting_attachments_for_mail aafm ON ((aafm.send_uk = asfm.uk)));


ALTER TABLE "SSDQ".alert_sends_to_do OWNER TO ssdq_admin;

--
-- Name: alerting_dq_ftp_file; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".alerting_dq_ftp_file (
    s_filename character varying(255),
    s_host_path_id character varying(255),
    c_uk numeric,
    wf_run_id character varying(255)
);


ALTER TABLE "SSDQ".alerting_dq_ftp_file OWNER TO ssdq_admin;

--
-- Name: bi_depts_t; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".bi_depts_t (
    id character varying(100),
    department character varying(1000),
    disabled character varying(1),
    as_of_day timestamp without time zone
);


ALTER TABLE "SSDQ".bi_depts_t OWNER TO ssdq_admin;

--
-- Name: components_t; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".components_t (
    project character varying(100),
    component_id character varying(100),
    component_name character varying(2000),
    component_lead character varying(100),
    archived character varying(1),
    as_of_day timestamp without time zone
);


ALTER TABLE "SSDQ".components_t OWNER TO ssdq_admin;

--
-- Name: customer_depts_t; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".customer_depts_t (
    id character varying(100),
    department character varying(2000),
    disabled character varying(1),
    as_of_day timestamp without time zone
);


ALTER TABLE "SSDQ".customer_depts_t OWNER TO ssdq_admin;

--
-- Name: dq_error_type_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_error_type_sdim (
    id numeric NOT NULL,
    error_type_name character varying(100)
);


ALTER TABLE "SSDQ".dq_error_type_sdim OWNER TO ssdq_admin;

--
-- Name: TABLE dq_error_type_sdim; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_error_type_sdim IS 'Типы характера ошибки';


--
-- Name: COLUMN dq_error_type_sdim.id; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_error_type_sdim.id IS 'код характера ошибки';


--
-- Name: COLUMN dq_error_type_sdim.error_type_name; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_error_type_sdim.error_type_name IS 'наименование характера ошибки';


--
-- Name: dict_error_type_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dict_error_type_seq
    START WITH 4
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999999
    CACHE 1;


ALTER TABLE "SSDQ".dict_error_type_seq OWNER TO ssdq_admin;

--
-- Name: dict_error_type_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dict_error_type_seq OWNED BY "SSDQ".dq_error_type_sdim.id;


--
-- Name: dq_owner_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_owner_sdim (
    id numeric NOT NULL,
    owner_name_short character varying(20),
    owner_name_full character varying(255),
    email character varying(255)
);


ALTER TABLE "SSDQ".dq_owner_sdim OWNER TO ssdq_admin;

--
-- Name: TABLE dq_owner_sdim; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_owner_sdim IS 'Владельцы Систем/Процессов в рамках процесса УКД ПВР';


--
-- Name: COLUMN dq_owner_sdim.owner_name_short; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_owner_sdim.owner_name_short IS 'Краткое наименование подразделения';


--
-- Name: COLUMN dq_owner_sdim.owner_name_full; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_owner_sdim.owner_name_full IS 'Полное наименование подразделения';


--
-- Name: COLUMN dq_owner_sdim.email; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_owner_sdim.email IS 'Email';


--
-- Name: dict_owner_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dict_owner_seq
    START WITH 2
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999999999999
    CACHE 1;


ALTER TABLE "SSDQ".dict_owner_seq OWNER TO ssdq_admin;

--
-- Name: dict_owner_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dict_owner_seq OWNED BY "SSDQ".dq_owner_sdim.id;


--
-- Name: dq_quality_type_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_quality_type_sdim (
    id numeric NOT NULL,
    quality_type_name character varying(255)
);


ALTER TABLE "SSDQ".dq_quality_type_sdim OWNER TO ssdq_admin;

--
-- Name: TABLE dq_quality_type_sdim; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_quality_type_sdim IS 'Характеристики Качества Данных';


--
-- Name: dict_quality_type_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dict_quality_type_seq
    START WITH 4
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 1;


ALTER TABLE "SSDQ".dict_quality_type_seq OWNER TO ssdq_admin;

--
-- Name: dict_quality_type_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dict_quality_type_seq OWNED BY "SSDQ".dq_quality_type_sdim.id;


--
-- Name: dq_systems_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_systems_sdim (
    id numeric NOT NULL,
    system_name character varying(255),
    system_short character varying(255)
);


ALTER TABLE "SSDQ".dq_systems_sdim OWNER TO ssdq_admin;

--
-- Name: dict_system_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dict_system_seq
    START WITH 2
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 1;


ALTER TABLE "SSDQ".dict_system_seq OWNER TO ssdq_admin;

--
-- Name: dict_system_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dict_system_seq OWNED BY "SSDQ".dq_systems_sdim.id;


--
-- Name: dq_alerting_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_alerting_hdim (
    dq_request_uk numeric NOT NULL,
    user_uk numeric NOT NULL,
    dq_mail_attachtype_uk numeric NOT NULL,
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'DD.MM.YYYY'::text),
    deleted_flag character(1) DEFAULT 'N'::bpchar
);


ALTER TABLE "SSDQ".dq_alerting_hdim OWNER TO ssdq_admin;

--
-- Name: dq_application_lov; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_application_lov (
    app_id numeric NOT NULL,
    app_name character varying(255),
    description character varying(1000)
);


ALTER TABLE "SSDQ".dq_application_lov OWNER TO ssdq_admin;

--
-- Name: TABLE dq_application_lov; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_application_lov IS 'Списко приложений КД';


--
-- Name: COLUMN dq_application_lov.app_id; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_application_lov.app_id IS 'Номер приложения';


--
-- Name: COLUMN dq_application_lov.app_name; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_application_lov.app_name IS 'Название приложения';


--
-- Name: COLUMN dq_application_lov.description; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_application_lov.description IS 'Описание';


--
-- Name: dq_bireport_department_lov; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_bireport_department_lov (
    business_category character varying(48),
    id character varying(100),
    dept_name character varying(93)
);


ALTER TABLE "SSDQ".dq_bireport_department_lov OWNER TO ssdq_admin;

--
-- Name: TABLE dq_bireport_department_lov; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_bireport_department_lov IS 'Перечень департаментов из BIHelp';


--
-- Name: dq_control2team_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_control2team_sdim (
    control_id numeric NOT NULL,
    team_id numeric NOT NULL
);


ALTER TABLE "SSDQ".dq_control2team_sdim OWNER TO ssdq_admin;

--
-- Name: dq_control_param_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_control_param_hdim (
    uk numeric NOT NULL,
    dq_request_uk numeric NOT NULL,
    control_name character varying(500),
    control_description character varying(4000),
    control_init character varying(400),
    client_dept_id character varying(100),
    release_numeric character varying(100),
    cr_numeric character varying(100),
    cor_date date,
    move_date character varying(20),
    delay character varying(100),
    mail_type character varying(100),
    ror_flag character(1) DEFAULT 'N'::bpchar,
    mail_h_flag character(1) DEFAULT 'N'::bpchar,
    auto_inc_flag character(1) DEFAULT 'N'::bpchar,
    officer_uk numeric,
    officer_to_do character varying(4000),
    dq_object_uk numeric,
    wiki_link character varying(400),
    dq_status_uk numeric,
    dq_ftp_path_uk numeric,
    customer_depts_t_id character varying(100),
    bi_depts_t_id character varying(100),
    components_t_id character varying(100),
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'DD.MM.YYYY'::text),
    deleted_flag character(1) DEFAULT 'N'::bpchar,
    default_flag character(1) DEFAULT 'N'::bpchar,
    user_login character varying(20),
    release_number character varying(100),
    cr_number character varying(100),
    user_name character varying(100),
    steward_uk numeric,
    control_critical_flag character(1),
    bondrymin_alerting numeric,
    bondrymax_alerting numeric,
    critmin_alerting numeric,
    critmax_alerting numeric
);


ALTER TABLE "SSDQ".dq_control_param_hdim OWNER TO ssdq_admin;

--
-- Name: dq_control_param_hdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_control_param_hdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 20;


ALTER TABLE "SSDQ".dq_control_param_hdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_control_param_hdim_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dq_control_param_hdim_seq OWNED BY "SSDQ".dq_control_param_hdim.uk;


--
-- Name: dq_dag_crossdb_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_dag_crossdb_hdim (
    dq_request_uk numeric NOT NULL,
    sql text,
    source character varying(100),
    custom_source_name character varying(100),
    main_sql character(1) DEFAULT 'N'::bpchar,
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'dd.mm.yyyy'::text),
    deleted_flag character(1) DEFAULT 'N'::bpchar
);


ALTER TABLE "SSDQ".dq_dag_crossdb_hdim OWNER TO ssdq_admin;

--
-- Name: dq_dag_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_dag_hdim (
    uk numeric NOT NULL,
    dq_request_uk numeric NOT NULL,
    sql text,
    alg character varying(4000),
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'dd.mm.yyyy'::text),
    deleted_flag character(1) DEFAULT 'N'::bpchar,
    crossdb_flag character(1) DEFAULT 'N'::bpchar,
    cron character varying(100),
    ready_start_object_uk numeric,
    load_end character varying(100),
    source character varying(100)
);


ALTER TABLE "SSDQ".dq_dag_hdim OWNER TO ssdq_admin;

--
-- Name: dq_dag_hdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_dag_hdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 20;


ALTER TABLE "SSDQ".dq_dag_hdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_dag_hdim_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dq_dag_hdim_seq OWNED BY "SSDQ".dq_dag_hdim.uk;


--
-- Name: dq_department_delta; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_department_delta (
    name character varying(256)
);


ALTER TABLE "SSDQ".dq_department_delta OWNER TO ssdq_admin;

--
-- Name: dq_department_sdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_department_sdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "SSDQ".dq_department_sdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_department_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_department_sdim (
    id numeric DEFAULT nextval('"SSDQ".dq_department_sdim_seq'::regclass) NOT NULL,
    name character varying(256),
    deleted_flag character varying(1) DEFAULT 'N'::character varying
);


ALTER TABLE "SSDQ".dq_department_sdim OWNER TO ssdq_admin;

--
-- Name: dq_detail_agg; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_detail_agg (
    description character varying(255),
    dq_control_uk numeric NOT NULL,
    end_time timestamp(6) without time zone,
    mistake_count numeric,
    report_date timestamp(6) without time zone,
    start_time timestamp(6) without time zone,
    max_result numeric,
    pm_workflow_run_id character varying(255) NOT NULL,
    script_finished character(1),
    error_flag character(1),
    out_of_margins_flag character(1),
    workflow_name character varying(155),
    error_name character varying(250),
    report_mistake_count numeric,
    read_rows_count numeric
);


ALTER TABLE "SSDQ".dq_detail_agg OWNER TO ssdq_admin;

--
-- Name: COLUMN dq_detail_agg.out_of_margins_flag; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_detail_agg.out_of_margins_flag IS '0 – не вышли; 1 – вышли за границы; 2 – есть критичные результаты';


--
-- Name: COLUMN dq_detail_agg.read_rows_count; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_detail_agg.read_rows_count IS 'Количество считанных строк';


--
-- Name: dq_detailjournal_web__pm_workflow_run_id_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_detailjournal_web__pm_workflow_run_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "SSDQ".dq_detailjournal_web__pm_workflow_run_id_seq OWNER TO ssdq_admin;

--
-- Name: dq_detailjournal_web; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_detailjournal_web (
    column_name character varying(255),
    column_uk1 numeric,
    column_uk2 numeric,
    column_uk3 numeric,
    defaultst_flag character(1),
    description character varying(255),
    dq_control_uk numeric,
    dq_level_uk numeric,
    error_flag character(1) DEFAULT 'Y'::bpchar,
    report_time timestamp(6) without time zone DEFAULT CURRENT_TIMESTAMP,
    result_char1 character varying(255),
    result_char2 character varying(255),
    result_char3 character varying(255),
    result_char4 character varying(255),
    result_char5 character varying(255),
    result_char6 character varying(255),
    result_date1 date,
    result_date2 date,
    result_date3 date,
    result_date4 date,
    result_num1 numeric,
    result_num2 numeric,
    result_num3 numeric,
    result_num4 numeric,
    rule_description character varying(255),
    value_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    xk numeric NOT NULL,
    pm_workflow_run_id character varying(25) DEFAULT nextval('"SSDQ".dq_detailjournal_web__pm_workflow_run_id_seq'::regclass) NOT NULL,
    connection_sid numeric,
    result_cur numeric(25,10),
    user_id numeric,
    result_owner character varying(250),
    mail_header character varying(1000),
    report_err_count numeric,
    impact_value numeric
);


ALTER TABLE "SSDQ".dq_detailjournal_web OWNER TO ssdq_admin;

--
-- Name: dq_detailjournal_web_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_detailjournal_web_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 20;


ALTER TABLE "SSDQ".dq_detailjournal_web_seq OWNER TO ssdq_admin;

--
-- Name: dq_detailjournal_web_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dq_detailjournal_web_seq OWNED BY "SSDQ".dq_detailjournal_web.xk;


--
-- Name: dq_ftp_path_ldim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_ftp_path_ldim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "SSDQ".dq_ftp_path_ldim_seq OWNER TO ssdq_admin;

--
-- Name: dq_ftp_path_ldim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_ftp_path_ldim (
    uk numeric DEFAULT nextval('"SSDQ".dq_ftp_path_ldim_seq'::regclass) NOT NULL,
    path_name character varying(255),
    host character varying(255)
);


ALTER TABLE "SSDQ".dq_ftp_path_ldim OWNER TO ssdq_admin;

--
-- Name: dq_mail_attachtype_lov; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_mail_attachtype_lov (
    uk numeric NOT NULL,
    "NAME" character varying(255)
);


ALTER TABLE "SSDQ".dq_mail_attachtype_lov OWNER TO ssdq_admin;

--
-- Name: TABLE dq_mail_attachtype_lov; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_mail_attachtype_lov IS 'Тип привязки результатов при отправке письма';


--
-- Name: COLUMN dq_mail_attachtype_lov.uk; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_mail_attachtype_lov.uk IS 'Уникальный Идентификатор записи';


--
-- Name: dq_mailing_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_mailing_hdim (
    dq_control_uk numeric NOT NULL,
    email character varying(250) NOT NULL,
    dq_mail_attachtype_uk numeric NOT NULL,
    deleted_flag character(1) NOT NULL,
    validfrom timestamp without time zone NOT NULL,
    validto timestamp without time zone NOT NULL,
    user_login character(10)
);


ALTER TABLE "SSDQ".dq_mailing_hdim OWNER TO ssdq_admin;

--
-- Name: TABLE dq_mailing_hdim; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_mailing_hdim IS 'Перечень п/я для рассылки результатов';


--
-- Name: dq_user_hdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_user_hdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "SSDQ".dq_user_hdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_user_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_user_hdim (
    uk numeric DEFAULT nextval('"SSDQ".dq_user_hdim_seq'::regclass) NOT NULL,
    ad_login character varying(20),
    full_name character varying(255) NOT NULL,
    email character varying(255),
    status character varying(64),
    deleted_flag character(1) DEFAULT 'N'::bpchar NOT NULL,
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    validto timestamp without time zone DEFAULT '5999-12-31'::date NOT NULL
);


ALTER TABLE "SSDQ".dq_user_hdim OWNER TO ssdq_admin;

--
-- Name: TABLE dq_user_hdim; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_user_hdim IS 'Справочник пользователей ПО КД. п/я в формате EXample@alfabank.ru';


--
-- Name: COLUMN dq_user_hdim.uk; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_user_hdim.uk IS 'Идентификатор записи';


--
-- Name: COLUMN dq_user_hdim.ad_login; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_user_hdim.ad_login IS 'Логин пользователя в КИС';


--
-- Name: COLUMN dq_user_hdim.email; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_user_hdim.email IS 'П/я в формате EXample@gazprombank.ru';


--
-- Name: COLUMN dq_user_hdim.status; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_user_hdim.status IS 'WORK-Работает,FIRED-Уволен,DENIED-Лишен доступа';


--
-- Name: dq_mailing_hdim_view; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".dq_mailing_hdim_view AS
 SELECT dah.dq_request_uk AS dq_control_uk,
    duh.email,
    dah.dq_mail_attachtype_uk,
    duh.ad_login AS user_login
   FROM ("SSDQ".dq_alerting_hdim dah
     JOIN "SSDQ".dq_user_hdim duh ON (((dah.user_uk = duh.uk) AND (duh.validto = to_date('31.12.5999'::text, 'DD.MM.YYYY'::text)) AND (duh.deleted_flag <> 'Y'::bpchar))))
  WHERE (dah.validto = to_date('31.12.5999'::text, 'DD.MM.YYYY'::text));


ALTER TABLE "SSDQ".dq_mailing_hdim_view OWNER TO ssdq_admin;

--
-- Name: dq_mailtype_lov; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_mailtype_lov (
    uk numeric NOT NULL,
    ccode character(1),
    "NAME" character varying(255)
);


ALTER TABLE "SSDQ".dq_mailtype_lov OWNER TO ssdq_admin;

--
-- Name: TABLE dq_mailtype_lov; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_mailtype_lov IS 'Условие отправки письма по результатам работы контроля';


--
-- Name: COLUMN dq_mailtype_lov.uk; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_mailtype_lov.uk IS 'Уникальный Идентификатор записи';


--
-- Name: dq_object_hdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_object_hdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "SSDQ".dq_object_hdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_object_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_object_hdim (
    uk numeric DEFAULT nextval('"SSDQ".dq_object_hdim_seq'::regclass) NOT NULL,
    base_name character varying(255),
    schema character varying(255),
    table_name character varying(255) NOT NULL,
    description character varying(255) NOT NULL,
    loaddq_flag character(1),
    reglament_uk numeric,
    entity_id numeric,
    deleted_flag character(1) DEFAULT 'N'::bpchar NOT NULL,
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'DD.MM.YYYY'::text) NOT NULL
);


ALTER TABLE "SSDQ".dq_object_hdim OWNER TO ssdq_admin;

--
-- Name: TABLE dq_object_hdim; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_object_hdim IS 'Справочник объектов проверки и расписаний';


--
-- Name: COLUMN dq_object_hdim.uk; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_object_hdim.uk IS 'Идентификатор записи';


--
-- Name: dq_request_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_request_hdim (
    uk numeric NOT NULL,
    terms character varying(4000) NOT NULL,
    owner character varying(50),
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'DD.MM.YYYY'::text),
    deleted_flag character(1) DEFAULT 'N'::bpchar,
    default_flag character(1) DEFAULT 'N'::bpchar,
    user_login character varying(20),
    user_name character varying(100)
);


ALTER TABLE "SSDQ".dq_request_hdim OWNER TO ssdq_admin;

--
-- Name: dq_spec_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_spec_hdim (
    uk numeric NOT NULL,
    dq_request_uk numeric NOT NULL,
    dqi_code character varying(200),
    segment_id character varying(20),
    ind_system_id numeric,
    data_system_id numeric,
    quality_type_id numeric,
    ind_version character varying(500),
    c_terms character varying(4000),
    alg_business character varying(4000),
    data_layer character varying(200),
    criterius character varying(4000),
    boundrymax_min numeric,
    boundrymed_max numeric,
    boundrymed_min numeric,
    boundrymin_max numeric,
    alg_tech character varying(4000),
    schedule character varying(4000),
    error_type_id numeric,
    met_owner1_id numeric,
    met_owner2_id numeric,
    met_owner3_id numeric,
    met_owner4_id numeric,
    met_owner5_id numeric,
    met_owner1_email character varying(200),
    met_owner2_email character varying(200),
    met_owner3_email character varying(200),
    met_owner4_email character varying(200),
    met_owner5_email character varying(200),
    cor_owner1_id numeric,
    cor_owner2_id numeric,
    cor_owner3_id numeric,
    cor_owner4_id numeric,
    cor_owner5_id numeric,
    cor_owner6_id numeric,
    cor_owner7_id numeric,
    cor_owner8_id numeric,
    cor_owner9_id numeric,
    cor_owner10_id numeric,
    cor_owner1_email character varying(200),
    cor_owner2_email character varying(200),
    cor_owner3_email character varying(200),
    cor_owner4_email character varying(200),
    cor_owner5_email character varying(200),
    cor_owner6_email character varying(200),
    cor_owner7_email character varying(200),
    cor_owner8_email character varying(200),
    cor_owner9_email character varying(200),
    cor_owner10_email character varying(200),
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'DD.MM.YYYY'::text),
    deleted_flag character(1) DEFAULT 'N'::bpchar,
    default_flag character(1) DEFAULT 'N'::bpchar,
    user_login character varying(20),
    user_name character varying(100)
);


ALTER TABLE "SSDQ".dq_spec_hdim OWNER TO ssdq_admin;

--
-- Name: dq_status_lov; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_status_lov (
    uk numeric NOT NULL,
    name character varying(255),
    description character varying(4000)
);


ALTER TABLE "SSDQ".dq_status_lov OWNER TO ssdq_admin;

--
-- Name: TABLE dq_status_lov; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON TABLE "SSDQ".dq_status_lov IS 'Справочник статусов контролей';


--
-- Name: COLUMN dq_status_lov.uk; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_status_lov.uk IS 'Уникальный Идентификатор записи';


--
-- Name: dq_monitoring_view; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".dq_monitoring_view AS
 SELECT DISTINCT r.uk,
    (((s.dqi_code)::text || ' '::text) || (c.control_name)::text) AS name,
    (((ob.schema)::text || '.'::text) || (ob.table_name)::text) AS object_name,
    u.full_name AS officer_name,
    c.officer_uk,
    st.name AS status_name,
    (dt.pm_workflow_run_id)::text AS run_id,
    dt.last_start,
    dt.last_result,
    dt.last_start AS overflow_start,
    dt2.last_result AS overflow_result,
    "SSDQ".nvl(c.control_description, '-'::character varying) AS description,
    "SSDQ".nvl(s.alg_business, '-'::character varying) AS rule_description,
    NULL::text AS defect,
    NULL::text AS proj,
    (dt2.pm_workflow_run_id)::text AS overflow_run_id,
    qt.quality_type_name AS control_type,
        CASE
            WHEN (c.dq_status_uk = (6)::numeric) THEN 'Да'::text
            ELSE 'Нет'::text
        END AS need_act,
    (((dep.business_category)::text || '-'::text) || (dep.dept_name)::text) AS dept_name,
    ('/change-spec.html/'::text || r.uk) AS dqi_id,
    st.uk AS dq_status_uk
   FROM ((((((((("SSDQ".dq_request_hdim r
     LEFT JOIN "SSDQ".dq_spec_hdim s ON (((r.uk = s.dq_request_uk) AND (s.validto = to_date('31.12.5999'::text, 'dd.mm.yyyy'::text)) AND (s.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_quality_type_sdim qt ON ((s.quality_type_id = qt.id)))
     LEFT JOIN "SSDQ".dq_control_param_hdim c ON (((r.uk = c.dq_request_uk) AND (c.validto = to_date('31.12.5999'::text, 'dd.mm.yyyy'::text)) AND (c.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_object_hdim ob ON (((c.dq_object_uk = ob.uk) AND (ob.validto = '5999-12-31'::date) AND (ob.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_user_hdim u ON (((c.officer_uk = u.uk) AND (u.validto = '5999-12-31'::date) AND (u.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_status_lov st ON ((c.dq_status_uk = st.uk)))
     LEFT JOIN ( SELECT (ag.start_time)::timestamp without time zone AS last_start,
            ag.pm_workflow_run_id,
            ag.dq_control_uk,
            row_number() OVER (PARTITION BY ag.dq_control_uk ORDER BY ag.pm_workflow_run_id DESC) AS rn,
            ag.mistake_count AS last_result
           FROM "SSDQ".dq_detail_agg ag) dt ON (((dt.dq_control_uk = r.uk) AND (dt.rn = 1))))
     LEFT JOIN ( SELECT (ag.start_time)::timestamp without time zone AS last_start,
            ag.pm_workflow_run_id,
            ag.dq_control_uk,
            row_number() OVER (PARTITION BY ag.dq_control_uk ORDER BY ag.pm_workflow_run_id DESC) AS rn,
            ag.mistake_count AS last_result
           FROM "SSDQ".dq_detail_agg ag
          WHERE (ag.mistake_count > (0)::numeric)) dt2 ON (((dt2.dq_control_uk = r.uk) AND (dt2.rn = 1))))
     LEFT JOIN "SSDQ".dq_bireport_department_lov dep ON (((dep.id)::text = (c.client_dept_id)::text)))
  WHERE ((r.validto = to_date('31.12.5999'::text, 'dd.mm.yyyy'::text)) AND (r.deleted_flag <> 'Y'::bpchar) AND (r.default_flag <> 'Y'::bpchar));


ALTER TABLE "SSDQ".dq_monitoring_view OWNER TO ssdq_admin;

--
-- Name: dq_request_hdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_request_hdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999999
    CACHE 1;


ALTER TABLE "SSDQ".dq_request_hdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_request_hdim_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dq_request_hdim_seq OWNED BY "SSDQ".dq_request_hdim.uk;


--
-- Name: dq_segment_hdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_segment_hdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 20;


ALTER TABLE "SSDQ".dq_segment_hdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_segment_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_segment_sdim (
    id numeric DEFAULT nextval('"SSDQ".dq_segment_hdim_seq'::regclass) NOT NULL,
    name character varying(50),
    description character varying(500),
    deleted_flag character(1) DEFAULT 'N'::bpchar
);


ALTER TABLE "SSDQ".dq_segment_sdim OWNER TO ssdq_admin;

--
-- Name: dq_source_hdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_source_hdim (
    uk numeric NOT NULL,
    name character varying(100) NOT NULL,
    connection_type character varying(255),
    schema character varying(255),
    host character varying(255),
    port numeric,
    description character varying(4000),
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'dd.mm.yyyy'::text),
    deleted_flag character varying(1) DEFAULT 'N'::character varying,
    default_flag character varying(1) DEFAULT 'N'::character varying
);


ALTER TABLE "SSDQ".dq_source_hdim OWNER TO ssdq_admin;

--
-- Name: dq_source_hdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_source_hdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 20;


ALTER TABLE "SSDQ".dq_source_hdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_source_hdim_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dq_source_hdim_seq OWNED BY "SSDQ".dq_source_hdim.uk;


--
-- Name: dq_spec_hdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_spec_hdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999999999
    CACHE 20;


ALTER TABLE "SSDQ".dq_spec_hdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_spec_hdim_seq; Type: SEQUENCE OWNED BY; Schema: SSDQ; Owner: ssdq_admin
--

ALTER SEQUENCE "SSDQ".dq_spec_hdim_seq OWNED BY "SSDQ".dq_spec_hdim.uk;


--
-- Name: dq_sql_detail_ldim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_sql_detail_ldim (
    dq_request_uk numeric,
    sql_query text,
    validfrom timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    validto timestamp without time zone DEFAULT to_date('31.12.5999'::text, 'dd.mm.yyyy'::text),
    user_login character varying(100),
    user_name character varying(100)
);


ALTER TABLE "SSDQ".dq_sql_detail_ldim OWNER TO ssdq_admin;

--
-- Name: dq_teams_sdim_seq; Type: SEQUENCE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE SEQUENCE "SSDQ".dq_teams_sdim_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "SSDQ".dq_teams_sdim_seq OWNER TO ssdq_admin;

--
-- Name: dq_teams_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_teams_sdim (
    id numeric DEFAULT nextval('"SSDQ".dq_teams_sdim_seq'::regclass) NOT NULL,
    name character varying(255) NOT NULL,
    description character varying(1000),
    deleted_flag character varying(1) DEFAULT 'N'::character varying,
    edit_mode character varying(10) DEFAULT 'nobody'::character varying
);


ALTER TABLE "SSDQ".dq_teams_sdim OWNER TO ssdq_admin;

--
-- Name: COLUMN dq_teams_sdim.edit_mode; Type: COMMENT; Schema: SSDQ; Owner: ssdq_admin
--

COMMENT ON COLUMN "SSDQ".dq_teams_sdim.edit_mode IS 'all - все члены команды, owners - все админы команды, nobody - никто';


--
-- Name: dq_user2department_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_user2department_sdim (
    user_id numeric NOT NULL,
    department_id numeric NOT NULL,
    deleted_flag character varying(1) DEFAULT 'N'::character varying
);


ALTER TABLE "SSDQ".dq_user2department_sdim OWNER TO ssdq_admin;

--
-- Name: dq_user2team_request; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_user2team_request (
    user_id numeric NOT NULL,
    team_id numeric NOT NULL
);


ALTER TABLE "SSDQ".dq_user2team_request OWNER TO ssdq_admin;

--
-- Name: dq_user2team_sdim; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_user2team_sdim (
    user_id numeric NOT NULL,
    team_id numeric NOT NULL,
    is_owner character varying(1) DEFAULT 'N'::character varying
);


ALTER TABLE "SSDQ".dq_user2team_sdim OWNER TO ssdq_admin;

--
-- Name: dq_user_delta; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".dq_user_delta (
    login character varying(20) NOT NULL,
    full_name character varying(256) NOT NULL,
    email character varying(256),
    department character varying(255)
);


ALTER TABLE "SSDQ".dq_user_delta OWNER TO ssdq_admin;

--
-- Name: si_pimp_my_mail; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".si_pimp_my_mail (
    dq_control_uk numeric,
    letters_count numeric,
    pm_workflow_run_id character varying(255),
    connection_sid numeric,
    start_time timestamp without time zone,
    end_time timestamp without time zone
);


ALTER TABLE "SSDQ".si_pimp_my_mail OWNER TO ssdq_admin;

--
-- Name: sql_c_uk; Type: TABLE; Schema: SSDQ; Owner: ssdq_admin
--

CREATE TABLE "SSDQ".sql_c_uk (
    sql text
);


ALTER TABLE "SSDQ".sql_c_uk OWNER TO ssdq_admin;

--
-- Name: view_all_controls_bydate; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_all_controls_bydate AS
 WITH calendar AS (
         SELECT (gs.gs)::date AS thedate
           FROM generate_series('2024-02-06 00:00:00+03'::timestamp with time zone, (CURRENT_DATE)::timestamp with time zone, '1 day'::interval) gs(gs)
        ), controls AS (
         SELECT t.dq_request_uk,
            t.dq_status_uk,
            t.officer_uk,
            t.validfrom,
            t.validto
           FROM ( SELECT p.dq_request_uk,
                    p.dq_status_uk,
                    p.officer_uk,
                    date(p.validfrom) AS validfrom,
                    date(p.validto) AS validto,
                    row_number() OVER (PARTITION BY p.dq_request_uk, (date(p.validfrom)) ORDER BY p.validfrom DESC) AS rn
                   FROM "SSDQ".dq_control_param_hdim p
                  WHERE (p.deleted_flag <> 'Y'::bpchar)) t
          WHERE (t.rn = 1)
        )
 SELECT c.thedate,
    ct.dq_request_uk AS uk,
    ct.dq_status_uk,
    ct.officer_uk
   FROM (calendar c
     LEFT JOIN controls ct ON (((c.thedate >= ct.validfrom) AND (c.thedate <= (ct.validto - 1)))))
  ORDER BY c.thedate;


ALTER TABLE "SSDQ".view_all_controls_bydate OWNER TO ssdq_admin;

--
-- Name: view_controls_count; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_controls_count AS
 WITH all_cnt AS (
         SELECT count(r.uk) AS cnt,
            p.dq_status_uk
           FROM ("SSDQ".dq_request_hdim r
             JOIN "SSDQ".dq_control_param_hdim p ON (((r.uk = p.dq_request_uk) AND (p.deleted_flag <> 'Y'::bpchar) AND (p.validto = '5999-12-31'::date))))
          WHERE ((r.deleted_flag <> 'Y'::bpchar) AND (r.validto = '5999-12-31'::date))
          GROUP BY p.dq_status_uk
        UNION ALL
         SELECT count(r.uk) AS cnt,
            0 AS dq_status_uk
           FROM "SSDQ".dq_request_hdim r
          WHERE ((r.deleted_flag <> 'Y'::bpchar) AND (r.validto = '5999-12-31'::date))
        )
 SELECT COALESCE(a.cnt, (0)::bigint) AS all_cnt,
    COALESCE(d.cnt, (0)::bigint) AS exp_cnt,
    COALESCE(b.cnt, (0)::bigint) AS cncl_cnt,
    COALESCE(c.cnt, (0)::bigint) AS act_cnt
   FROM (((all_cnt a
     LEFT JOIN all_cnt b ON ((b.dq_status_uk = (5)::numeric)))
     LEFT JOIN all_cnt c ON ((c.dq_status_uk = (6)::numeric)))
     LEFT JOIN all_cnt d ON ((d.dq_status_uk = (4)::numeric)))
  WHERE (a.dq_status_uk = (0)::numeric);


ALTER TABLE "SSDQ".view_controls_count OWNER TO ssdq_admin;

--
-- Name: view_controls_error; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_controls_error AS
 WITH calendar AS (
         SELECT (gs.gs)::date AS thedate
           FROM generate_series(('2024-02-06'::date)::timestamp with time zone, (CURRENT_DATE)::timestamp with time zone, '1 day'::interval) gs(gs)
        ), controls AS (
         SELECT date(agg.report_date) AS report_date,
            agg.dq_control_uk AS uk,
            cp.officer_uk,
            sp.segment_id
           FROM ((("SSDQ".dq_detail_agg agg
             JOIN "SSDQ".dq_spec_hdim sp ON (((agg.dq_control_uk = sp.dq_request_uk) AND (sp.deleted_flag <> 'Y'::bpchar) AND (sp.validto = '5999-12-31'::date))))
             JOIN "SSDQ".dq_control_param_hdim cp ON (((agg.dq_control_uk = cp.dq_request_uk) AND (cp.deleted_flag <> 'Y'::bpchar) AND (cp.validto = '5999-12-31'::date))))
             LEFT JOIN "SSDQ".dq_segment_sdim seg ON ((((sp.segment_id)::text = ((seg.id)::character varying)::text) AND (seg.deleted_flag <> 'Y'::bpchar))))
          WHERE (agg.mistake_count > (0)::numeric)
        )
 SELECT cal.thedate AS report_date,
    COALESCE(c.uk, ('-1'::integer)::numeric) AS uk,
    COALESCE(c.officer_uk, ('-1'::integer)::numeric) AS officer_uk,
    COALESCE((c.segment_id)::numeric, ('-1'::integer)::numeric) AS segment_id
   FROM (calendar cal
     LEFT JOIN controls c ON ((cal.thedate = c.report_date)));


ALTER TABLE "SSDQ".view_controls_error OWNER TO ssdq_admin;

--
-- Name: view_specification_change; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_specification_change AS
 SELECT r.uk,
    (((s.dqi_code)::text || ' '::text) || (c.control_name)::text) AS dqi_name,
    "SSDQ".nvl((c.control_description)::text, '-'::text) AS dq_description,
    "SSDQ".nvl((s.alg_business)::text, '-'::text) AS dq_rule_description,
    "SSDQ".nvl((s.data_layer)::text, '-'::text) AS level_name,
    "SSDQ".nvl((s.segment_id)::text, '-'::text) AS segment_id,
    "SSDQ".nvl((s.segment_id)::text, '-'::text) AS segment_type_name,
    "SSDQ".nvl(qt.quality_type_name, '-'::character varying) AS quality_type_name,
    "SSDQ".nvl(sm1.system_name, '-'::character varying) AS control_system_name,
    "SSDQ".nvl(sm2.system_name, '-'::character varying) AS data_system_name,
    "SSDQ".nvl(det.error_type_name, '-'::character varying) AS error_type_name,
    "SSDQ".nvl(metod1.owner_name_full, '-'::character varying) AS metod1_full_name,
    "SSDQ".nvl((s.met_owner1_email)::text, '-'::text) AS met_owner1_email,
    "SSDQ".nvl(owner1.owner_name_full, '-'::character varying) AS owner1_name_full,
    "SSDQ".nvl(owner2.owner_name_full, '-'::character varying) AS owner2_name_full,
    "SSDQ".nvl(owner3.owner_name_full, '-'::character varying) AS owner3_name_full,
    "SSDQ".nvl(owner4.owner_name_full, '-'::character varying) AS owner4_name_full,
    "SSDQ".nvl((s.cor_owner1_email)::text, '-'::text) AS cor_owner1_email,
    "SSDQ".nvl((s.cor_owner2_email)::text, '-'::text) AS cor_owner2_email,
    "SSDQ".nvl((s.cor_owner3_email)::text, '-'::text) AS cor_owner3_email,
    "SSDQ".nvl((s.cor_owner4_email)::text, '-'::text) AS cor_owner4_email,
    (s.boundrymin_max - (s.boundrymin_max - 0.01)) AS b_0_01,
    s.boundrymin_max AS b_boundrymin,
    s.boundrymed_min AS b_boundrymin_p_1,
    s.boundrymed_max AS b_boundrymax,
    s.boundrymax_min AS b_boundrymax_p_1,
    "SSDQ".nvl((s.criterius)::text, '-'::text) AS b_param_boundry,
    "SSDQ".nvl((s.schedule)::text, '-'::text) AS schedule,
    "SSDQ".nvl((s.alg_tech)::text, '-'::text) AS alg_tech,
    "SSDQ".nvl((s.c_terms)::text, '-'::text) AS c_terms,
    r.uk AS "DQI_ID",
    c.control_name,
    c.control_description,
    c.control_init,
    c.client_dept_id,
    c.release_number,
    c.cr_number,
    c.cor_date,
    c.move_date,
    c.delay,
    c.mail_type,
    c.ror_flag,
    c.mail_h_flag,
    c.auto_inc_flag,
    c.officer_uk,
    c.officer_to_do,
    c.dq_object_uk,
    c.wiki_link,
    c.dq_status_uk,
    c.dq_ftp_path_uk,
    c.components_t_id,
    c.customer_depts_t_id,
    c.bi_depts_t_id,
    dag.sql AS source_query,
    dag.source AS source_name,
    dag.alg,
    dag.cron,
    dag.ready_start_object_uk,
    dag.load_end,
    ('V'::text || to_char(r.validto, 'dd-mm-yyyy hh24:mi:ss'::text)) AS ver,
    r.validto,
    c.steward_uk,
    c.control_critical_flag,
    c.bondrymin_alerting,
    c.bondrymax_alerting,
    c.critmin_alerting,
    c.critmax_alerting,
    dag.crossdb_flag
   FROM (((((((((((("SSDQ".dq_request_hdim r
     LEFT JOIN "SSDQ".dq_spec_hdim s ON (((r.uk = s.dq_request_uk) AND (s.validto = r.validto) AND (s.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_control_param_hdim c ON (((r.uk = c.dq_request_uk) AND (c.validto = r.validto) AND (c.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_quality_type_sdim qt ON ((s.quality_type_id = qt.id)))
     LEFT JOIN "SSDQ".dq_systems_sdim sm1 ON ((sm1.id = s.ind_system_id)))
     LEFT JOIN "SSDQ".dq_systems_sdim sm2 ON ((sm2.id = s.data_system_id)))
     LEFT JOIN "SSDQ".dq_error_type_sdim det ON ((det.id = s.error_type_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim metod1 ON ((metod1.id = s.met_owner1_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim owner1 ON ((owner1.id = s.cor_owner1_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim owner2 ON ((owner2.id = s.cor_owner2_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim owner3 ON ((owner3.id = s.cor_owner3_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim owner4 ON ((owner4.id = s.cor_owner4_id)))
     LEFT JOIN "SSDQ".dq_dag_hdim dag ON (((r.uk = dag.dq_request_uk) AND (dag.validto = r.validto) AND (dag.deleted_flag <> 'Y'::bpchar))))
  WHERE ((r.deleted_flag <> 'Y'::bpchar) AND (r.default_flag <> 'Y'::bpchar));


ALTER TABLE "SSDQ".view_specification_change OWNER TO ssdq_admin;

--
-- Name: view_specification_info; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_specification_info AS
 SELECT r.uk,
    (((s.dqi_code)::text || ' '::text) || (c.control_name)::text) AS dqi_name,
    "SSDQ".nvl((c.control_description)::text, '-'::text) AS dq_description,
    "SSDQ".nvl((s.alg_business)::text, '-'::text) AS dq_rule_description,
    "SSDQ".nvl((s.data_layer)::text, '-'::text) AS level_name,
    "SSDQ".nvl((s.segment_id)::text, '-'::text) AS segment_id,
    "SSDQ".nvl((s.segment_id)::text, '-'::text) AS segment_type_name,
    "SSDQ".nvl(qt.quality_type_name, '-'::character varying) AS quality_type_name,
    "SSDQ".nvl(sm1.system_name, '-'::character varying) AS control_system_name,
    "SSDQ".nvl(sm2.system_name, '-'::character varying) AS data_system_name,
    "SSDQ".nvl(det.error_type_name, '-'::character varying) AS error_type_name,
    "SSDQ".nvl(metod1.owner_name_full, '-'::character varying) AS metod1_full_name,
    "SSDQ".nvl((s.met_owner1_email)::text, '-'::text) AS met_owner1_email,
    "SSDQ".nvl(owner1.owner_name_full, '-'::character varying) AS owner1_name_full,
    "SSDQ".nvl(owner2.owner_name_full, '-'::character varying) AS owner2_name_full,
    "SSDQ".nvl(owner3.owner_name_full, '-'::character varying) AS owner3_name_full,
    "SSDQ".nvl(owner4.owner_name_full, '-'::character varying) AS owner4_name_full,
    "SSDQ".nvl((s.cor_owner1_email)::text, '-'::text) AS cor_owner1_email,
    "SSDQ".nvl((s.cor_owner2_email)::text, '-'::text) AS cor_owner2_email,
    "SSDQ".nvl((s.cor_owner3_email)::text, '-'::text) AS cor_owner3_email,
    "SSDQ".nvl((s.cor_owner4_email)::text, '-'::text) AS cor_owner4_email,
    (s.boundrymin_max - (s.boundrymin_max - 0.01)) AS b_0_01,
    s.boundrymin_max AS b_boundrymin,
    s.boundrymed_min AS b_boundrymin_p_1,
    s.boundrymed_max AS b_boundrymax,
    s.boundrymax_min AS b_boundrymax_p_1,
    "SSDQ".nvl((s.criterius)::text, '-'::text) AS b_param_boundry,
    "SSDQ".nvl((s.schedule)::text, '-'::text) AS schedule,
    "SSDQ".nvl((s.alg_tech)::text, '-'::text) AS alg_tech,
    "SSDQ".nvl((s.c_terms)::text, '-'::text) AS c_terms,
    r.uk AS "DQI_ID",
    ('V'::text || to_char(r.validto, 'dd-mm-yyyy hh24:mi:ss'::text)) AS ver,
    r.validto
   FROM ((((((((((("SSDQ".dq_request_hdim r
     LEFT JOIN "SSDQ".dq_spec_hdim s ON (((r.uk = s.dq_request_uk) AND (date_trunc('minute'::text, s.validto) = date_trunc('minute'::text, r.validto)) AND (s.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_control_param_hdim c ON (((r.uk = c.dq_request_uk) AND (date_trunc('minute'::text, c.validto) = date_trunc('minute'::text, r.validto)) AND (c.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_quality_type_sdim qt ON ((s.quality_type_id = qt.id)))
     LEFT JOIN "SSDQ".dq_systems_sdim sm1 ON ((sm1.id = s.ind_system_id)))
     LEFT JOIN "SSDQ".dq_systems_sdim sm2 ON ((sm2.id = s.data_system_id)))
     LEFT JOIN "SSDQ".dq_error_type_sdim det ON ((det.id = s.error_type_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim metod1 ON ((metod1.id = s.met_owner1_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim owner1 ON ((owner1.id = s.cor_owner1_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim owner2 ON ((owner2.id = s.cor_owner2_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim owner3 ON ((owner3.id = s.cor_owner3_id)))
     LEFT JOIN "SSDQ".dq_owner_sdim owner4 ON ((owner4.id = s.cor_owner4_id)))
  WHERE ((r.deleted_flag <> 'Y'::bpchar) AND (r.default_flag <> 'Y'::bpchar));


ALTER TABLE "SSDQ".view_specification_info OWNER TO ssdq_admin;

--
-- Name: view_specification_list; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_specification_list AS
 SELECT s.dqi_code AS code,
    c.control_name AS name,
    c.control_description AS description,
    r.uk AS id
   FROM (("SSDQ".dq_request_hdim r
     LEFT JOIN "SSDQ".dq_spec_hdim s ON (((r.uk = s.dq_request_uk) AND (s.validto = to_date('31.12.5999'::text, 'dd.mm.yyyy'::text)) AND (s.deleted_flag <> 'Y'::bpchar))))
     LEFT JOIN "SSDQ".dq_control_param_hdim c ON (((r.uk = c.dq_request_uk) AND (c.validto = to_date('31.12.5999'::text, 'dd.mm.yyyy'::text)) AND (c.deleted_flag <> 'Y'::bpchar))))
  WHERE ((r.validto = to_date('31.12.5999'::text, 'dd.mm.yyyy'::text)) AND (r.deleted_flag <> 'Y'::bpchar) AND (r.default_flag <> 'Y'::bpchar));


ALTER TABLE "SSDQ".view_specification_list OWNER TO ssdq_admin;

--
-- Name: view_specification_versions; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_specification_versions AS
 SELECT r.uk,
    ('V'::text || to_char(r.validto, 'dd-mm-yyyy hh24:mi:ss'::text)) AS ver,
    r.validto
   FROM "SSDQ".dq_request_hdim r
  WHERE ((r.deleted_flag <> 'Y'::bpchar) AND (r.default_flag <> 'Y'::bpchar));


ALTER TABLE "SSDQ".view_specification_versions OWNER TO ssdq_admin;

--
-- Name: view_team_users; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_team_users AS
 SELECT u2t.user_id,
    u.full_name,
    u.email,
    u2t.team_id,
    u2t.is_owner
   FROM ("SSDQ".dq_user2team_sdim u2t
     JOIN "SSDQ".dq_user_hdim u ON (((u2t.user_id = u.uk) AND (u.deleted_flag <> 'Y'::bpchar) AND (u.validto = '5999-12-31'::date))));


ALTER TABLE "SSDQ".view_team_users OWNER TO ssdq_admin;

--
-- Name: view_teams_requests; Type: VIEW; Schema: SSDQ; Owner: ssdq_admin
--

CREATE VIEW "SSDQ".view_teams_requests AS
 SELECT tr.team_id,
    t.name AS team_name,
    tr.user_id,
    u.ad_login AS login,
    u.full_name
   FROM (("SSDQ".dq_user2team_request tr
     LEFT JOIN "SSDQ".dq_teams_sdim t ON (((tr.team_id = t.id) AND ((t.deleted_flag)::text <> 'Y'::text))))
     LEFT JOIN "SSDQ".dq_user_hdim u ON (((tr.user_id = u.uk) AND (u.deleted_flag <> 'Y'::bpchar) AND (u.validto = '5999-12-31'::date))));


ALTER TABLE "SSDQ".view_teams_requests OWNER TO ssdq_admin;

--
-- Name: dq_control_param_hdim uk; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_control_param_hdim ALTER COLUMN uk SET DEFAULT nextval('"SSDQ".dq_control_param_hdim_seq'::regclass);


--
-- Name: dq_dag_hdim uk; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_dag_hdim ALTER COLUMN uk SET DEFAULT nextval('"SSDQ".dq_dag_hdim_seq'::regclass);


--
-- Name: dq_detailjournal_web xk; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_detailjournal_web ALTER COLUMN xk SET DEFAULT nextval('"SSDQ".dq_detailjournal_web_seq'::regclass);


--
-- Name: dq_error_type_sdim id; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_error_type_sdim ALTER COLUMN id SET DEFAULT nextval('"SSDQ".dict_error_type_seq'::regclass);


--
-- Name: dq_owner_sdim id; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_owner_sdim ALTER COLUMN id SET DEFAULT nextval('"SSDQ".dict_owner_seq'::regclass);


--
-- Name: dq_quality_type_sdim id; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_quality_type_sdim ALTER COLUMN id SET DEFAULT nextval('"SSDQ".dict_quality_type_seq'::regclass);


--
-- Name: dq_request_hdim uk; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_request_hdim ALTER COLUMN uk SET DEFAULT nextval('"SSDQ".dq_request_hdim_seq'::regclass);


--
-- Name: dq_source_hdim uk; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_source_hdim ALTER COLUMN uk SET DEFAULT nextval('"SSDQ".dq_source_hdim_seq'::regclass);


--
-- Name: dq_spec_hdim uk; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_spec_hdim ALTER COLUMN uk SET DEFAULT nextval('"SSDQ".dq_spec_hdim_seq'::regclass);


--
-- Name: dq_systems_sdim id; Type: DEFAULT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_systems_sdim ALTER COLUMN id SET DEFAULT nextval('"SSDQ".dict_system_seq'::regclass);


--
-- Data for Name: alerting_attachments_for_mail; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".alerting_attachments_for_mail (wf_run_id, c_uk, res_o, mail_header, c_report_time, filename, attach_mimetype, send_uk) FROM stdin;
\.


--
-- Data for Name: alerting_dq_ftp_file; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".alerting_dq_ftp_file (s_filename, s_host_path_id, c_uk, wf_run_id) FROM stdin;
\.


--
-- Data for Name: alerting_sends_for_mail; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".alerting_sends_for_mail (mailto, subject, message, mimetype, res_i_tab_flag, pm_workflow_run_id, dq_control_uk, uk, sent_flag) FROM stdin;
\.


--
-- Data for Name: bi_depts_t; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".bi_depts_t (id, department, disabled, as_of_day) FROM stdin;
\.


--
-- Data for Name: components_t; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".components_t (project, component_id, component_name, component_lead, archived, as_of_day) FROM stdin;
\.


--
-- Data for Name: customer_depts_t; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".customer_depts_t (id, department, disabled, as_of_day) FROM stdin;
\.


--
-- Data for Name: dq_alerting_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_alerting_hdim (dq_request_uk, user_uk, dq_mail_attachtype_uk, validfrom, validto, deleted_flag) FROM stdin;
1	1	1	2024-03-05 18:15:47.715136	5999-12-31 00:00:00	N
1	2	1	2024-03-05 18:15:47.715136	5999-12-31 00:00:00	N
2	1	1	2024-03-13 15:53:26.711494	5999-12-31 00:00:00	N
2	2	1	2024-03-13 15:53:26.711494	5999-12-31 00:00:00	N
\.


--
-- Data for Name: dq_application_lov; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_application_lov (app_id, app_name, description) FROM stdin;
\.


--
-- Data for Name: dq_bireport_department_lov; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_bireport_department_lov (business_category, id, dept_name) FROM stdin;
\.


--
-- Data for Name: dq_control2team_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_control2team_sdim (control_id, team_id) FROM stdin;
\.


--
-- Data for Name: dq_control_param_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_control_param_hdim (uk, dq_request_uk, control_name, control_description, control_init, client_dept_id, release_numeric, cr_numeric, cor_date, move_date, delay, mail_type, ror_flag, mail_h_flag, auto_inc_flag, officer_uk, officer_to_do, dq_object_uk, wiki_link, dq_status_uk, dq_ftp_path_uk, customer_depts_t_id, bi_depts_t_id, components_t_id, validfrom, validto, deleted_flag, default_flag, user_login, release_number, cr_number, user_name, steward_uk, control_critical_flag, bondrymin_alerting, bondrymax_alerting, critmin_alerting, critmax_alerting) FROM stdin;
21	2	Test teams control	Test teams control		0	\N	\N	\N		-	Всегда	N	N	N	22	Test teams control	2		4	0	\N	\N	\N	2024-03-13 13:45:44.556716	5999-12-31 00:00:00	N	N	1			admin	0	N	\N	\N	\N	\N
1	1	Test dq control	Test dq control		0	\N	\N	\N		-	Всегда	N	N	N	1	Test dq control	2		4	0	\N	\N	\N	2024-03-05 18:15:47.715136	2024-03-14 13:02:09.767166	N	N	1			admin	3	N	\N	\N	\N	\N
41	1	Test dq control	Test dq control		0	\N	\N	\N		-	Всегда	N	N	N	22	Test dq control	2		4	0	\N	\N	\N	2024-03-14 13:02:09.767166	5999-12-31 00:00:00	N	N	admin			admin	3	N	\N	\N	\N	\N
61	3	Test accessable control	Test accessable control		0	\N	\N	\N		-	Всегда	N	N	N	1	Test accessable control	2		4	0	\N	\N	\N	2024-03-14 15:26:36.246951	5999-12-31 00:00:00	N	N	admin			admin	0	N	\N	\N	\N	\N
81	4	Test unavailable control	Test unavailable control		0	\N	\N	\N		-	Всегда	N	N	N	3	Test unavailable control	4		4	0	\N	\N	\N	2024-03-14 15:28:56.472608	5999-12-31 00:00:00	N	N	admin			admin	0	N	\N	\N	\N	\N
\.


--
-- Data for Name: dq_dag_crossdb_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_dag_crossdb_hdim (dq_request_uk, sql, source, custom_source_name, main_sql, validfrom, validto, deleted_flag) FROM stdin;
\.


--
-- Data for Name: dq_dag_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_dag_hdim (uk, dq_request_uk, sql, alg, validfrom, validto, deleted_flag, crossdb_flag, cron, ready_start_object_uk, load_end, source) FROM stdin;
1	1	Select 1 as column_uk1		2024-03-05 18:15:47.715136	5999-12-31 00:00:00	N	N	None	\N	\N	GreenPlum
21	2	select 23 as column_uk1		2024-03-13 13:45:44.556716	5999-12-31 00:00:00	N	N	None	\N	\N	GreenPlum
41	3	select 121 as column_uk1		2024-03-14 15:26:36.246951	5999-12-31 00:00:00	N	N	None	\N	\N	GreenPlum
61	4	select 100 as column_uk1		2024-03-14 15:28:56.472608	5999-12-31 00:00:00	N	N	None	\N	\N	GreenPlum
\.


--
-- Data for Name: dq_department_delta; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_department_delta (name) FROM stdin;
\.


--
-- Data for Name: dq_department_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_department_sdim (id, name, deleted_flag) FROM stdin;
\.


--
-- Data for Name: dq_detail_agg; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_detail_agg (description, dq_control_uk, end_time, mistake_count, report_date, start_time, max_result, pm_workflow_run_id, script_finished, error_flag, out_of_margins_flag, workflow_name, error_name, report_mistake_count, read_rows_count) FROM stdin;
\N	1	\N	0	2024-03-01 00:00:00	\N	\N	1	\N	\N	\N	\N	\N	\N	\N
\N	1	\N	3	2024-03-01 00:00:00	\N	\N	2	\N	\N	\N	\N	\N	\N	\N
\N	1	\N	1	2024-03-02 00:00:00	\N	\N	3	\N	\N	\N	\N	\N	\N	\N
\N	2	\N	1	2024-03-01 00:00:00	\N	\N	5	\N	\N	\N	\N	\N	\N	\N
\N	2	\N	0	2024-03-02 00:00:00	\N	\N	6	\N	\N	\N	\N	\N	\N	\N
\N	2	\N	5	2024-03-03 00:00:00	\N	\N	7	\N	\N	\N	\N	\N	\N	\N
\N	2	\N	0	2024-03-04 00:00:00	\N	\N	8	\N	\N	\N	\N	\N	\N	\N
\N	3	\N	0	2024-03-01 00:00:00	\N	\N	9	\N	\N	\N	\N	\N	\N	\N
\N	3	\N	4	2024-03-02 00:00:00	\N	\N	10	\N	\N	\N	\N	\N	\N	\N
\N	3	\N	3	2024-03-03 00:00:00	\N	\N	11	\N	\N	\N	\N	\N	\N	\N
\N	3	\N	0	2024-03-04 00:00:00	\N	\N	12	\N	\N	\N	\N	\N	\N	\N
\N	1	\N	4	2024-03-04 00:00:00	\N	\N	4	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: dq_detailjournal_web; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_detailjournal_web (column_name, column_uk1, column_uk2, column_uk3, defaultst_flag, description, dq_control_uk, dq_level_uk, error_flag, report_time, result_char1, result_char2, result_char3, result_char4, result_char5, result_char6, result_date1, result_date2, result_date3, result_date4, result_num1, result_num2, result_num3, result_num4, rule_description, value_date, xk, pm_workflow_run_id, connection_sid, result_cur, user_id, result_owner, mail_header, report_err_count, impact_value) FROM stdin;
\.


--
-- Data for Name: dq_error_type_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_error_type_sdim (id, error_type_name) FROM stdin;
1	Целостность данных
2	Актуальность данных
3	Доступность данных
\.


--
-- Data for Name: dq_ftp_path_ldim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_ftp_path_ldim (uk, path_name, host) FROM stdin;
\.


--
-- Data for Name: dq_mail_attachtype_lov; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_mail_attachtype_lov (uk, "NAME") FROM stdin;
\.


--
-- Data for Name: dq_mailing_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_mailing_hdim (dq_control_uk, email, dq_mail_attachtype_uk, deleted_flag, validfrom, validto, user_login) FROM stdin;
\.


--
-- Data for Name: dq_mailtype_lov; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_mailtype_lov (uk, ccode, "NAME") FROM stdin;
\.


--
-- Data for Name: dq_object_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_object_hdim (uk, base_name, schema, table_name, description, loaddq_flag, reglament_uk, entity_id, deleted_flag, validfrom, validto) FROM stdin;
\.


--
-- Data for Name: dq_owner_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_owner_sdim (id, owner_name_short, owner_name_full, email) FROM stdin;
\.


--
-- Data for Name: dq_quality_type_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_quality_type_sdim (id, quality_type_name) FROM stdin;
1	Актуальность данных
2	Доступность данных
3	Целостность данных
\.


--
-- Data for Name: dq_request_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_request_hdim (uk, terms, owner, validfrom, validto, deleted_flag, default_flag, user_login, user_name) FROM stdin;
\.


--
-- Data for Name: dq_segment_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_segment_sdim (id, name, description, deleted_flag) FROM stdin;
1	Корпоративный	Корпоративный сегмент	N
2	Розничный	Розничный сегмент	N
\.


--
-- Data for Name: dq_source_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_source_hdim (uk, name, connection_type, schema, host, port, description, validfrom, validto, deleted_flag, default_flag) FROM stdin;
\.


--
-- Data for Name: dq_spec_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_spec_hdim (uk, dq_request_uk, dqi_code, segment_id, ind_system_id, data_system_id, quality_type_id, ind_version, c_terms, alg_business, data_layer, criterius, boundrymax_min, boundrymed_max, boundrymed_min, boundrymin_max, alg_tech, schedule, error_type_id, met_owner1_id, met_owner2_id, met_owner3_id, met_owner4_id, met_owner5_id, met_owner1_email, met_owner2_email, met_owner3_email, met_owner4_email, met_owner5_email, cor_owner1_id, cor_owner2_id, cor_owner3_id, cor_owner4_id, cor_owner5_id, cor_owner6_id, cor_owner7_id, cor_owner8_id, cor_owner9_id, cor_owner10_id, cor_owner1_email, cor_owner2_email, cor_owner3_email, cor_owner4_email, cor_owner5_email, cor_owner6_email, cor_owner7_email, cor_owner8_email, cor_owner9_email, cor_owner10_email, validfrom, validto, deleted_flag, default_flag, user_login, user_name) FROM stdin;
\.


--
-- Data for Name: dq_sql_detail_ldim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_sql_detail_ldim (dq_request_uk, sql_query, validfrom, validto, user_login, user_name) FROM stdin;
\.


--
-- Data for Name: dq_status_lov; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_status_lov (uk, name, description) FROM stdin;
1	Разработка	Контроли в разработке
2	Тестирование	Контроли на тестировании
3	Приемка заказчиком	Контроли на приемке заказчиком
4	В эксплуатации	Контроли в эксплуатации
5	Отменен	Отключенные контроли
6	На актуализации	Контроли на актуализации
\.


--
-- Data for Name: dq_systems_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_systems_sdim (id, system_name, system_short) FROM stdin;
1	Корпоративное хранилище данных	КХД
\.


--
-- Data for Name: dq_teams_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_teams_sdim (id, name, description, deleted_flag, edit_mode) FROM stdin;
\.


--
-- Data for Name: dq_user2department_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_user2department_sdim (user_id, department_id, deleted_flag) FROM stdin;
\.


--
-- Data for Name: dq_user2team_request; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_user2team_request (user_id, team_id) FROM stdin;
\.


--
-- Data for Name: dq_user2team_sdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_user2team_sdim (user_id, team_id, is_owner) FROM stdin;
\.


--
-- Data for Name: dq_user_delta; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_user_delta (login, full_name, email, department) FROM stdin;
\.


--
-- Data for Name: dq_user_hdim; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".dq_user_hdim (uk, ad_login, full_name, email, status, deleted_flag, validfrom, validto) FROM stdin;
\.


--
-- Data for Name: si_pimp_my_mail; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".si_pimp_my_mail (dq_control_uk, letters_count, pm_workflow_run_id, connection_sid, start_time, end_time) FROM stdin;
\.


--
-- Data for Name: sql_c_uk; Type: TABLE DATA; Schema: SSDQ; Owner: ssdq_admin
--

COPY "SSDQ".sql_c_uk (sql) FROM stdin;
\.


--
-- Name: alerting_sends_for_mail_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".alerting_sends_for_mail_seq', 1, false);


--
-- Name: dict_error_type_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dict_error_type_seq', 21, false);


--
-- Name: dict_owner_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dict_owner_seq', 43, false);


--
-- Name: dict_quality_type_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dict_quality_type_seq', 11, false);


--
-- Name: dict_system_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dict_system_seq', 28, false);


--
-- Name: dq_control_param_hdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_control_param_hdim_seq', 100, true);


--
-- Name: dq_dag_hdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_dag_hdim_seq', 80, true);


--
-- Name: dq_department_sdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_department_sdim_seq', 1, false);


--
-- Name: dq_detailjournal_web__pm_workflow_run_id_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_detailjournal_web__pm_workflow_run_id_seq', 1, false);


--
-- Name: dq_detailjournal_web_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_detailjournal_web_seq', 177740, true);


--
-- Name: dq_ftp_path_ldim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_ftp_path_ldim_seq', 1, false);


--
-- Name: dq_object_hdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_object_hdim_seq', 6, true);


--
-- Name: dq_request_hdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_request_hdim_seq', 4, true);


--
-- Name: dq_segment_hdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_segment_hdim_seq', 3, false);


--
-- Name: dq_source_hdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_source_hdim_seq', 20, true);


--
-- Name: dq_spec_hdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_spec_hdim_seq', 80, true);


--
-- Name: dq_teams_sdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_teams_sdim_seq', 43, true);


--
-- Name: dq_user_hdim_seq; Type: SEQUENCE SET; Schema: SSDQ; Owner: ssdq_admin
--

SELECT pg_catalog.setval('"SSDQ".dq_user_hdim_seq', 22, true);


--
-- Name: dq_error_type_sdim dict_error_type_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_error_type_sdim
    ADD CONSTRAINT dict_error_type_pk PRIMARY KEY (id);


--
-- Name: dq_owner_sdim dict_owner_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_owner_sdim
    ADD CONSTRAINT dict_owner_pk PRIMARY KEY (id);


--
-- Name: dq_quality_type_sdim dict_quality_type_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_quality_type_sdim
    ADD CONSTRAINT dict_quality_type_pk PRIMARY KEY (id);


--
-- Name: dq_systems_sdim dict_system_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_systems_sdim
    ADD CONSTRAINT dict_system_pk PRIMARY KEY (id);


--
-- Name: dq_application_lov dq_application_lov_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_application_lov
    ADD CONSTRAINT dq_application_lov_pk PRIMARY KEY (app_id);


--
-- Name: dq_control2team_sdim dq_control2team_sdim_unique; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_control2team_sdim
    ADD CONSTRAINT dq_control2team_sdim_unique UNIQUE (control_id, team_id);


--
-- Name: dq_mail_attachtype_lov dq_mail_attachtype_lov_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_mail_attachtype_lov
    ADD CONSTRAINT dq_mail_attachtype_lov_pk PRIMARY KEY (uk);


--
-- Name: dq_mailing_hdim dq_mailing_hdim_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_mailing_hdim
    ADD CONSTRAINT dq_mailing_hdim_pk PRIMARY KEY (dq_control_uk, email, deleted_flag, validto);


--
-- Name: dq_mailtype_lov dq_mailtype_lov_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_mailtype_lov
    ADD CONSTRAINT dq_mailtype_lov_pk PRIMARY KEY (uk);


--
-- Name: dq_object_hdim dq_object_hdim_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_object_hdim
    ADD CONSTRAINT dq_object_hdim_pk PRIMARY KEY (uk, deleted_flag, validto);


--
-- Name: dq_status_lov dq_status_lov_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_status_lov
    ADD CONSTRAINT dq_status_lov_pk PRIMARY KEY (uk);


--
-- Name: dq_teams_sdim dq_teams_sdim_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_teams_sdim
    ADD CONSTRAINT dq_teams_sdim_pk PRIMARY KEY (id);


--
-- Name: dq_teams_sdim dq_teams_sdim_unique; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_teams_sdim
    ADD CONSTRAINT dq_teams_sdim_unique UNIQUE (name);


--
-- Name: dq_user2team_request dq_user2team_request_unique; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_user2team_request
    ADD CONSTRAINT dq_user2team_request_unique UNIQUE (user_id, team_id);


--
-- Name: dq_user2team_sdim dq_user2team_sdim_unique; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_user2team_sdim
    ADD CONSTRAINT dq_user2team_sdim_unique UNIQUE (user_id, team_id);


--
-- Name: dq_user_hdim dq_user_hdim_pk; Type: CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_user_hdim
    ADD CONSTRAINT dq_user_hdim_pk PRIMARY KEY (uk, deleted_flag, validto);


--
-- Name: dq_control2team_sdim_control_id_idx; Type: INDEX; Schema: SSDQ; Owner: ssdq_admin
--

CREATE INDEX dq_control2team_sdim_control_id_idx ON "SSDQ".dq_control2team_sdim USING btree (control_id);


--
-- Name: dq_detailjournal_uk_indx; Type: INDEX; Schema: SSDQ; Owner: ssdq_admin
--

CREATE INDEX dq_detailjournal_uk_indx ON "SSDQ".dq_detailjournal_web USING btree (dq_control_uk);


--
-- Name: dq_user2team_request_team_id_idx; Type: INDEX; Schema: SSDQ; Owner: ssdq_admin
--

CREATE INDEX dq_user2team_request_team_id_idx ON "SSDQ".dq_user2team_request USING btree (team_id);


--
-- Name: dq_mailing_hdim dq_mailattach_fk; Type: FK CONSTRAINT; Schema: SSDQ; Owner: ssdq_admin
--

ALTER TABLE ONLY "SSDQ".dq_mailing_hdim
    ADD CONSTRAINT dq_mailattach_fk FOREIGN KEY (dq_mail_attachtype_uk) REFERENCES "SSDQ".dq_mail_attachtype_lov(uk);


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: SSDQ; Owner: ssdq_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE ssdq_admin IN SCHEMA "SSDQ" GRANT ALL ON SEQUENCES  TO ssdq_admin;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: SSDQ; Owner: ssdq_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE ssdq_admin IN SCHEMA "SSDQ" GRANT ALL ON FUNCTIONS  TO ssdq_admin;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: SSDQ; Owner: ssdq_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE ssdq_admin IN SCHEMA "SSDQ" GRANT ALL ON TABLES  TO ssdq_admin;


--
-- PostgreSQL database dump complete
--

