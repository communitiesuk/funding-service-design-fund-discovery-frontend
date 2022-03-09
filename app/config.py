"""Flask configuration."""
import os
from os import path

"""
Application Config
"""
SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME") or "session_cookie"
STATIC_FOLDER = "static"
TEMPLATES_FOLDER = "templates"


"""
APIs Config: contains api host imported from manifest.yml.
& string variables set for test_fund & test_round in the event of 
host api doesn't not work/respond
"""
TEST_FUND_STORE_API_HOST = "fund_store"
TEST_ROUNDS_STORE_API_HOST = "rounds_store"

FUND_STORE_API_HOST = (
    os.environ.get("FUND_STORE_API_HOST") or TEST_FUND_STORE_API_HOST
)

ROUND_STORE_API_HOST = (
    os.environ.get("ROUND_STORE_API_HOST")
    or TEST_ROUNDS_STORE_API_HOST
)


