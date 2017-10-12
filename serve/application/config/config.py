#coding:utf-8


class DevelopmentConfig():
    DEBUG = True
    SECRET_KEY='123456'
    pass


class TestingConfig():
    DEBUG = True
    TESTING = True
    SECRET_KEY='123456'
    pass

class ProductionConfig():
    DEBUG = False
    SECRET_KEY='123456'
    pass


config = {
    
    "dev":DevelopmentConfig,
    "test":TestingConfig,
    "product":ProductionConfig,
    "default":DevelopmentConfig
}

