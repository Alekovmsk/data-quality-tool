# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from datetime import timedelta
from .classes.conf import ConfYaml


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    template_folder = 'templates/home'

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    

class ProductionConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = ConfYaml.config['keycloak']['secret']
    OIDC_CLIENT_SECRETS = 'config/client_secrets.json'
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    OIDC_USER_INFO_ENABLED = True
    OIDC_INTROSPECTION_AUTH_METHOD = 'client_secret_post'
    OIDC_TOKEN_TYPE_HINT = 'acces_token'

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=ConfYaml.config['ssdq']['JWT_ACCESS_TOKEN_EXPIRES'])

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        ConfYaml.config['database']['flaskDb']['type'],
        ConfYaml.config['database']['flaskDb']['user'],
        ConfYaml.config['database']['flaskDb']['password'],
        ConfYaml.config['database']['flaskDb']['host'],
        ConfYaml.config['database']['flaskDb']['port'],
        ConfYaml.config['database']['flaskDb']['db']
    )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
