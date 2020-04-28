class Config:
    SECRET_KEY = 'clave'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql://root:@localhost/project_web_python'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = ''
    MAIL_PORT = ''
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql://root:@localhost/project_web_python_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}
