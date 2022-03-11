import requests
from dataclasses import dataclass
from selenium.webdriver.common.by import By

"""
DATA to be searched
"""
HOMEPAGE = 'http://127.0.0.1:5000/'
RESPONSE_PAGE= 'http://127.0.0.1:5000/round/funding-service-design'
SEARCH_BOX_ID = 'search'
SUBMIT_BUTTON_CLASS = 'govuk-button--secondary'
SEARCH_DATA_KEYWORD = 'fund'

@dataclass
class SeleniumElements:
    """
    GIVEN class is dataclass contains api host
    for homepage(search page) & rounds store page
    (response page) & driver for selenium chrome.
    """
    homepage: str
    response_page: str
    selenium_id: str
    selenium_class: str
    search_data: str
    driver: str
    
    def searching_element_max_time(self,sec):
        """
        GIVEN function in a class return max
        wait time for selenium elements to load up
        """
        return self.driver.implicitly_wait(sec)

    def get_data(self, browser):
        """
        GIVEN function searches selenium elements
        with given attributes from SeleniumElements class
        & return successful response
        """
        browser.get(self.homepage)
        self.searching_element_max_time(10)
        to_search = browser.find_element(By.ID, self.selenium_id)
        to_search.click()
        to_search.send_keys(self.search_data)
        submit = browser.find_element(By.CLASS_NAME,self.selenium_class)
        submit.click()
        fund_response = requests.get(self.homepage)
        assert fund_response.status_code == 200
        self.searching_element_max_time(10)
        href_links = browser.find_element(
            By.XPATH, '//*[@id="main-content"]/div[4]/div/h1/a')
        href_links.click()
        self.searching_element_max_time(10)
        rounds_response = requests.get(self.response_page)
        assert rounds_response.status_code == 200