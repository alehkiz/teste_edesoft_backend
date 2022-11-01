from os import environ
from os.path import abspath, dirname, join
import app

class BaseConfig(object):
    PROJECT_NAME = 'Desafio'
    SECRET_KEY = environ.get('SERVER_KEY', 'ChAvE AleTorIa-d4b68abb2e9f7eb')#Apenas para o desafio
    APP_DIR = abspath(dirname(app.__file__))
    DEV_DB = join(APP_DIR, r'db.db')
    _SQLALCHEMY_DATABASE_NAME = environ.get('DATABASE', False) or PROJECT_NAME.lower()
    _SQLALCHEMY_DATABASE_HOST = environ.get('DB_HOST')
    _SQLALCHEMY_DATABASE_USERNAME = environ.get('DB_USER')
    _SQLALCHEMY_DATABASE_PASSWORD = environ.get('DB_PASS')
    _SQLALCHEMY_DATABASE_PORT = environ.get('DB_PORT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = join(APP_DIR, r'uploads/')
    MAX_UPLOAD_FILE_MB = 50
    MAX_CONTENT_PATH = 52428800
    ALLOWED_EXTENSIONS = {'csv', 'xlsx'}


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BaseConfig.DEV_DB}'
    MODE = 'dev'
    ENV = 'dev'

class ProductionConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{BaseConfig._SQLALCHEMY_DATABASE_USERNAME}:{BaseConfig._SQLALCHEMY_DATABASE_PASSWORD}@{BaseConfig._SQLALCHEMY_DATABASE_HOST}:{BaseConfig._SQLALCHEMY_DATABASE_PORT}/{BaseConfig._SQLALCHEMY_DATABASE_NAME}'
    # SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or f'postgresql://khtknuvbaeavvq:98b557036b61944f2912ccc6aa07b0c907352da55603ce611bb9b744da9398fa@ec2-23-23-128-222.compute-1.amazonaws.com:5432/dtf9faocttt57'
    SESSION_COOKIE_SECURE = False
    MODE = 'prod'
# 
config = {'development': DevelopmentConfig,
          'production': ProductionConfig}