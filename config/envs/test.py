import logging
from os import environ

from config.envs.default import DefaultConfig
from fsd_utils import configclass


@configclass
class TestConfig(DefaultConfig):
    SECRET_KEY = environ.get("SECRET_KEY", "test_secret_key")

    # Logging
    FSD_LOG_LEVEL = logging.INFO
