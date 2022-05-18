"""Flask configuration."""
import os

"""
Application Config
"""
SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME") or "session_cookie"
STATIC_FOLDER = "static"
TEMPLATES_FOLDER = "templates"
FLASK_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FLASK_ENV = os.environ.get("FLASK_ENV")

"""
APIs Config: contains api host imported from manifest.yml.
& string variables in the event of
host api doesn't not work/respond
"""

TEST_FUND_STORE_API_HOST = "fund_store"
TEST_ROUND_STORE_API_HOST = "round_store"
TEST_AUTHENTICATOR_API_HOST = "authenticator_host"


FUND_STORE_API_HOST = (
    os.environ.get("FUND_STORE_API_HOST") or TEST_FUND_STORE_API_HOST
)


ROUND_STORE_API_HOST = (
    os.environ.get("ROUND_STORE_API_HOST") or TEST_ROUND_STORE_API_HOST
)


AUTHENTICATOR_HOST = (
    os.environ.get("AUTHENTICATOR_STORE_API_HOST")
    or os.environ.get("TEST_AUTHENTICATOR_STORE_API_HOST")
    or TEST_AUTHENTICATOR_API_HOST
)

FUNDS_URL = "{host}/funds/{fund_id}"
FUNDS_SEARCH_URL = "{host}/funds/search/?"

ROUNDS_URL = "{host}/funds/{fund_id}/rounds"


def get_endpoints():
    """
    GIVEN function return development & production urls
    for accessibility tests if FLASK_ENV
    is in development or production.
    """
    if FLASK_ENV == "development":
        return (
            "http://127.0.0.1:5000",
            "http://127.0.0.1:5000/round/funding-service-design",
        )

    else:
        return (
            "https://funding-service-design-fund-discovery-dev.london.cloudapps.digital",  # noqa
            "https://funding-service-design-fund-discovery-dev.london.cloudapps.digital/round/funding-service-design",  # noqa
        )
