"""
Contains test configuration.
"""
import os
from unittest import mock

import pytest
from app.create_app import create_app


@pytest.fixture()
def flask_test_client(mocker):
    """
    Creates the test client we will be using to test the responses
    from our app, this is a test fixture.
    :return: A flask test client.
    """
    with create_app().test_client() as test_client:
        yield test_client
        os.environ["FLASK_DEBUG"] = "0"


@pytest.fixture(autouse=True, scope="session")
def mock_env_vars():
    with mock.patch.dict(
        os.environ, {"FLASK_ENV": "unit_test", "FLASK_DEBUG": "1"}
    ):
        yield


@pytest.fixture(scope="session")
def app():
    app = create_app()
    yield app
