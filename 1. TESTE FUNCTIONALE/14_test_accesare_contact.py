"""

    14. Test accesare sectiunea "CONTACT".
        Acest test va efectua accesarea sectiunii "CONTACT", sectiune prezenta in cadrul site-ului ales pentru testare si completarea formuralui on-line disponibil.

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


# 14. Test accesare sectiunea 'CONTACT '  
def test_accesare_contact(browser:webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(3)

    # Test accesare sectiunea 'CONTACT'
    contact = browser.find_element(By.XPATH, '//*[@id="main-menu"]/div/ul/li[8]/a')
    contact.click()
    assert contact, "Sectiunea 'CONTACT' nu este disponibila."
    time.sleep(1)

    # Test scroll pe verticala pagina sectiunii 'CONTACT'
    time.sleep(2)
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 3:
            break
        time.sleep(1.1)
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,450)")
    time.sleep(3)

    # Test completare formular 'Contacteaza-ne'
    email = "........" # Se introduce adresa de email dorita
    caseta_email = browser.find_element(By.XPATH, '//*[@id="email"]')
    for letter in email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_email.send_keys(letter)
    assert email, "Caseta 'Email' nu este vizibila."
    assert email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    nume = "........" # Se introduce nume si / sau prenume dorit
    caseta_nume = browser.find_element(By.NAME, 'lastname')
    for letter in nume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume.send_keys(letter)
    assert nume, "Caseta 'Nume' nu este vizibila."
    time.sleep(2)

    telefon = "........" # Se introduce numarul de telefon dorit
    caseta_telefon = browser.find_element(By.NAME, "phone")
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,125)")
    time.sleep(1)

    mesaj = "........" # Se introduce mesajul dorit
    caseta_mesaj = browser.find_element(By.NAME, "message")
    for letter in mesaj:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_mesaj.send_keys(letter)
    assert mesaj, "Caseta 'Mesajul tau' nu este vizibila."
    time.sleep(2)

    # Test confirmare Acord GDPR
    acord_GDPR = browser.find_element(By.NAME, "agreePersonalInformation")
    acord_GDPR.click()
    assert acord_GDPR, "Check-box-ul nu este vizibil."

    # Test apasare buton 'TRIMITE MESAJ'
    trimite_mesaj = browser.find_element(By.ID, "sendMessage")
    assert trimite_mesaj, "Mesajul tau a fost trimis cu succes !"
    time.sleep(3)