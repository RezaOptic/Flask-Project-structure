
class DefaultConfig(object):
    pass


class DevConfig(DefaultConfig):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    DEBUG = False


class TestConfig(DefaultConfig):
    TESTING = True
