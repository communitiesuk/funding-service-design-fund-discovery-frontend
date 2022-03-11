from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from tests.data import (
    SeleniumElements, HOMEPAGE, RESPONSE_PAGE,
    SEARCH_BOX_ID, SUBMIT_BUTTON_CLASS, SEARCH_DATA_KEYWORD)

@pytest.fixture(scope="class")
def selenium_chrome_driver():
    """
    GIVEN function  returns a Selenium Chrome driver 
    as a fixture for testing.
    """
    global driver
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield 
    driver.close()


@pytest.mark.usefixtures("selenium_chrome_driver")
def test_post_data_response():
    """
    Given test function post the data from 
    discover store to funds store to grab the data 
    & when/if response & data is received from funds store
    then grabs the data from rounds store to grab the data &
    checks the response 
    """

    search_response = SeleniumElements(homepage=HOMEPAGE,
    response_page=RESPONSE_PAGE, selenium_id=SEARCH_BOX_ID,
    selenium_class=SUBMIT_BUTTON_CLASS, search_data=SEARCH_DATA_KEYWORD, driver =driver)
    search_response.get_data(driver)
