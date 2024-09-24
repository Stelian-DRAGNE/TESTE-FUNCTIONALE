"""

    8.  Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principala si test cautare produs 2, urmate de finalizare comanda.
        Acest test va efectua cautarea unui produs in cadrul site-ului ales pentru testare, se va accesa produsul respectiv, se configureaza, se adauga in cos.
        In continuare se va efectua cautarea unui alt produs in cadrul site-ului ales pentru testare, se va accesa produsul respectiv, se configureaza, se adauga in cos si se finalizeaza comanda pentru cele doua categorii de produse alese.

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


# 8. Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principala si test cautare produs 2, urmate de finalizare comanda
def test_produs_1_si_produs_2(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(2) 

    # Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principala
    search_produs = "........" # Se introduce orice produs care se regaseste in portofoliul site-ului 'https://www.mosionroata.ro/'
    caseta_cautare = browser.find_element(By.NAME, "c")
    for letter in search_produs:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cautare.send_keys(letter)
    assert search_produs, "Caseta 'Cauta in site ...' nu este vizibila."
    assert search_produs, "Produsul cautat nu mai este disponibil."
    time.sleep(2)

    # Test selectare produs cautat 1
    produs_1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/div/div/div[2]/form/div/div/div/div[2]/div/a[1]')))
    time.sleep(3)
    produs_1.click()
    assert produs_1, "Produsul cautat nu mai este disponibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,200)")

    # Test alegere dimensiune pentru produs 1
    dimensiune_produs = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-page"]/div[1]/div[1]/div[3]/div[3]/div/div[4]/a')))
    time.sleep(3)
    dimensiune_produs.click()
    assert dimensiune_produs, "STOC EPUIZAT"
    time.sleep(2)

    # Test alegere dimensiune dorita pentru produs 1
    dimensiune_produs_1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-page"]/div[1]/div[1]/div[3]/div[3]/div/div[3]/a')))
    time.sleep(3)
    dimensiune_produs_1.click()
    assert dimensiune_produs_1, "STOC EPUIZAT"
    time.sleep(2)

    # Test adaugare produs 1 in cosul de cumparaturi
    adaugare_produs_1_in_cos = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-page"]/div[1]/div[1]/div[3]/div[4]/a')))
    time.sleep(2)
    adaugare_produs_1_in_cos.click()
    assert adaugare_produs_1_in_cos, "Butonul 'ADAUGA IN COS' nu este vizibil."
    time.sleep(5)

    browser.execute_script("window.scrollTo(0,0)")

    # Test accesare cos de cumparaturi
    panou_lateral_cos = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div/div/div[3]/ul/li[5]/a")
    time.sleep(5)
    panou_lateral_cos.click()
    assert panou_lateral_cos, "Fereastra 'Cos de cumparaturi' nu este vizibila."
    time.sleep(3)

    # Test inchidere cos de cumparaturi
    close_panou_lateral = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/i")
    close_panou_lateral.click()
    time.sleep(3)

    # Test cautare produs dorit 2 in caseta 'Cauta in site ...'
    search_produs_2 = "........" # Se introduce orice produs care se regaseste in portofoliul site-ului 'https://www.mosionroata.ro/'
    caseta_cautare = browser.find_element(By.NAME, "c")
    for letter in search_produs_2:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cautare.send_keys(letter)
    assert search_produs_2, "Caseta 'Cauta in site ...' nu este vizibila."
    assert search_produs_2, "Produsul cautat nu mai este disponibil."
    time.sleep(2)

    # Test selectare produs dorit 2 in caseta 'Cauta in site ...'
    produs_2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_searchFormMainHeader"]/div/div/div/div[2]/div/a[1]/img')))
    time.sleep(3)
    produs_2.click()
    assert produs_2, "Produsul cautat nu mai este disponibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,200)")
    time.sleep(2)

    # Test alegere dimensiune pentru produs 2
    dimensiune_produs = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-page"]/div[1]/div[1]/div[3]/div[2]/div/div[5]/a')))
    dimensiune_produs.click()
    assert dimensiune_produs, "STOC EPUIZAT"
    time.sleep(5)

    # Test alegere dimensiune dorita pentru produs 2
    dimensiune_produs_2 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-page"]/div[1]/div[1]/div[3]/div[2]/div/div[4]/a')))
    dimensiune_produs_2.click()
    assert dimensiune_produs_2, "STOC EPUIZAT"
    time.sleep(5)

    # Test marire cantitate produs 2
    marire_cantitate_produs_2 = browser.find_element(By.XPATH, '//*[@id="qtyplus"]/i')
    time.sleep(2)
    marire_cantitate_produs_2.click()
    assert marire_cantitate_produs_2, "Cantitatea solicitata nu este disponibila."
    time.sleep(2)

    # Test adaugare produs 2 in cosul de cumparaturi
    adaugare_produs_2_in_cos = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-page"]/div[1]/div[1]/div[3]/div[3]/a')))
    adaugare_produs_2_in_cos.click()
    assert adaugare_produs_2_in_cos, "Butonul 'ADAUGA IN COS' nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(2)

    # Test accesare cos de cumparaturi
    cos_de_cumparaturi_2 = browser.find_element(By.XPATH, '//*[@id="wrapper"]/header/div[2]/div/div/div[3]/ul/li[5]/a/span[2]')
    time.sleep(5)
    cos_de_cumparaturi_2.click()
    assert cos_de_cumparaturi_2, "Cosul de cumparaturi nu este vizibil."
    time.sleep(3)

    # Test finalizare comanda
    finalizare_comanda_panoul_lateral = browser.find_element(By.XPATH, '//*[@id="-g-cart-dropdown"]/div[3]/button')
    time.sleep(3)
    finalizare_comanda_panoul_lateral.click()
    assert finalizare_comanda_panoul_lateral, "Butonul 'FINALIZEAZA COMANDA' nu este disponibil."
    time.sleep(3)

    # Test completare formular 'Finalizare comanda' cu logare pe cont utilizator/client creat in prealabil
    # Test accesare formular 'Finalizare comanda'
    completare_formular_comanda = browser.find_element(By.ID, "login-buy-button")
    completare_formular_comanda.click()
    assert completare_formular_comanda, "Formularul nu este vizibil."
    time.sleep(2)

    # Test logare pe cont utilizator/client creat in prealabil in formularul de 'Finalizare comanda'
    user_email = "........" # Se introduce adresa de email cu care s-a creat in prealabil contul de utilizator/client
    email = browser.find_element(By.ID, '_loginEmail')
    for letter in user_email:
        time.sleep(random.uniform(0.05, 0.05))
        email.send_keys(letter)
    assert user_email, "Caseta 'Email' nu este vizibila."
    assert user_email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    user_password = "........" # Se introduce parola cu care s-a creat in prealabil contul de utilizator/client
    password = browser.find_element(By.ID, '_loginPassword')
    for letter in user_password:
        time.sleep(random.uniform(0.05, 0.05))
        password.send_keys(letter)
    assert user_password, "Caseta 'Parola' nu este vizibila."
    assert user_password, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    # Test apasare buton 'INTRA IN CONT' din formularul 'Finalizare comanda'
    login_button = browser.find_element(By.ID, '_doLogin')
    login_button.click()
    assert login_button, "Butonul 'INTRA IN CONT' nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,200)")
    time.sleep(2)
    browser.execute_script("window.scrollBy(200,350)")
    time.sleep(2)

    # Test completare sectiune 'LIVRARE' - alegere Metoda de livrare 'Livrare Curier'
    metoda_de_livrare_curier = browser.find_element(By.XPATH, '//*[@id="checkoutform"]/div[19]/div/label[1]/input')
    metoda_de_livrare_curier.click()
    assert metoda_de_livrare_curier, "Check-box-ul 'Livrare Curier' nu este vizibil."
    assert metoda_de_livrare_curier, "Metoda de livrare 'Livrare Curier' nu este disponibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,425)")

    # Test completare sectiune 'PLATA' - alegere metoda de plata 'RAMBURS / CARD LA EASYBOX'
    metoda_de_plata_ramburs = browser.find_element(By.XPATH, '//*[@id="_paymentOptions"]/span[1]/label/input')
    metoda_de_plata_ramburs.click()
    assert metoda_de_plata_ramburs, "Check-box-ul 'RAMBURS / CARD LA EASYBOX' nu este vizibil."
    assert metoda_de_plata_ramburs, "Metoda de plata 'RAMBURS / CARD LA EASYBOX' nu este disponibila."
    time.sleep(2)

    # Test completare sectiune 'OBSERVATII' - mesaj catre vanzator prin intermediul formularului de comanda online
    mesaj = "........" # Se introduce mesajul dorit
    caseta_mesaj = browser.find_element(By.NAME, "public_comments")
    for letter in mesaj:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_mesaj.send_keys(letter)
    assert mesaj, "Caseta 'Mesajul tau' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,430)")
    time.sleep(2)

    # Test confirmare Acord GDPR 
    acord_GDPR = browser.find_element(By.NAME, "agreePersonalInformation")
    acord_GDPR.click()
    assert acord_GDPR, "Check-box-ul nu este vizibil."
    time.sleep(2)

    # Test abonare la Newsletter
    abonare_newsletter = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "agreeNewsletterInformation")))
    abonare_newsletter.click()
    assert abonare_newsletter, "Check-box-ul nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,50)")

    # Test apasare buton 'TRIMITE COMANDA'
    trimite_comanda = browser.find_element(By.ID, "doCheckout")
    assert trimite_comanda, "Comanda a fost trimisa cu succes !"
    time.sleep(3)