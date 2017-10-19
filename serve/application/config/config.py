#coding:utf-8


class DevelopmentConfig():
    DEBUG = True
    SECRET_KEY='123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./db/learoom.db'
    pass


class TestingConfig():
    DEBUG = True
    TESTING = True
    SECRET_KEY='123456'
    SQLALCHEMY_DATABASE_URI = ''
    pass

class ProductionConfig():
    DEBUG = False
    SECRET_KEY='123456'
    SQLALCHEMY_DATABASE_URI = ''
    pass


config = {
    
    "dev":DevelopmentConfig,
    "test":TestingConfig,
    "product":ProductionConfig,
    "default":DevelopmentConfig
}

