"""
Contains test configuration.
"""
import pytest


@pytest.fixture()
def flask_test_client():
    """
    Creates the test client we will be using to test the responses
    from our app, this is a test fixture.
    :return: A flask test client.
    """
    from app.create_app import create_app

    with create_app().test_client() as test_client:
        yield test_client


@pytest.fixture(scope="session")
def app():
    from app.create_app import create_app

    app = create_app()
    yield app
