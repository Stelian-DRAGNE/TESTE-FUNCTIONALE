"""

    15. Test abonare la 'Newsletter'.
        Acest test va efectua abonarea la 'Newsletter', sectiune prezenta in cadrul site-ului ales pentru testare.

"""


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


# 15. Test abonare la 'Newsletter'
def test_abonare_newsletter(browser: webdriver.Chrome):
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
        if stopScrolling > 25:
            break
        time.sleep(1.1)

    browser.execute_script("window.scrollTo(4750,4750)")
    time.sleep(3)
    
    # Test completare sectiune 'Newsletter'
    email = "........" # Se introduce adresa de email dorita
    caseta_email = browser.find_element(By.ID, '_emailAddress')
    for letter in email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_email.send_keys(letter)
    assert email, "Caseta 'Adresa de email' nu este vizibila."
    assert email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    # Test abonare la 'Newsletter'
    accept_primire_newsletter = browser.find_element(By.CLASS_NAME, "styleApplied")
    accept_primire_newsletter.click()
    assert accept_primire_newsletter, "Check-box-ul nu este vizibil."
    time.sleep(2)

    # Test apasare buton 'ABONEAZA-TE'
    abonare_newsletter = browser.find_element(By.ID, "_subscribe")
    assert abonare_newsletter, "Te-ai abonat cu succes la Newsletter."
    time.sleep(3)