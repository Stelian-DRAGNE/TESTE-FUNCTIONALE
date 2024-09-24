"""

    10. Test accesare sectiunea 'BLOG'.
        Acest test va efectua accesarea sectiunii "BLOG", sectiune prezenta in cadrul site-ului ales pentru testare.

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


# 10. Test accesare sectiune 'BLOG'
def test_accesare_blog(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(3)

    # Test accesare sectiunea 'BLOG'
    blog = browser.find_element(By.XPATH, '//*[@id="main-menu"]/div/ul/li[5]/a')
    blog.click()
    assert blog, "Sectiunea 'BLOG' nu este disponibila."
    time.sleep(2)

    # Test scroll pe verticala pagina sectiune 'BLOG'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 10:
            break
        time.sleep(1.1)
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(2)

    # Test accesare articol dorit din sectiunea 'BLOG' -> 'Cum să aşez şi să reglez corect casca pentru copil'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 8:
            break
        time.sleep(1.1)
    time.sleep(2)
    
    browser.get("https://www.mosionroata.ro/blog/cum-sa-reglezi-corect-casca-pentru-copil.html")
    time.sleep(2)

    # Test scroll pe verticala pagina sectiune 'BLOG' -> 'Cum să aşez şi să reglez corect casca pentru copil'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 18:
            break
        time.sleep(1.1)
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(3)