"""

    4.  Test accesare sectiunea 'DESPRE NOI'.
        Acest test va accesa sectiunea "DESPRE NOI", prezenta in cadrul site-ului ales pentru testare si completarea formularului online disponibil.

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


# 4. Test accesare sectiunea 'DESPRE NOI'
def test_despre_noi(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(2)

    # Test cautare pe pagina principala a sectiunii 'DESPRE NOI'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 18:
            break
        time.sleep(1.1)
    time.sleep(1)

    # Test accesare sectiune 'DESPRE NOI'
    despre_noi = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[21]/p/span[2]/a/span/strong')
    time.sleep(2)
    despre_noi.click()
    assert despre_noi, "Linkul 'AICI' nu este vizibil."
    time.sleep(3)

    # Test scroll pe verticala pagina 'DESPRE NOI'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 11:
            break
        time.sleep(1.1)
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,2200)")
    time.sleep(2)

    # Test completare formular 'Ai o întrebare pentru noi? Nu ezita să ne contactezi!'
    nume = "........" # Se introduce numele dorit
    caseta_nume = browser.find_element(By.NAME, "field[1]")
    for letter in nume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume.send_keys(letter)
    assert nume, "Caseta 'Nume' nu este vizibila."
    time.sleep(2)

    prenume = "........" # Se introduce prenumele dorit
    caseta_prenume = browser.find_element(By.NAME, "field[2]")
    for letter in prenume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_prenume.send_keys(letter)
    assert prenume, "Caseta 'Prenume' nu este vizibila."
    time.sleep(2)

    email = "........" # Se introduce adresa de email dorita
    caseta_email = browser.find_element(By.NAME, "field[0]")
    for letter in email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_email.send_keys(letter)
    assert email, "Caseta 'Email' nu este vizibila."
    assert email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    telefon = "........" # Se introduce numarul de telefon dorin dorit
    caseta_telefon = browser.find_element(By.NAME, "field[3]")
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)")
    time.sleep(2)

    mesaj = "........" # Se introduce mesajul dorit
    caseta_mesaj = browser.find_element(By.NAME, "field[4]")
    for letter in mesaj:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_mesaj.send_keys(letter)
    assert mesaj, "Caseta 'Mesaj' nu este vizibila."
    time.sleep(2)

    # Test accept Acord GDPR
    acord_GDPR = browser.find_element(By.XPATH, '//*[@id="__submit7"]/div/label/div/input')
    acord_GDPR.click()
    assert acord_GDPR, "Check-box-ul nu este vizibil."
    time.sleep(2)

    # Test apasare buton TRIMITE
    trimite = browser.find_element(By.ID, "__doSubmit7")
    assert trimite, "Mesajul a fost transmis cu succes !"
    time.sleep(3)