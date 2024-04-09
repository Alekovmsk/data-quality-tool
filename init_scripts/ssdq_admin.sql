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

CREATE DATABASE ssdq_admin WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'C.UTF-8';


ALTER DATABASE ssdq_admin OWNER TO ssdq_admin;

\connect ssdq_admin

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Users; Type: TABLE; Schema: public; Owner: ssdq_admin
--

CREATE TABLE public."Users" (
    id character varying(255) NOT NULL,
    email character varying(255),
    name character varying(255),
    login character varying(255),
    "timestamp" timestamp without time zone
);


ALTER TABLE public."Users" OWNER TO ssdq_admin;

--
-- Name: roles; Type: TABLE; Schema: public; Owner: ssdq_admin
--

CREATE TABLE public.roles (
    id integer,
    name character varying(255)
);


ALTER TABLE public.roles OWNER TO ssdq_admin;

--
-- Name: ssdq_logs_seq; Type: SEQUENCE; Schema: public; Owner: ssdq_admin
--

CREATE SEQUENCE public.ssdq_logs_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ssdq_logs_seq OWNER TO ssdq_admin;

--
-- Name: ssdq_logs; Type: TABLE; Schema: public; Owner: ssdq_admin
--

CREATE TABLE public.ssdq_logs (
    id integer DEFAULT nextval('public.ssdq_logs_seq'::regclass) NOT NULL,
    logger character varying(100),
    level character varying(100),
    trace character varying(4096),
    login character varying(20),
    msg character varying(4096),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ssdq_logs OWNER TO ssdq_admin;

--
-- Name: user_login; Type: TABLE; Schema: public; Owner: ssdq_admin
--

CREATE TABLE public.user_login (
    user_id character varying(255),
    login_timestamp timestamp without time zone,
    access_token character varying(3000)
);


ALTER TABLE public.user_login OWNER TO ssdq_admin;

--
-- Name: user_roles; Type: TABLE; Schema: public; Owner: ssdq_admin
--

CREATE TABLE public.user_roles (
    user_id character varying(255),
    role_id integer
);


ALTER TABLE public.user_roles OWNER TO ssdq_admin;


CREATE OR REPLACE VIEW public.user_w_role
AS SELECT u.id AS user_id,
    u.name,
    u.email,
    u.login,
    array_agg(r.name) AS role
   FROM "Users" u
     LEFT JOIN user_roles ur ON u.id::text = ur.user_id::text
     LEFT JOIN roles r ON r.id = ur.role_id
  GROUP BY u.id, u.name, u.email, u.login;


ALTER TABLE "SSDQ".user_w_role OWNER TO ssdq_admin;
--
-- Data for Name: Users; Type: TABLE DATA; Schema: public; Owner: ssdq_admin
--

COPY public."Users" (id, email, name, login, "timestamp") FROM stdin;
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: ssdq_admin
--

COPY public.roles (id, name) FROM stdin;
1	Readonly
2	DQ_OFFICER
3	DQ_ADMIN
4	DQ_STEWARD
\.


--
-- Data for Name: ssdq_logs; Type: TABLE DATA; Schema: public; Owner: ssdq_admin
--

COPY public.ssdq_logs (id, logger, level, trace, login, msg, created_at) FROM stdin;
\.


--
-- Data for Name: user_login; Type: TABLE DATA; Schema: public; Owner: ssdq_admin
--

COPY public.user_login (user_id, login_timestamp, access_token) FROM stdin;
\.


--
-- Data for Name: user_roles; Type: TABLE DATA; Schema: public; Owner: ssdq_admin
--

COPY public.user_roles (user_id, role_id) FROM stdin;
\.


--
-- Name: ssdq_logs_seq; Type: SEQUENCE SET; Schema: public; Owner: ssdq_admin
--

SELECT pg_catalog.setval('public.ssdq_logs_seq', 1, false);


--
-- Name: Users Users_pkey; Type: CONSTRAINT; Schema: public; Owner: ssdq_admin
--

ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT "Users_pkey" PRIMARY KEY (id);


--
-- Name: Users users_unique; Type: CONSTRAINT; Schema: public; Owner: ssdq_admin
--

ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT users_unique UNIQUE (email, login);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: ssdq_admin
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO ssdq_admin;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

