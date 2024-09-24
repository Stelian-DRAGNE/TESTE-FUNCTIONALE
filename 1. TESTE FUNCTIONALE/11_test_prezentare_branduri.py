"""

    11. Test accesare sectiunea "BRANDURI"
        Acest test va prezenta lista brand-urilor comercializate de catre site-ul ales pentru testare, in ordinea numarului de pagini disponibile in acesta sectiune a site-ului.

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


# 11. Test accesare sectiunea 'BRANDURI'
def test_prezentare_branduri(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(2)

    # Test accesare sectiune 'BRANDURI' si vizualizare pagini cu marcile comercializate
    # Test accesare pagina 1 din sectiunea 'BRANDURI'
    branduri_pagina_1 = browser.find_element(By.XPATH, '//*[@id="main-menu"]/div/ul/li[6]/a')
    branduri_pagina_1.click()
    assert branduri_pagina_1, "Pagina 1 nu este disponibila."
    time.sleep(2)

    # Test scroll pe verticala pagina 1 din sectiunea 'BRANDURI'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 6:
            break
        time.sleep(1.1)
    time.sleep(2)

    # Test accesare pagina 2 din sectiunea 'BRANDURI'
    branduri_pagina_2 = browser.find_element(By.CSS_SELECTOR, '#category-page > div.pagination.pg-categ.pull-right > ol > li:nth-child(2) > a')
    branduri_pagina_2.click()
    assert branduri_pagina_2, "Pagina 2 nu este disponibila."
    time.sleep(2)

    # Test scroll pe verticala pagina 2 din sectiunea 'BRANDURI'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 6:
            break
        time.sleep(1.1)
    time.sleep(2)

    # Test accesare pagina 3 din sectiunea 'BRANDURI'
    branduri_pagina_3 = browser.find_element(By.CSS_SELECTOR, '#category-page > div.pagination.pg-categ.pull-right > ol > li:nth-child(4) > a')
    branduri_pagina_3.click()
    assert branduri_pagina_3, "Pagina 3 nu este disponibila."
    time.sleep(2)

    # Test scroll pe verticala pagina 3 din sectiunea 'BRANDURI'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 6:
            break
        time.sleep(1.1)
    time.sleep(2)

    # Test accesare pagina 4 din sectiunea 'BRANDURI'
    branduri_pagina_4 = browser.find_element(By.CSS_SELECTOR, '#category-page > div.pagination.pg-categ.pull-right > ol > li:nth-child(5) > a')
    branduri_pagina_4.click()
    assert branduri_pagina_4, "Pagina 4 nu este disponibila."
    time.sleep(2)

    # Test scroll pe verticala pagina 4 din sectiunea 'BRANDURI'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 4:
            break
        time.sleep(1.1)
    time.sleep(2)

    browser.get("https://www.mosionroata.ro/lista-marci")
    time.sleep(3)