from os import environ
import os
from config.envs.default import DefaultConfig
from distutils.util import strtobool
from fsd_utils import configclass
import logging


@configclass
class DevelopmentConfig(DefaultConfig):

    SECRET_KEY = "dev_secret_key"
    FUND_STORE_API_HOST = os.getenv("FUND_STORE_API_HOST", "fund_store")
    AUTHENTICATOR_HOST = os.getenv("AUTHENTICATOR_HOST", "https://funding-service-design-authenticator-dev.london.cloudapps.digital")
    USE_LOCAL_DATA = strtobool(environ.get("USE_LOCAL_DATA", "True"))

    if AUTHENTICATOR_HOST:
        AUTHENTICATOR_MAGIC_LINK_URL = (
            AUTHENTICATOR_HOST
            + "/service/magic-links/new?fund_id={fund_id}&round_id={round_id}"
        )

    # Logging
    FSD_LOG_LEVEL = logging.DEBUG
    FORCE_HTTPS = False
