

# default config
class BaseConfig(object):
    DEBUG                   = False
    SECRET_KEY              = "]\x9f\x85nj\xe3\xb4;\xea\xe3\xfb\xb2\xe1\x14I\xff\x16\x9f\xa6'\xa0,\x11\x92"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db\sample.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False