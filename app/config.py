"""Flask configuration."""
import os

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

FUND_STORE_API_HOST="https://funding-service-design-fund-store-dev.london.cloudapps.digital"

ROUND_STORE_API_HOST="https://funding-service-design-round-store-dev.london.cloudapps.digital"

FUND_ENDPOINT = 'funds/search/'
ROUND_ENDPOINT = 'fund'
ROUND_ID = "funding-service-design"


ACCESSIBILITY_ENDPOINTS = [   
    "http://127.0.0.1:5000/round/funding-service-design", 
    "http://127.0.0.1:5000/",
    "https://funding-service-design-fund-discovery-dev.london.cloudapps.digital/round/funding-service-design", 
    "https://funding-service-design-fund-discovery-dev.london.cloudapps.digital"
]
