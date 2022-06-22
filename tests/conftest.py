"""
Contains test configuration.
"""
import os

import config
import pytest
from app.create_app import create_app
from config.unit_test import UnitTestConfig


@pytest.fixture()
def flask_test_client(mocker):
    """
    Creates the test client we will be using to test the responses
    from our app, this is a test fixture.
    :return: A flask test client.
    """
    os.environ["FLASK_DEBUG"] = "1"
    mocker.patch.object(config, "Config", UnitTestConfig)
    with create_app().test_client() as test_client:
        yield test_client
        os.environ["FLASK_DEBUG"] = "0"


@pytest.fixture(scope="session")
def app():
    os.environ["FLASK_DEBUG"] = "1"
    app = create_app()
    yield app
    os.environ["FLASK_DEBUG"] = "0"
