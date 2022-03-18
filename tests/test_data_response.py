from urllib.request import urlopen

import pytest
from app.create_app import create_app
from flask import url_for


@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.mark.usefixtures("live_server")
class TestSearchPage:
    """
    GIVEN class checks if route for search_fund
    is up & running
    """

    def test_search_page_response(self):
        url = url_for("discovery_bp.search_funds", _external=True)
        res = urlopen(url)
        assert b"search" in res.read()
        assert res.code == 200


@pytest.fixture()
def flask_test_client():
    """
    Creates the test client we will be using to test the responses
    from our app, this is a test fixture.
    :return: A flask test client.
    """
    with create_app().test_client() as test_client:
        yield test_client


@pytest.mark.usefixtures("live_server")
def test_search_page_found(flask_test_client):
    response = flask_test_client.get(
        url_for("discovery_bp.search_funds") + "/?search_items=fund",
        follow_redirects=True,
    )
    assert b"Funding Service Design" in response.data


@pytest.mark.usefixtures("live_server")
def test_search_page_response(flask_test_client):
    response = flask_test_client.get("/rubbish_url", follow_redirects=True)
    assert response.status_code == 404


@pytest.mark.usefixtures("live_server")
def test_search_page_not_found(flask_test_client):
    response = flask_test_client.get(
        url_for("discovery_bp.search_funds") + "/?search_items=bloolive",
        follow_redirects=True,
    )
    assert b"fund" not in response.data


@pytest.mark.usefixtures("live_server")
def test_round_page_found(flask_test_client):
    response = flask_test_client.get(
        url_for("discovery_bp.funds", fund_id="funding-service-design"),
        follow_redirects=True,
    )
    assert b"SUMMER" in response.data
    assert b"SPRING" in response.data
    assert b"AUTUMN" in response.data
