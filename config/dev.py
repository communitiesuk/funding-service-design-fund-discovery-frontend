from config.default import DefaultConfig
from fsd_tech import configclass


@configclass
class DevConfig(DefaultConfig):

    USE_LOCAL_DATA = False
