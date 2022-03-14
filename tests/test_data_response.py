from urllib.request import urlopen
from flask import url_for
import pytest
from app.create_app import create_app

@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app

@pytest.mark.usefixtures('live_server')
class TestLiveServer:
    """
    GIVEN class checks if routes are up & running
    """

    def test_search_page_response(self):
        url = url_for('discovery_bp.search_fund', _external=True)
        res = urlopen(url)
        assert b'search' in res.read()
        assert res.code == 200



