from config.environments.default import DefaultConfig
from fsd_utils import configclass


@configclass
class UnitTestConfig(DefaultConfig):

    USE_LOCAL_DATA = True
    FUND_STORE_API_HOST = "fund_store"
