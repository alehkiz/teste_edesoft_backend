from flask.cli import with_appcontext

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
    return app

