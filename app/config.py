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
& string variables set for test_fund & test_round in the event of
host api doesn't not work/respond
"""

TEST_FUND_STORE_API_HOST = "fund_store"
TEST_ROUND_STORE_API_HOST = "round_store"


FUND_STORE_API_HOST = (
    os.environ.get("FUND_STORE_API_HOST") or TEST_FUND_STORE_API_HOST
)


ROUND_STORE_API_HOST = (
    os.environ.get("ROUND_STORE_API_HOST") or TEST_ROUND_STORE_API_HOST
)


FUND_ENDPOINT = "funds"
FUND_SEARCH_ENDPOINT = "search"
ROUND_ENDPOINT = "fund"


def get_endpoints():
    """
    GIVEN function return development & production urls
    for accessibility tests if FLASK_ENV
    is in development or production.
    """
    if FLASK_ENV == "development":
        return (
            "http://127.0.0.1:5000/",
            "http://127.0.0.1:5000/round/funding-service-design",
        )

    else:
        return (
            "https://funding-service-design-fund-discovery-dev.london.cloudapps.digital",  # noqa
            "https://funding-service-design-fund-discovery-dev.london.cloudapps.digital/round/funding-service-design",  # noqa
        )
