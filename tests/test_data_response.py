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
        url = url_for("discovery_bp.search_fund", _external=True)
        res = urlopen(url)
        assert b"search" in res.read()
        assert res.code == 200
