import os

from config.environments.default import DefaultConfig
from distutils.util import strtobool
from fsd_utils import configclass


@configclass
class DevelopmentConfig(DefaultConfig):

    USE_LOCAL_DATA = strtobool(os.environ.get("USE_LOCAL_DATA", "True"))
    FUND_STORE_API_HOST = os.environ.get("FUND_STORE_API_HOST", "fund_store")
