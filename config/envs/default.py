from os import environ
from os import path
from pathlib import Path

from fsd_utils import configclass
import logging


@configclass
class DefaultConfig:

    SECRET_KEY = environ.get("SECRET_KEY")
    SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")
    FLASK_ROOT = str(Path(__file__).parent.parent.parent)
    STATIC_FOLDER = environ.get("STATIC_FOLDER", "static")
    TEMPLATES_FOLDER = environ.get("TEMPLATES_FOLDER", "templates")
    FUND_STORE_API_HOST = environ.get("FUND_STORE_API_HOST")
    AUTHENTICATOR_HOST = environ.get("AUTHENTICATOR_HOST")
    USE_LOCAL_DATA = False
    FUNDS_URL = "{host}/funds/{fund_id}"
    FUNDS_SEARCH_URL = "{host}/funds"

    ROUNDS_URL = "{host}/funds/{fund_id}/rounds"

    if AUTHENTICATOR_HOST:
        AUTHENTICATOR_MAGIC_LINK_URL = (
            AUTHENTICATOR_HOST
            + "/service/magic-links/new?fund_id={fund_id}&round_id={round_id}"
        )

    FLASK_ENV = environ.get("FLASK_ENV")

    # Logging
    FSD_LOG_LEVEL = logging.WARNING

    # Frontend
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True

    # Talisman Config
    FORCE_HTTPS = True

    # Content Security Policy
    SECURE_CSP = {
        "default-src": "'self'",
        "script-src": [
            "'self'",
            "'sha256-+6WnXIl4mbFTCARd8N3COQmT3bJJmo32N8q8ZSQAIcU='",
            "'sha256-l1eTVSK8DTnK8+yloud7wZUqFrI0atVo6VlC6PJvYaQ='",
        ],
        "img-src": ["data:", "'self'"],
    }

    # Security headers and other policies
    FSD_REFERRER_POLICY = "strict-origin-when-cross-origin"
    FSD_SESSION_COOKIE_SAMESITE = "Lax"
    FSD_PERMISSIONS_POLICY = {"interest-cohort": "()"}
    FSD_DOCUMENT_POLICY = {}
    FSD_FEATURE_POLICY = {
        "microphone": "'bob'",
        "camera": "'none'",
        "geolocation": "'none'",
    }

    DENY = "DENY"
    SAMEORIGIN = "SAMEORIGIN"
    ALLOW_FROM = "ALLOW-FROM"
    ONE_YEAR_IN_SECS = 31556926

    TALISMAN_SETTINGS = {
        "feature_policy": FSD_FEATURE_POLICY,
        "permissions_policy": FSD_PERMISSIONS_POLICY,
        "document_policy": FSD_DOCUMENT_POLICY,
        "force_https": FORCE_HTTPS,
        "force_https_permanent": False,
        "force_file_save": False,
        "frame_options": "SAMEORIGIN",
        "frame_options_allow_from": None,
        "strict_transport_security": True,
        "strict_transport_security_preload": True,
        "strict_transport_security_max_age": ONE_YEAR_IN_SECS,
        "strict_transport_security_include_subdomains": True,
        "content_security_policy": SECURE_CSP,
        "content_security_policy_report_uri": None,
        "content_security_policy_report_only": False,
        "content_security_policy_nonce_in": None,
        "referrer_policy": FSD_REFERRER_POLICY,
        "session_cookie_secure": True,
        "session_cookie_http_only": True,
        "session_cookie_samesite": FSD_SESSION_COOKIE_SAMESITE,
        "x_content_type_options": True,
        "x_xss_protection": True,
    }

