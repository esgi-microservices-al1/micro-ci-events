import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(
        os.getenv("DB_USER", "micro_ci_events"),
        os.getenv("DB_PASSWORD", "micro_ci_events"),
        os.getenv("DB_HOST", "mysql1"),
        os.getenv("DB_NAME", "micro-ci-events")
    )
    DEBUG = True

key = Config.SECRET_KEY