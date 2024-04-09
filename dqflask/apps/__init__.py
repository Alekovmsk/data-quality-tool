# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from .classes.Logger import SQLAlchemyHandler
import logging
import logging.config
from .classes.conf import ConfYaml
from .api import api_routes


db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    module = import_module('apps.{}.routes'.format('home'))
    app.register_blueprint(module.blueprint)
    app.register_blueprint(api_routes)


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)

    # Logging into file
    logging.config.dictConfig(ConfYaml.logging_conf)

    # Log handler into database
    #log_handler = SQLAlchemyHandler()
    #log_handler.setLevel(ConfYaml.config['logging']['log_level'])
    #log_handler.setFormatter(logging.Formatter(ConfYaml.config['logging']['log_formatter']))
    #app.logger.addHandler(log_handler)

    # System logs into database
    #logger = logging.getLogger('werkzeug')
    #logger.setLevel(ConfYaml.config['logging']['systemlog_level'])
    #logger.addHandler(log_handler)

    return app
