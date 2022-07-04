from config.envs.default import DefaultConfig
from fsd_utils import configclass


@configclass
class UnitTestConfig(DefaultConfig):

    SECRET_KEY = "dev_secret_key"
    SESSION_COOKIE_NAME = "session_cookie"
    FUND_STORE_API_HOST = "fund_store"
    AUTHENTICATOR_HOST = "https://funding-service-design-authenticator-dev.london.cloudapps.digital"

    if AUTHENTICATOR_HOST:
        AUTHENTICATOR_MAGIC_LINK_URL = (
                AUTHENTICATOR_HOST
                + "/service/magic-links/new?fund_id={fund_id}&round_id={round_id}"
        )
    USE_LOCAL_DATA = True
