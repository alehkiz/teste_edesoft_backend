from config.config import config
from flask import Flask
from app.core.configure import init
from app.core.db import init_db
from logging import INFO

def create_app(mode='production'):
    app = Flask(__name__)
    app.config.from_object(config[mode])
    init(app)
    app.cli.add_command(init_db)
    app.logger.setLevel(INFO)
    return app