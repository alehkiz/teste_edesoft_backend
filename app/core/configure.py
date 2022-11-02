from flask.cli import with_appcontext
from os.path import exists
from os import mkdir
from logging.handlers import RotatingFileHandler
import logging

from datetime import datetime
from app.core.db import db
from app.blueprints import register_blueprints
from app.core.extensions import csrf


def init(app):
    db.init_app(app)
    csrf.init_app(app)
    register_blueprints(app)


    print('Servidor iniciado: ', datetime.utcnow())
    if app.debug is not True:
        if not exists('logs'):
            mkdir('logs')
        file_handler = RotatingFileHandler(
            'logs/errors.log', maxBytes=1024000, backupCount=100)
        file_handler.setFormatter(logging.Formatter(
            "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"))
        file_handler.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler)

    return app

