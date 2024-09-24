"""

    13. Test accesare sectiunea "RETUR/GARANTIE" si completare Formular de Garantie.
        Acest test va efectua accesarea si completarea formularului online cu privire la aplicarea conditiilor de garantie comerciala asupra unui produs nou, putin utilizat, care prezinta diverse neconcordante functionale si de forma.

"""




from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
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


# 13. Test completare 'Formular de Garantie'
def test_formular_de_garantie(browser:webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(2)

    # Test accesare sectiunea 'RETUR/GARANTIE'
    hover = ActionChains(browser)
    retur_garantie = browser.find_element(By.CSS_SELECTOR, "#main-menu > div > ul > li:nth-child(7) > a")
    time.sleep(2)
    hover.move_to_element(retur_garantie)
    ActionChains.perform(hover)
    assert retur_garantie, ("Sectiunea 'RETUR/GARANTIE' nu este vizibila.")
    time.sleep(2)

    # Test accesare 'Formular de Garantie'
    formular_garantie = browser.find_element(By.CSS_SELECTOR, '#main-menu > div > ul > li:nth-child(7) > div > ul > li:nth-child(2) > a')
    time.sleep(2)
    hover.move_to_element(formular_garantie)
    ActionChains.perform(hover)
    time.sleep(2)
    formular_garantie.click()
    assert formular_garantie, "Sectiunea 'Formular GARANTIE' nu este vizibila."
    time.sleep(2)

    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)

    # Test scroll pe verticala pagina 'Formular de Garantie'     
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 4:
            break
        time.sleep(1)
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,525)")
    time.sleep(2)

    # Test completare 'Formular de Garantie'
    nume_si_prenume = "........" # Se introduce numele si prenumele dorit
    caseta_nume_si_prenume = browser.find_element(By.NAME, 'name')
    for letter in nume_si_prenume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume_si_prenume.send_keys(letter)
    assert nume_si_prenume, "Caseta 'Nume si Prenume' nu este vizibila."
    time.sleep(2)

    telefon = "........" # Se introduce numarul de telefon dorit
    caseta_telefon = browser.find_element(By.NAME, "phone")
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    adresa_de_email = "........" # Se introduce adresa de email dorita
    caseta_adresa_de_email = browser.find_element(By.NAME, "email")
    for letter in adresa_de_email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_adresa_de_email.send_keys(letter)
    assert adresa_de_email, "Caseta 'Adresa de Email' nu este vizibila."
    time.sleep(2)

    # In functie de necesitate, va fi necesara updatarea informatiilor, conform coordonatelor din site, a reperelor dorite, prin modificarea codului
    judet_de_ridicare_colet = browser.find_element(By.CSS_SELECTOR, '#__pickupRegion > option:nth-child(11)').click()
    browser.find_element(By.NAME, 'pickup_region').click()
    judet_de_ridicare_colet = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[4]/div/select/option[11]')
    time.sleep(2)
    judet_de_ridicare_colet.click()
    click_judet_de_ridicare_colet = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[4]/label')
    click_judet_de_ridicare_colet.click()
    assert judet_de_ridicare_colet, "Caseta 'Judet de Ridicare Colet' nu este vizibila."
    assert judet_de_ridicare_colet, "Lista 'Judet de Ridicare Colet' nu este vizibila."
    time.sleep(2)

    oras_de_ridicare_colet = browser.find_element(By.CSS_SELECTOR, "#__pickupCity > option:nth-child(3)").click()
    browser.find_element(By.NAME, 'pickup_city').click()
    oras_de_ridicare_colet = browser.find_element(By.XPATH, "/html/body/div[2]/div[5]/div/div[1]/form/div[5]/div/select/option[3]")
    time.sleep(2)
    oras_de_ridicare_colet.click()
    click_oras_de_ridicare_colet = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[5]/label')
    click_oras_de_ridicare_colet.click()
    assert oras_de_ridicare_colet, "Caseta 'Oras de Ridicare Colet' nu este vizibila."
    assert oras_de_ridicare_colet, "Lista 'Oras de Ridicare Colet' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,300)")
    time.sleep(2)

    adresa_de_ridicare_colet = "........" # Se introduce Adresa dorita
    caseta_adresa_de_ridicare_colet = browser.find_element(By.NAME, "pickup_address")
    for letter in adresa_de_ridicare_colet:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_adresa_de_ridicare_colet.send_keys(letter)
    assert adresa_de_ridicare_colet, "Caseta 'Adresa de Ridicare Colet' nu este vizibila."
    time.sleep(2)

    numar_factura = "........" # Se introduce numarul de factura real sau fictiv
    caseta_numar_factura = browser.find_element(By.NAME, "invoice")
    for letter in numar_factura:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_numar_factura.send_keys(letter)
    assert numar_factura, "Caseta 'Numar Factura' nu este vizibila."
    time.sleep(2)

    data_factura = "........" # Se introduce data facturii, reala sau fictiva
    caseta_data_factura = browser.find_element(By.NAME, "invoice_date")
    for letter in data_factura:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_data_factura.send_keys(letter)
    assert data_factura, "Caseta 'Data Factura' mu este vizibila."
    time.sleep(2)

    denumire_produs = "........" # Se introduce orice produs care se regaseste in portofoliul site-ului 'https://www.mosionroata.ro/'
    caseta_denumire_produs = browser.find_element(By.NAME, "product")
    for letter in denumire_produs:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_denumire_produs.send_keys(letter)
        assert denumire_produs, "Caseta 'Denumire Produs' nu este vizibila."
    time.sleep(2)

    descrierea_problemei_intampinate = "........" # Se introduce omesajul dorit
    caseta_descrierea_problemei_intampinate = browser.find_element(By.NAME, "message")
    for letter in descrierea_problemei_intampinate:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_descrierea_problemei_intampinate.send_keys(letter)
    assert descrierea_problemei_intampinate, "Caseta 'Descrierea problemei intampinate' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,175)")
    time.sleep(2)

    # Test confirmare Acord GDPR 
    acord_GDPR = browser.find_element(By.NAME, "agreePersonalInformation")
    acord_GDPR.click()
    assert acord_GDPR, "Check-box-ul nu este vizibil."
    time.sleep(2)

    # Test apasare buton 'TRIMITE CERERE'
    trimite_cerere = browser.find_element(By.ID, "sendMessage")
    assert trimite_cerere, "Cererea ta a fost transmisa cu succes."
    time.sleep(3)