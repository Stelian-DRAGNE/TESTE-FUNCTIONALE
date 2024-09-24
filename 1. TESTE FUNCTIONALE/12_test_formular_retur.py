"""

    12. Test accesare sectiunea "RETUR/GARANTIE" si completare Formular de Retur.
        Acest test va efectua accesarea si completarea formularului online cu privire la returnarea unui produs nou comandat online, produs care la primire, prezinta urme de uzura.

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


# 12. Test completare 'Formular de Retur'
def test_formular_de_retur(browser: webdriver.Chrome):
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

    # Test accesare 'Formular de Retur'
    formular_retur_rma = browser.find_element(By.CSS_SELECTOR, '#main-menu > div > ul > li:nth-child(7) > div > ul > li:nth-child(1) > a')
    time.sleep(2)
    hover.move_to_element(formular_retur_rma)
    ActionChains.perform(hover)
    time.sleep(2)
    formular_retur_rma.click()
    assert formular_retur_rma, "Sectiunea 'Formular RETUR (RMA)' nu este vizibila."
    time.sleep(2)

    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)

    # Test scroll pe verticala pagina 'Formular de Retur'
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 5:
            break
        time.sleep(1.1)
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,500)")
    time.sleep(2)

    # Test completare 'Formular de Retur'
    nume_si_prenume = "........" # Se introduce numele si prenumele dorit
    caseta_nume_si_prenume = browser.find_element(By.NAME, "name")
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
    assert adresa_de_email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    numar_factura = "........" # Se introduce numarul de factura real sau fictiv
    caseta_numar_factura = browser.find_element(By.NAME, "invoice")
    for letter in numar_factura:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_numar_factura.send_keys(letter)
    assert numar_factura, "Caseta 'Numar Factura' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,200)")
    time.sleep(2)

    # In functie de necesitate, va fi necesara updatarea informatiilor, conform coordonatelor din site, a reperelor dorite, prin modificarea codului
    data_factura_an =  browser.find_element(By.CSS_SELECTOR, "#__orderYear > option:nth-child(2)").click()
    browser.find_element(By.NAME, 'order_year').click()
    data_factura_an = browser.find_element(By.XPATH, '//*[@id="__orderYear"]/option[2]')
    data_factura_an.click()
    time.sleep(2)
    click_data_factura_an = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/label')
    click_data_factura_an.click()
    assert data_factura_an, "Caseta 'Data Factura - An' nu este vizibila"
    assert data_factura_an, "Lista 'Data Factura - An' nu este vizibila"
    time.sleep(2)

    data_factura_luna = browser.find_element(By.CSS_SELECTOR, "#__orderMonth > option:nth-child(3)").click()
    browser.find_element(By.NAME, 'order_month').click()
    data_factura_luna = browser.find_element(By.XPATH, '//*[@id="__orderMonth"]/option[3]')
    data_factura_luna.click()
    time.sleep(2)
    click_data_factura_luna = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/label')
    click_data_factura_luna.click()
    assert data_factura_luna, "Caseta 'Data Factura - Luna' nu este vizibila"
    assert data_factura_luna, "Lista 'Data Factura - Luna' nu este vizibila"
    time.sleep(2)

    data_factura_zi = browser.find_element(By.CSS_SELECTOR, "#__orderDay > option:nth-child(22)").click()
    browser.find_element(By.NAME, 'order_day').click()
    data_factura_zi = browser.find_element(By.XPATH, '//*[@id="__orderDay"]/option[22]')
    data_factura_zi.click()
    time.sleep(2)
    click_data_factura_zi = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/label')
    click_data_factura_zi.click()
    assert data_factura_zi, "Caseta 'Data Factura - Zi' nu este vizibila"
    assert data_factura_zi, "Lista 'Data Factura - Zi' nu este vizibila"
    time.sleep(2)

    mod_plasare_comanda_online = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/div/input[1]')
    mod_plasare_comanda_online.click()
    assert mod_plasare_comanda_online, "Butonul 'Online' nu este vizibil."
    time.sleep(2)

    mod_plasare_comanda_telefonic = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/div/input[2]')
    mod_plasare_comanda_telefonic.click()
    assert mod_plasare_comanda_telefonic, "Butonul 'telefonic' nu este vizibil."
    time.sleep(2)

    mod_plasare_comanda_online = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/div/input[1]')
    mod_plasare_comanda_online.click()
    assert mod_plasare_comanda_online, "Butonul 'Online' nu este vizibil."
    time.sleep(2)

    cont_bancar_pentru_returnare_contravaloare_comanda = "........" # Se introduce numarul de cont dorit
    caseta_cont_bancar_pentru_returnare_contravaloare_comanda = browser.find_element(By.NAME, "bank_account")
    for letter in cont_bancar_pentru_returnare_contravaloare_comanda:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cont_bancar_pentru_returnare_contravaloare_comanda.send_keys(letter)
    assert cont_bancar_pentru_returnare_contravaloare_comanda, "Caseta 'Cont bancar pentru returnare contravaloare comanda' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    produs_returnat = "........" # Se introduce orice produs care se regaseste in portofoliul site-ului 'https://www.mosionroata.ro/'
    caseta_produs_returnat = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[8]/div/input')
    for letter in produs_returnat:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_produs_returnat.send_keys(letter)
    assert produs_returnat, "Caseta 'Produs returnat' nu este vizibila"
    time.sleep(2)

    motivul_returnarii_produsului = "........" # Se introduce mesajul dorit
    caseta_produs_returnat = browser.find_element(By.NAME, "reason")
    for letter in motivul_returnarii_produsului:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_produs_returnat.send_keys(letter)
    assert motivul_returnarii_produsului, "Caseta 'Motivul returnarii produsului' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)")
    time.sleep(2)

    observatii_alte_comentarii = "........" # Se introduce mesajul dorit
    caseta_observatii_alte_comentarii = browser.find_element(By.NAME, "message")
    for letter in observatii_alte_comentarii:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_observatii_alte_comentarii.send_keys(letter)
    assert observatii_alte_comentarii, "Caseta 'Observatii/Alte comentarii' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    # Test confirmare Acord GDPR 
    acord_GDPR = browser.find_element(By.NAME, "agreePersonalInformation")
    acord_GDPR.click()
    time.sleep(2)
    assert acord_GDPR, "Check-box-ul nu este vizibil."
    time.sleep(2)

    # Test apasare buton 'TRIMITE CERERE'
    trimite_cerere = browser.find_element(By.ID, "sendMessage")
    assert trimite_cerere, "Cererea ta a fost transmisa cu succes."
    time.sleep(3)