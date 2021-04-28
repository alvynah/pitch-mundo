import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cocoh:kitkAt10@localhost/pitchmundo'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = "postgresql://rbocsdssvyutqf:99831c8ebddd7c0f123f8bab7a9bae10d3b8c62b25c3990db38ae056ef0ac0a7@ec2-54-152-185-191.compute-1.amazonaws.com:5432/d223617h6tq3h?sslmode=require"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cocoh:kitkAt10@localhost/pitchmundo_test'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cocoh:kitkAt10@localhost/pitchmundo'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig

}
