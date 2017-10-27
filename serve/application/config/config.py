#coding:utf-8


class DevelopmentConfig():
    DEBUG = True
    SECRET_KEY='123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./application/db/learoom.db'
    GIT_VERSION_DISPLAY = False
    pass


class TestingConfig():
    DEBUG = True
    TESTING = True
    SECRET_KEY='123456'
    SQLALCHEMY_DATABASE_URI = ''
    GIT_VERSION_DISPLAY = False
    pass

class ProductionConfig():
    DEBUG = False
    SECRET_KEY='123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./application/db/learoom.db'
    GIT_VERSION_DISPLAY = False
    pass


config = {
    
    "dev":DevelopmentConfig,
    "test":TestingConfig,
    "product":ProductionConfig,
    "default":DevelopmentConfig
}

