
import requests 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.common.by import By
import time



FUNDS_URL = 'http://127.0.0.1:5000/'
ROUNDS_URL= 'http://127.0.0.1:5000/round/funding-service-design'
SELECT_ID = 'search'
SELECT_CLASS = 'govuk-button--secondary'
DATA = 'fund'

def get_data(funds_url, rounds_url, selector_one,
             selector_two,data):
    """
    Given test function post the data from 
    discover store to funds store to grab the data 
    & when/if response & data is received from funds store
    then grabs the data from rounds store to grab the data &
    checks the response 
    """
    driver.get(funds_url)
    to_search = driver.find_element(By.ID, selector_one)
    time.sleep(1)
    to_search.click()
    to_search.send_keys(data)
    submit = driver.find_element(By.CLASS_NAME,selector_two)
    submit.click()
    fund_response = requests.get(FUNDS_URL)
    time.sleep(1)
    href_links = driver.find_element(
        By.XPATH, '//*[@id="main-content"]/div[4]/div/h1/a')
    href_links.click()
    time.sleep(1)
    rounds_response = requests.get(rounds_url)
    assert fund_response.status_code == 200
    assert rounds_response.status_code == 200
 

@pytest.fixture()
def test_setup(request):
    """
    GIVEN function  returns a Selenium Chrome driver 
    as a fixture for testing.
    """
    global driver
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    yield 
    driver.close()



def test_post_data_response(test_setup):
    """
    Given test function post the data from 
    discover store to funds store to grab the data 
    & when/if response & data is received from funds store
    then grabs the data from rounds store to grab the data &
    checks the response 
    """
    get_data(funds_url = FUNDS_URL, 
    rounds_url= ROUNDS_URL, selector_one=SELECT_ID,
    selector_two=SELECT_CLASS, data=DATA)

