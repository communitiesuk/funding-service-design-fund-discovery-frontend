"""
Contains test configuration.
"""
import pytest
from app.create_app import create_app


@pytest.fixture()
def app():
    app = create_app()
    return app
