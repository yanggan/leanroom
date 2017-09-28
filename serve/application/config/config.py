#coding:utf-8


class DevelopmentConfig():
    DEBUG = True
    pass


class TestingConfig():
    DEBUG = True
    TESTING = True
    pass

class ProductionConfig():
    DEBUG = False
    pass


config = {
    
    "dev":DevelopmentConfig,
    "test":TestingConfig,
    "product":ProductionConfig,
    "default":DevelopmentConfig
}

