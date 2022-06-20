from fsd_tech import configclass


@configclass
class DefaultConfig:

    SECRET_KEY = "dev"
    SESSION_COOKIE_NAME = "session_cookie"
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    FUND_STORE_API_HOST = "https://funding-service-design-fund-"
    "store-dev.london.cloudapps.digital"
    AUTHENTICATOR_HOST = "https://funding-service-design-"
    "authenticator-dev.london.cloudapps.digital"

    FUNDS_URL = "{host}/funds/{fund_id}"
    FUNDS_SEARCH_URL = "{host}/funds"

    ROUNDS_URL = "{host}/funds/{fund_id}/rounds"

    AUTHENTICATOR_MAGIC_LINK_URL = (
        "https://funding-service-design-authenticator-dev.london."
        "cloudapps.digital/service/magic-links/new?fund_id={fund_id}"
        "&round_id={round_id}"
    )

    FUND_STORE_API_HOST = "fund_store"
    AUTHENTICATOR_HOST = "authenticator_host"
