# config.py
import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    # SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_KEY="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
    RESTPLUS_VALIDATE = True
    ERROR_404_HELP = False
    # db_name = os.getenv("DATABASE")
    # host = os.getenv("HOST")
    # role = os.getenv("ROLE")
    # pwd = os.getenv("PASSWORD")
    # port = os.getenv("PORT")


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    MODE="development"

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    # db_name = os.getenv("TEST_DB")
    MODE="testing"

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}