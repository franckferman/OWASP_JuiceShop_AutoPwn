from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils import check_browser

def setup_webdriver(browser, wait_time):
    check_browser(browser)
 
    driver = None
    wait = None
 
    try:
        if browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser in ['chrome', 'chromium']:
            driver = webdriver.Chrome()
        elif browser == 'safari':
            driver == webdriver.Safari()
        elif browser == 'edge':
            driver == webdriver.Edge()
        else:
            raise ValueError("Browser not supported")
 
        wait = WebDriverWait(driver, wait_time)
        return driver, wait
 
    except WebDriverException as e:
        if driver:
            driver.quit()
        raise ValueError(f"{browser.capitalize()} was unable to initialize") from e
