"""
Contains test configuration.
"""
import pytest
from app.create_app import create_app


@pytest.fixture(scope="session")
def app():

    app = create_app()
    yield app
