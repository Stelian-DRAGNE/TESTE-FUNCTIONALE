"""

    6.  Test functionare caseta 'Cauta in site ...' din pagina principala.
        Acest test va verifica functionalitatea casetei 'Cauta in site ...' din pagina principala a site-ului ales pentru testare.

"""




from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
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


# 6. Test functionare caseta 'Cauta in site ...' din pagina principala
def test_caseta_search(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(3)

    # Test cautare produs in caseta 'Cauta in site ...' din pagina principala
    search_produs = "........" # Se introduce produsul dorit, care se regaseste pe site-ul 'https://www.mosionroata.ro/'
    caseta_cautare = browser.find_element(By.NAME, "c")
    for letter in search_produs:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cautare.send_keys(letter)
    assert search_produs, "Caseta 'Cauta in site ...' nu este vizibila."
    assert search_produs, "Produsul cautat nu mai este disponibil."
    time.sleep(2)

    # Test accesare produs cautat si gasit
    produs = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/div/div/div[2]/form/div/div/div/div[2]/div/a[1]')))
    time.sleep(2)
    produs.click()
    assert produs, "Produsul cautat nu mai este disponibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,200)")
    time.sleep(3)