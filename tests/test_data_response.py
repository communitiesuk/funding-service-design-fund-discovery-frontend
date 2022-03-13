from urllib.request import urlopen
from chromedriver_py import binary_path
from flask import url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from app.create_app import create_app
from flask import Response
from tests.model import (
    SearchSeleniumElements, SEARCH_PAGE, RESPONSE_PAGE,
    SEARCH_BOX_ID, SUBMIT_BUTTON_CLASS, ROUND_STORE_XPATH, SEARCH_KEYWORD)

class MyResponse(Response):
    '''Implements custom de-serialization method for response objects.'''
    @property
    def json(self):
        return 42

@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.response_class = MyResponse
    return app

@pytest.mark.usefixtures('live_server')
class TestLiveServer:
    """
    GIVEN class checks if routes are up & running
    """

    def test_server_is_up_and_running(self):
        url = url_for('discovery_bp.search_fund', _external=True)
        res = urlopen(url)
        assert b'search' in res.read()
        assert res.code == 200

    # def test_server_is_up_and_running(self):
    #     url = url_for('discovery_bp.fund_rounds',id = 'fund', _external=True)
    #     res = urlopen(url)
    #     assert res.code == 200






# def test_add_endpoint_to_live_server(live_server):
#     @live_server.app.route('/round/')
#     def test_endpoint():
#         return 'got it', 200
#     live_server.start()
#     res = urlopen(url_for('discovery_bp.fund_rounds',id = 'fund'
#     , _external=True))
#     assert res.code == 200


# def test_get_request(client, live_server):
#     @live_server.app.route('/round/', methods=['GET','POST'])
#     def get_endpoint():
#         return url_for('discovery_bp.fund_rounds',id = 'fund/',
#          _external=True)
#     live_server.start()
#     res = client.get(get_endpoint())
#     assert res.status_code == 200


# def test_load_data(live_server, client):
#     @live_server.app.route('/round/', methods=['POST'])
#     def load_data():
#         pass

#     live_server.start()

#     res = client.get(url_for('discovery_bp.fund_rounds', id = 'fund'))
#     assert res.status_code == 200



# @pytest.fixture(scope="class")
# def selenium_chrome_driver():
#     """
#     GIVEN function  returns a Selenium Chrome driver 
#     as a fixture for testing.
#     """
#     global chrome_driver
#     options = Options()
#     options.add_argument("--headless")
#     chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield 
#     chrome_driver.close()


@pytest.fixture(scope="class")
def selenium_chrome_driver():
    global chrome_driver
    """
    Returns a Selenium Chrome driver as a fixture for testing.
    using an installed Chromedriver from the .venv chromedriver_py package
    install location. Accessible with the
    @pytest.mark.uses_fixture('selenium_chrome_driver')
    :return: A selenium chrome driver.
    """
    service_object = Service(binary_path)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # TODO: set chrome_options.binary_location = ...
    #  (if setting to run in container or on GitHub)
    chrome_driver = webdriver.Chrome(
        service=service_object, options=chrome_options
    )
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("selenium_chrome_driver")
@pytest.mark.usefixtures('live_server')
def test_post_data_response():
    """
    Given test function post the data from 
    discover store to funds store to grab the data 
    & when/if response & data is received from funds store
    then grabs the data from rounds store to grab the data &
    checks the response 
    """
    search_response = SearchSeleniumElements(
        search_page=SEARCH_PAGE,
        response_page=RESPONSE_PAGE,
        selenium_id=SEARCH_BOX_ID,
        selenium_class=SUBMIT_BUTTON_CLASS,
        selenium_Xpath= ROUND_STORE_XPATH,
        search_data=SEARCH_KEYWORD,
        driver =chrome_driver)     
    search_response.get_data()


# urlopen(url_for('discovery_bp.search_fund', _external=True))
# urlopen(url_for('discovery_bp.fund_rounds', _external=True))


# def test_my_json_response(client):
#     res = client.get(url_for('discovery_bp.search_fund'))
#     assert res.json == 42

# @pytest.fixture()
# def flask_test_client():
#     """
#     Creates the test client we will be using to test the responses
#     from our app, this is a test fixture.
#     :return: A flask test client.
#     """
#     with create_app().test_client() as test_client:
#         yield test_client

# @pytest.mark.usefixtures("app")
# def test_search_fund__response(client):
#     res = client.get(url_for('discovery_bp.search_fund'))
#     assert res.json == 42

# @pytest.mark.usefixtures("app")
# def test_fund_store__response(client):
#     response = client.get(url_for('discovery_bp.fund_rounds'))
#     assert response.json == 42
    
