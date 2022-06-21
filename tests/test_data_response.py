import config
import pytest
from config.test import TestConfig
from flask import url_for


@pytest.mark.usefixtures("live_server")
def test_search_page_response(flask_test_client, mocker):
    """
    GIVEN class checks if route for search_fund
    is up & running
    """
    mocker.patch.object(config, "Config", TestConfig)
    url = url_for("discovery_bp.search_funds")
    response = flask_test_client.get(url, follow_redirects=True)
    assert b"search" in response.data
    assert response.status_code == 200


@pytest.mark.usefixtures("live_server")
def test_fund_exist(flask_test_client, mocker):
    mocker.patch.object(config, "Config", TestConfig)
    response = flask_test_client.get(
        url_for("discovery_bp.search_funds") + "?query_fund=fund",
        follow_redirects=True,
    )
    assert b"fund" in response.data


@pytest.mark.usefixtures("live_server")
def test_fund_not_found(flask_test_client, mocker):
    mocker.patch.object(config, "Config", TestConfig)
    response = flask_test_client.get(
        url_for("discovery_bp.search_funds") + "/?query_fund=fund",
        follow_redirects=True,
    )
    assert b"blloobllaalive" not in response.data


@pytest.mark.usefixtures("live_server")
def test_route_response_404(flask_test_client, mocker):
    mocker.patch.object(config, "Config", TestConfig)
    response = flask_test_client.get("/rubbish_url", follow_redirects=True)
    assert response.status_code == 404


@pytest.mark.usefixtures("live_server")
def test_rounds_exist(flask_test_client, mocker):
    mocker.patch.object(config, "Config", TestConfig)
    response = flask_test_client.get(
        url_for("discovery_bp.fund_rounds", fund_id="funding-service-design"),
        follow_redirects=True,
    )
    assert b"SUMMER" in response.data
    assert b"SPRING" in response.data
    assert b"AUTUMN" in response.data
