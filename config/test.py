from config.default import DefaultConfig
from fsd_tech import configclass


@configclass
class TestConfig(DefaultConfig):

    USE_LOCAL_DATA = False
