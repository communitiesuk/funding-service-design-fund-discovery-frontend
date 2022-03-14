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

FUND_STORE_API_HOST="https://funding-service-design-fund-store-dev.london.cloudapps.digital"

ROUND_STORE_API_HOST="https://funding-service-design-round-store-dev.london.cloudapps.digital"

FUND_ENDPOINT = 'funds/search/'
ROUND_ENDPOINT = 'fund'
ROUND_ID = "funding-service-design"



def get_endpoints():
    """
    GIVEN function return development & production urls
    for accessibility tests if FLASK_ENV 
    is in development or production
    """
    if FLASK_ENV =="development":
        return (
            'http://127.0.0.1:5000/',
             'http://127.0.0.1:5000/round/funding-service-design'
        )
        
    else:
        return  (
            "https://funding-service-design-fund-discovery-dev.london.cloudapps.digital",
            "https://funding-service-design-fund-discovery-dev.london.cloudapps.digital/round/funding-service-design"
            
        )

