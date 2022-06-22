from config.default import DefaultConfig
from fsd_tech import configclass


@configclass
class DevelopmentConfig(DefaultConfig):

    USE_LOCAL_DATA = True
    FUND_STORE_API_HOST = "fund_store"
