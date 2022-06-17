"""
Contains test configuration.
"""
from os import environ

import pytest
from app.create_app import create_app


@pytest.fixture()
def flask_test_client():
    """
    Creates the test client we will be using to test the responses
    from our app, this is a test fixture.
    :return: A flask test client.
    """
    with create_app(testing=True).test_client() as test_client:
        yield test_client


@pytest.fixture(scope="session")
def app():
    environ["FLASK_ENV"] = "development"
    app = create_app()
    return app
