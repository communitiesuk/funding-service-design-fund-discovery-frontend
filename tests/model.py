# import requests
# from dataclasses import dataclass
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.errorhandler import NoSuchElementException
# from json import JSONEncoder
# """
# DATA to be searched
# """
# SEARCH_PAGE = 'http://127.0.0.1:5000/'
# RESPONSE_PAGE= 'http://127.0.0.1:5000/round/funding-service-design'
# SEARCH_BOX_ID = 'search'
# SUBMIT_BUTTON_CLASS = 'govuk-button--secondary'
# ROUND_STORE_XPATH = '//*[@id="main-content"]/div[4]/div/h1/a'
# SEARCH_KEYWORD = 'fund'

# @dataclass
# class SearchSeleniumElements:
#     """
#     GIVEN class is dataclass contains api host
#     for homepage(search page) & rounds store page
#     (response page) & driver for selenium chrome.
#     """
#     search_page: str
#     response_page: str
#     selenium_id: str
#     selenium_class: str
#     selenium_Xpath: str
#     search_data: str
#     driver: str

#     def default(self, o):
#         try:
#             iterable = iter(o)
#         except TypeError:
#             pass
#         else:
#             return list(iterable)
#         return JSONEncoder.default(self, o)

#     def element_search_max_time(self,sec):
#         """
#         GIVEN function in a class return max
#         wait time for selenium elements or page 
#         to load up
#         """
#         return self.driver.implicitly_wait(sec)

#     def get_data(self):
#         """
#         GIVEN function searches selenium elements
#         with given attributes from SeleniumElements class
#         & return successful response
#         """
#         # load up search page
#         self.driver.get(self.search_page)

#         # find search box
#         try:
#             self.element_search_max_time(30)  
#             to_search = self.driver.find_element(
#                 By.ID, self.selenium_id)
#         except NoSuchElementException:
#             assert f"No selenium element {self.selenium_id} found  in {self.search_page}"
#         finally:
#             self.element_search_max_time(30)   
#             to_search.click()
#             to_search.send_keys(self.search_data)

#         # find submit button for search box
#         try:
#             self.element_search_max_time(30)    
#             submit = self.driver.find_element(By.CLASS_NAME,self.selenium_class)
#         except NoSuchElementException:
#              assert f"No selenium element {self.selenium_class} found in {self.search_page}"    
#         finally:     
#             submit.click()
#             self.element_search_max_time(30)
#             fund_response = requests.get(self.search_page)
#             assert fund_response.status_code == 200

#         # find round store fund_id XPATH
#         try:
#             self.element_search_max_time(30)
#             round_store_href_link = self.driver.find_element(
#                 By.XPATH, self.selenium_Xpath )
#         except NoSuchElementException:
#             assert f"No selenium element {self.selenium_Xpath} in {self.search_page}" 
#         finally:           
#             round_store_href_link.click()
#             self.element_search_max_time(30)
#             rounds_response = requests.get(self.response_page)
#             assert rounds_response.status_code == 200

            