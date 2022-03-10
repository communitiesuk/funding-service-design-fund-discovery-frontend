from selenium import webdriver
from axe_selenium_python import Axe
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
import pytest
from app.config import ACCESSIBILITY_ENDPOINTS
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture()
def test_setup():
    global driver
    service_object = Service(binary_path)
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield 
    driver.close()

@pytest.mark.accessibility
def test_run_axe(test_setup):
    for URL in ACCESSIBILITY_ENDPOINTS:
        driver.get(URL)
        axe = Axe(driver)
        # Inject axe-core javascript into page.
        axe.inject()
        # Run axe accessibility checks.
        results = axe.run()
        # Write results to file
        axe.write_results(results, 'tests/accessibility_report.json')
        # Assert no of violations are found
        assert len(results["violations"]) <= 1
        assert (
            len(results["violations"]) == 0
            or results["violations"][0]["impact"] == "minor"
        ), axe.report(results["violations"])







