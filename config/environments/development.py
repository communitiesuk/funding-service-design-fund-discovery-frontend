import os

from config.environments.default import DefaultConfig
from fsd_utils import configclass
from distutils.util import strtobool


@configclass
class DevelopmentConfig(DefaultConfig):

    USE_LOCAL_DATA = strtobool(os.environ.get("USE_LOCAL_DATA", "True"))
    FUND_STORE_API_HOST = os.environ.get("FUND_STORE_API_HOST", "fund_store")
