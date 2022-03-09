from selenium import webdriver
from axe_selenium_python import Axe
from app.discovery.models._endpoints import TEST_ACCESSIBILITY_ENDPOINTS
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.mark.accessibility
@pytest.fixture()
def test_setup():
    global driver
    CHROME_DRIVER_PATH = "/Users/ram/Downloads/CHROME-DRIVER/chromedriver"
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service) 
    yield 
    driver.close()



def test_run_axe(test_setup):
    for URL in TEST_ACCESSIBILITY_ENDPOINTS:
        driver.get(URL)
        axe = Axe(driver)
        # Inject axe-core javascript into page.
        axe.inject()
        # Run axe accessibility checks.
        results = axe.run()
        # Write results to file
        axe.write_results(results, 'tests/accessibility_test_report.json')
        # Assert no of violations are found
        assert len(results["violations"]) <= 1
        assert (
            len(results["violations"]) == 0
            or results["violations"][0]["impact"] == "minor"
        ), axe.report(results["violations"])







