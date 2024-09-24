"""

    3.  Test scroll pe verticala pagina principala.
        Acest test va face Scroll pe verticala a paginii principale a site-ului ales pentru testare.

"""




from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time




# Accesare browser CHROME
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options = chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


# 3. Test scroll pe verticala pagina principala
def test_scroll(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(3)

    # Test scroll pe verticala pagina principala
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 24:
            break
        time.sleep(1.1)
    time.sleep(3)