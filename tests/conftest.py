"""
Contains test configuration.
"""
import pytest
from app.create_app import create_app
from tests.mocks.account_data_mocks import account_methods_mock


@pytest.fixture(autouse=True)
def mock_account_store(monkeypatch):

    import app.discovery.models.data

    monkeypatch.setattr(
        app.discovery.models.data.account_methods,
        "get_account",
        account_methods_mock.get_account,
    )
    monkeypatch.setattr(
        app.discovery.models.data.account_methods,
        "post_account",
        account_methods_mock.post_account,
    )


@pytest.fixture(scope="session")
def app():

    app = create_app()
    yield app
