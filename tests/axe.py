from selenium import webdriver
from axe_selenium_python import Axe
from pylenium.driver import Pylenium

CHROME_DRIVER_PATH = "/Users/ram/Downloads/CHROME-DRIVER/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

try:
    driver.get("http://127.0.0.1:5000/round/funding-service-design")

except:
    driver.get("http://127.0.0.1:5000/")
finally:

    # Instantiate Axe
    axe = Axe(driver)
    # Inject axe-core javascript into the page
    axe.inject()
    # Run axe for accessability checks
    results = axe.run()
    # Write results onto json file
    # axe.write_results(results, 'test/accessability_test_report.json')
    # Close the driver
    driver.close()
    # Assert no violations are found
    assert len(results['violations']) == 0, axe.report(results['violations'])
    #quit the driver
    driver.quit()


     
def test_endpoint():
       pass  