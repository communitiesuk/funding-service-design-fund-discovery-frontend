from config.default import DefaultConfig
from fsd_tech import configclass


@configclass
class DevelopmentConfig(DefaultConfig):

    FUND_STORE_API_HOST = "fund_store"
    AUTHENTICATOR_HOST = "authenticator_host"
