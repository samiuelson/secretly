import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(basedir, 's3crtly.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_migrate_repository')
BASIC_AUTH_USERNAME = 'login'
BASIC_AUTH_PASSWORD = 'pass'