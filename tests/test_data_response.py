import os
from pickle import PickleBuffer
import random
import string
from urllib.request import urlopen
from tests.mocks.account_data_mocks import account_methods_mock

import pytest
import requests
from app.create_app import create_app
from app.discovery.models.data import account_methods
from flask import request
from flask import url_for
import pickledb

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
def test_search_page_response(flask_test_client):
    """
    GIVEN class checks if route for search_fund
    is up & running
    """
    url = url_for("discovery_bp.search_funds")
    response = flask_test_client.get(url, follow_redirects=True)
    assert b"search" in response.data
    assert response.status_code == 200


@pytest.mark.usefixtures("live_server")
def test_fund_exist(flask_test_client):
    response = flask_test_client.get(
        url_for("discovery_bp.search_funds") + "/?query_fund=fund",
        follow_redirects=True,
    )
    assert b"fund" in response.data


@pytest.mark.usefixtures("live_server")
def test_fund_not_found(flask_test_client):
    response = flask_test_client.get(
        url_for("discovery_bp.search_funds") + "/?query_fund=fund",
        follow_redirects=True,
    )
    assert b"blloobllaalive" not in response.data


@pytest.mark.usefixtures("live_server")
def test_route_response_404(flask_test_client):
    response = flask_test_client.get("/rubbish_url", follow_redirects=True)
    assert response.status_code == 404


@pytest.mark.usefixtures("live_server")
def test_rounds_exist(flask_test_client):
    response = flask_test_client.get(
        url_for("discovery_bp.fund_rounds", fund_id="funding-service-design"),
        follow_redirects=True,
    )
    assert b"SUMMER" in response.data
    assert b"SPRING" in response.data
    assert b"AUTUMN" in response.data

def test_page_creates_email(live_server):
    """
    GIVEN The flask test client
    WHEN we make a get request to the email confirmation page
    containing a random  email address.
    THEN we expect an account with the corresponding email
    address to exist in the account store.
    """

    live_server.start()

    random_string = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=10)
    )
    created_email = f"{random_string}@delete_me.com"
    url = request.root_url + url_for("discovery_bp.account_info_route", application_url = "www.google.com", email =created_email)
    requests.get(url)

    db = pickledb.load("./tests/mock_db.db", True)

    emailed_created = db.exists(created_email)

    # deletes temp fake db.
    os.remove("./tests/mock_db.db")

    assert emailed_created
