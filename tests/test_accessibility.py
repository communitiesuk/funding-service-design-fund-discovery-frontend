import pytest
from axe_selenium_python import Axe
from flask import request
from flask import url_for
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.accessibility
def test_run_axe(live_server):

    live_server.start()

    endpoints = [
        url_for("discovery_bp.search_funds"),
        url_for("discovery_bp.fund_rounds", fund_id="harry-s-breakfast-fund"),
    ]

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    for url in endpoints:
        url = str(url)
        driver.get(request.root_url[:-1] + url)
        axe = Axe(driver)
        # Inject axe-core javascript into page.
        axe.inject()
        # Run axe accessibility checks.
        results = axe.run()
        # Write results to file
        axe.write_results(results, "tests/accessibility_report.json")
        # Assert no of violations are found
        assert len(results["violations"]) <= 2
        assert (
            len(results["violations"]) == 0
            or results["violations"][0]["impact"] == "minor"
        ), axe.report(results["violations"])
