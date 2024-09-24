""" 

    Proiectul are in compunere 15 teste automate.

    Testele vor fi aplicate sectiunilor afisate in cadrul site-ului ales pentru testare.

    Aceste teste sunt:

        1.  Test verificare status pagina principala.
            Acest test va verifica daca pagina principala a site-ului ales pentru testare este activa si nu returneaza un cod de eroare, cel pregonizat fiind 200.

        2.  Test acceptare cookie-uri pagina principala.
            Acest test accepta politica de Cookie a site-ului ales pentru testare.

        3.  Test scroll pe verticala pagina principala.
            Acest test va face Scroll pe verticala a paginii principale a site-ului ales pentru testare.

        4.  Test accesare sectiunea 'DESPRE NOI'.
            Acest test va accesa sectiunea "DESPRE NOI", prezenta in cadrul site-ului ales pentru testare si completarea formularului online disponibil.

        5.  Test "Intra pe cont" pe site, in cont de utilizator/client creat in prealabil, verificare sectiuni disponibile, si apoi 'Logout'.
            In prealabil s-a creat un cont de utilizator/client, necesar ulterior in cadrul urmatoarelor teste.   Acest test va efectua logarea pe contul de utilizator/client, deja creat.

        6.  Test functionare caseta 'Cauta in site ...' din pagina principala.
            Acest test va verifica functionalitatea casetei 'Cauta in site ...' din pagina principala a site-ului ales pentru testare.

        7.  Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principala si finalizare comanda.
            Acest test va efectua cautarea unui produs in cadrul site-ului ales pentru testare, se va accesa produsul respectiv, se configureaza, se adauga in cos si se finalizeaza comanda.

        8.  Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principala si test cautare produs 2, urmate de finalizare comanda.
            Acest test va efectua cautarea unui produs in cadrul site-ului ales pentru testare, se va accesa produsul respectiv, se configureaza, se adauga in cos.
            In continuare se va efectua cautarea unui alt produs in cadrul site-ului ales pentru testare, se va accesa produsul respectiv, se configureaza, se adauga in cos si se finalizeaza comanda pentru cele doua categorii de produse alese.

        9.  Test sortare 'Biciclete Mountainbike' din sectiunea 'TOATE PRODUSELE'.
            Acest test va efectua sortarea produselor 'Biciclete Mountainbike' din sectiunea "TOATE PRODUSELE", in urma aplicarii filtrelor dorite, disponibile pe pagina 'Biciclete Mountainbike'.

        10. Test accesare sectiunea 'BLOG'.
            Acest test va efectua accesarea sectiunii "BLOG", sectiune prezenta in cadrul site-ului ales pentru testare.

        11. Test accesare sectiunea "BRANDURI".
            Acest test va prezenta lista brand-urilor comercializate de catre site-ul ales pentru testare, in ordinea numarului de pagini disponibile in aceasta sectiune a site-ului.

        12. Test accesare sectiunea "RETUR/GARANTIE" si completare Formular de Retur.
            Acest test va efectua accesarea si completarea formularului online cu privire la returnarea unui produs nou comandat online, produs care la primire, prezinta urme de uzura.

        13. Test accesare sectiunea "RETUR/GARANTIE" si completare Formular de Garantie.
            Acest test va efectua accesarea si completarea formularului online cu privire la aplicarea conditiilor de garantie comerciala asupra unui produs nou, putin utilizat, care prezinta diverse neconcordante functionale si de forma.

        14. Test accesare sectiunea "CONTACT".
            Acest test va efectua accesarea sectiunii "CONTACT", sectiune prezenta in cadrul site-ului ales pentru testare si completarea foformularului on-line disponibil.

        15. Test abonare la 'Newsletter'.
            Acest test va efectua abonarea la 'Newsletter', sectiune prezenta in cadrul site-ului ales pentru testare.

    In cadrul unora dintre teste s-a optat pentru similaritate cu celelalte, pentru a se evidentia ceea ce se doreste a se prezenta prin intermediul respectivului test, intr-o maniera cursiva si logica.

    Fiecare dintre teste are in compunere si assert-uri pentru diferite componente ale site-ului respectiv, presupus a fi aplicate.

    Timpul estimat de rulare a celor 15 teste : aproximativ 21 minute si 20 secunde.

"""




from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
import requests
import random
import pytest
import time




# Accesare browser Chrome
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options = chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


# 1. Test verificare status pagina principala
def test_status_pagina():
    response = requests.get("https://www.mosionroata.ro/")
    assert response.status_code == 200, f"Cod status este {response.status_code}, dar se astepta raspuns 200."
    assert len(response.text) > 0, "Continutul raspunsului este gol."


# 2. Test acceptare cookie-uri pagina principala
def test_acceptare_cookie(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(3)


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
    nume = "DRAGNE"
    caseta_nume = browser.find_element(By.NAME, "field[1]")
    for letter in nume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume.send_keys(letter)
    assert nume, "Caseta 'Nume' nu este vizibila."
    time.sleep(2)

    prenume = "Stelian"
    caseta_prenume = browser.find_element(By.NAME, "field[2]")
    for letter in prenume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_prenume.send_keys(letter)
    assert prenume, "Caseta 'Prenume' nu este vizibila."
    time.sleep(2)

    email = "stelian.dragne@yahoo.com"
    caseta_email = browser.find_element(By.NAME, "field[0]")
    for letter in email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_email.send_keys(letter)
    assert email, "Caseta 'Email' nu este vizibila."
    assert email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    telefon = "0733150829"
    caseta_telefon = browser.find_element(By.NAME, "field[3]")
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)")
    time.sleep(2)

    mesaj = "Va rog sa ma contactati in legatura cu procedura de plasare comanda on-line."
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


# 5. Test "Intra pe cont" pe site, in cont de utilizator/client creat in prealabil, verificare sectiuni disponibile, si apoi 'Logout'
def test_login(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(2)

    # Test accesare sectiunea 'Intra pe cont'
    accesare_login = browser.find_element(By.XPATH, '//*[@id="wrapper"]/header/div[2]/div/div/div[3]/ul/li[2]/a/i')
    accesare_login.click()
    assert accesare_login, "Butonul 'Intra in cont' nu este vizibil."
    assert accesare_login, "Pagina 'Client nou: Inregistrare / Contul tau' nu este disponibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)") 
    time.sleep(2)
    browser.execute_script("window.scrollBy(100,-100)") 
    time.sleep(2)

    # Test completare formular 'Client nou: Inregistrare'
    inregistreaza_te = browser.find_element(By.ID, "doRegister")
    inregistreaza_te.click()
    assert inregistreaza_te, "Sectiunea 'Client nou: Inregistrare' nu este vizibila."
    assert inregistreaza_te, "Butonul 'INREGISTREAZA-TE' nu este vizibil."
    time.sleep(2)

    email_inregistrare_cont = "stelian.dragne@yahoo.com"
    email = browser.find_element(By.ID, "__emailRegister")
    for letter in email_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        email.send_keys(letter)
    assert email_inregistrare_cont, "Caseta 'Email' nu este vizibila."
    assert email_inregistrare_cont, "Email-ul introdus nu este corect."
    time.sleep(2)

    nume_inregistrare_cont = "DRAGNE"
    nume = browser.find_element(By.ID, "__lastnameRegister")
    for letter in nume_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        nume.send_keys(letter)
    assert nume_inregistrare_cont, "Caseta 'Nume' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)") 
    time.sleep(2)

    prenume_inregistrare_cont = "Stelian"
    prenume = browser.find_element(By.ID, "__firstnameRegister")
    for letter in prenume_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        prenume.send_keys(letter)
    assert email_inregistrare_cont, "Caseta 'Prenume' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,75)") 
    time.sleep(2)

    parola_inregistrare_cont = "Sergiu2019@"
    parola = browser.find_element(By.ID, "__passwordRegister")
    for letter in parola_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        parola.send_keys(letter)
    assert parola_inregistrare_cont, "Caseta 'Parola' nu este vizibila."
    assert parola_inregistrare_cont, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)") 
    time.sleep(2)

    confirmare_parola_inregistrare_cont = "Sergiu2019@"
    confirmare_parola = browser.find_element(By.ID, "__confirmPasswordRegister")
    for letter in confirmare_parola_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        confirmare_parola.send_keys(letter)
    assert confirmare_parola_inregistrare_cont, "Caseta 'Confirma parola' nu este vizibila."
    assert confirmare_parola_inregistrare_cont, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    # Test abonare la Newsletter
    abonare_newsletter = browser.find_element(By.NAME, 'agreeNewsletterInformation')
    abonare_newsletter.click()
    assert abonare_newsletter, "Check-box-ul nu este vizibil."
    time.sleep(2)

    # Test confirmare Acord GDPR
    acord_GDPR = browser.find_element(By.NAME, 'agreePersonalInformation')
    acord_GDPR.click()
    assert acord_GDPR, "Check-box-ul nu este vizibil."
    time.sleep(2)

    # Test apasare buton INREGISTREAZA-TE
    buton_inregistreaza_te = browser.find_element(By.ID, 'doRegister')
    assert buton_inregistreaza_te, "Butonul 'INREGISTREAZA-TE' nu este vixibil."
    assert buton_inregistreaza_te, "Inregistrarea a fost efectuata cu succes !"

    browser.execute_script("window.scrollTo(0,0)") 
    time.sleep(2)

    # Test Login pe site, in cont de utilizator/client creat in prealabil
    accesare_login = browser.find_element(By.XPATH, '//*[@id="wrapper"]/header/div[2]/div/div/div[3]/ul/li[2]/a/i')
    accesare_login.click()
    assert accesare_login, "Pagina 'Inregistrare / Login' nu este disponibila."
    time.sleep(2)

    user_email = 'stelian.dragne@yahoo.com'
    email = browser.find_element(By.ID, '_loginEmail')
    for letter in user_email:
        time.sleep(random.uniform(0.05, 0.05))
        email.send_keys(letter)
    assert user_email, "Caseta 'Email' nu este vizibila."
    assert user_email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    user_password = "Sergiu2019@"
    password = browser.find_element(By.ID, '_loginPassword')
    for letter in user_password:
        time.sleep(random.uniform(0.05, 0.05))
        password.send_keys(letter)
    assert user_password, "Caseta 'Confirma parola' nu este vizibila."
    assert user_password, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    # Test apasare buton 'INTRA IN CONT'
    login_button = browser.find_element(By.ID, 'doLogin')
    login_button.click()
    assert login_button, "Butonul 'INTRA IN CONT' nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)") 
    time.sleep(2)
    browser.execute_script("window.scrollBy(0,0)") 
    time.sleep(2)

    # Test accesare sectiune 'Istoric Comenzi'
    istoric_comenzi = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[2]/li[3]/a')
    istoric_comenzi.click()
    assert istoric_comenzi, "Sectiunea 'Istoric Comenzi' nu este disponibila."
    time.sleep(2)

    # Test utilizare caseta 'Cauta dupa numar de comanda sau denumire produs'
    numar_comanda = "2024"
    caseta_istoric_comenzi = browser.find_element(By.XPATH, '//*[@id="keyword"]')
    for letter in numar_comanda:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_istoric_comenzi.send_keys(letter)
    assert numar_comanda, "Caseta 'Cauta dupa numar de comanda sau denumire produs' nu este disponibila."
    assert numar_comanda, "Ne pare rau, nu am gasit comenzi care sa se potriveasca cu cautarea ta."
    time.sleep(2)

    # Test cautare dupa numar comanda, in sectiunea 'Istoric Comenzi'
    cautare_numar_comanda = browser.find_element(By.XPATH, '//*[@id="__keywordSearch"]/i')
    cautare_numar_comanda.click()
    assert cautare_numar_comanda, "Butonul de cautare nu este vizibil."
    time.sleep(2)

    # Test inchidere filtru 'Cautare:"2024"'
    inchidere_filtru = browser.find_element(By.XPATH, '//*[@id="__quickListForm"]/div[2]/span/a')
    inchidere_filtru.click()
    assert inchidere_filtru, """Butonul de inchidere filtru 'Cautare:"2024"' nu este vizibil."""
    time.sleep(2)

    # Test accesare sectiune 'Status comanda'
    status_comanda = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[2]/li[4]/a')
    status_comanda.click()
    assert status_comanda, "Sectiunea 'Status comanda' nu este disponibila."
    time.sleep(2)

    # Test cautare dupa numar comanda, in sectiunea 'Status comanda' 
    status_numar_comanda = "2024"
    caseta_status_numar_comanda = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[4]/input')
    for letter in status_numar_comanda:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_status_numar_comanda.send_keys(letter)
    assert status_numar_comanda, "Caseta 'Numar Comanda' nu este vizibila."
    time.sleep(2)

    # Test apasare buton 'VEZI STATUS'
    buton_vezi_status = browser.find_element(By.XPATH, '//*[@id="doSave"]')
    buton_vezi_status.click()
    assert buton_vezi_status, "Butonul 'VEZI STATUS' nu este vizibil."
    assert buton_vezi_status, "Comanda nu a fost gasita."
    time.sleep(2)

    # Test accesare sectiune 'Status comanda'
    status_comanda = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[2]/li[4]/a')
    status_comanda.click()
    assert status_comanda, "Sectiunea 'Status comanda' nu este disponibila."
    time.sleep(2)

    # Test accesare sectiunea 'Produse Favorite - Wishlist'
    wishlist = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[2]/li[5]/a')
    wishlist.click()
    assert wishlist, "Sectiunea 'Produse Favorite - Wishlist' nu este vizibila."
    time.sleep(2)

    # Test accesare sectiunea 'Puncte de fidelitate'
    puncte_de_fidelitate = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[2]/li[6]/a')
    puncte_de_fidelitate.click()
    assert puncte_de_fidelitate, "Sectiunea 'Puncte de fidelitate' nu este vizibila."
    time.sleep(2)

    # Test scroll pe verticala a sectiunii 'Puncte de fidelitate'
    browser.execute_script("window.scrollBy(0,100)") 
    time.sleep(2)
    browser.execute_script("window.scrollBy(100,-100)") 
    time.sleep(2)

    # Test accesare sectiune 'Formular de Retur'
    formular_de_retur = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[2]/li[7]/a')
    formular_de_retur.click()
    assert formular_de_retur, "Seciunea 'Formular de Retur' nu este vizibila."
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
    nume_si_prenume = "DRAGNE Stelian"
    caseta_nume_si_prenume = browser.find_element(By.NAME, "name")
    for letter in nume_si_prenume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume_si_prenume.send_keys(letter)
    assert nume_si_prenume, "Caseta 'Nume si Prenume' nu este vizibila."
    time.sleep(2)

    telefon = "0733150829"
    caseta_telefon = browser.find_element(By.NAME, "phone")
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    adresa_de_email = "stelian.dragne@yahoo.com"
    caseta_adresa_de_email = browser.find_element(By.NAME, "email")
    for letter in adresa_de_email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_adresa_de_email.send_keys(letter)
    assert adresa_de_email, "Caseta 'Adresa de Email' nu este vizibila."
    assert adresa_de_email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    numar_factura = "2024"
    caseta_numar_factura = browser.find_element(By.NAME, "invoice")
    for letter in numar_factura:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_numar_factura.send_keys(letter)
    assert numar_factura, "Caseta 'Numar Factura' nu este vizibila."
    assert numar_factura, "Numarul facturii nu este corect."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,200)")
    time.sleep(2)

    data_factura_an =  browser.find_element(By.CSS_SELECTOR, "#__orderYear > option:nth-child(2)").click()
    browser.find_element(By.NAME, 'order_year').click()
    data_factura_an = browser.find_element(By.XPATH, '//*[@id="__orderYear"]/option[2]')
    data_factura_an.click()
    time.sleep(2)
    click_data_factura_an = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/label')
    click_data_factura_an.click()
    assert data_factura_an, "Caseta 'Data Factura - An' nu este vizibila."
    assert data_factura_an, "Lista 'Data Factura - An' nu este vizibila."
    assert data_factura_an, "'Data Factura - An' nu este corect."
    time.sleep(2)

    data_factura_luna = browser.find_element(By.CSS_SELECTOR, "#__orderMonth > option:nth-child(3)").click()
    browser.find_element(By.NAME, 'order_month').click()
    data_factura_luna = browser.find_element(By.XPATH, '//*[@id="__orderMonth"]/option[3]')
    data_factura_luna.click()
    time.sleep(2)
    click_data_factura_luna = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/label')
    click_data_factura_luna.click()
    assert data_factura_luna, "Caseta 'Data Factura - Luna' nu este vizibila."
    assert data_factura_luna, "Lista 'Data Factura - Luna' nu este vizibila."
    assert data_factura_luna, "'Data Factura - Luna' nu este corecta."
    time.sleep(2)

    data_factura_zi = browser.find_element(By.CSS_SELECTOR, "#__orderDay > option:nth-child(22)").click()
    browser.find_element(By.NAME, 'order_day').click()
    data_factura_zi = browser.find_element(By.XPATH, '//*[@id="__orderDay"]/option[22]')
    data_factura_zi.click()
    time.sleep(2)
    click_data_factura_zi = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/label')
    click_data_factura_zi.click()
    assert data_factura_zi, "Caseta 'Data Factura - Zi' nu este vizibila."
    assert data_factura_zi, "Lista 'Data Factura - Zi' nu este vizibila."
    assert data_factura_zi, "'Data Factura - Zi' nu este corecta."
    time.sleep(2)

    mod_plasare_comanda_telefonic = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/div/input[2]')
    mod_plasare_comanda_telefonic.click()
    assert mod_plasare_comanda_telefonic, "Butonul 'Telefonic' nu este vizibil."
    time.sleep(2)

    mod_plasare_comanda_online = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div/div[1]/form/div[6]/div/input[1]')
    mod_plasare_comanda_online.click()
    assert mod_plasare_comanda_online, "Butonul 'Online' nu este vizibil."
    time.sleep(2)

    cont_bancar_pentru_returnare_contravaloare_comanda = "RO XX XXXX XXXX XXXX XXXX XXXX"
    caseta_cont_bancar_pentru_returnare_contravaloare_comanda = browser.find_element(By.NAME, "bank_account")
    for letter in cont_bancar_pentru_returnare_contravaloare_comanda:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cont_bancar_pentru_returnare_contravaloare_comanda.send_keys(letter)
    assert cont_bancar_pentru_returnare_contravaloare_comanda, "Caseta 'Cont bancar pentru returnare contravaloare comanda' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    produs_returnat = "ANVELOPA PE SARMA CONTINENTAL CROSS KING 26, NEGRU, 58-559, 26X2.3"
    caseta_produs_returnat = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[8]/div/input')
    for letter in produs_returnat:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_produs_returnat.send_keys(letter)
    assert produs_returnat, "Caseta 'Produs returnat' nu este vizibila"
    time.sleep(2)

    motivul_returnarii_produsului = "Anvelopa prezinta urme de uzura."
    caseta_produs_returnat = browser.find_element(By.NAME, "reason")
    for letter in motivul_returnarii_produsului:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_produs_returnat.send_keys(letter)
    assert motivul_returnarii_produsului, "Caseta 'Motivul returnarii produsului' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)")
    time.sleep(2)

    observatii_alte_comentarii = "Solicit inlocuirea produsului ANVELOPA PE SARMA CONTINENTAL CROSS KING 26, NEGRU, 58-559, 26X2.3 cu unul nou."
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
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(2)

    # Test revenire la contul de utilizator/client
    revenire_la_cont = browser.find_element(By.XPATH, '//*[@id="wrapper"]/header/div[2]/div/div/div[3]/ul/li[2]/a/i[1]')
    revenire_la_cont.click()
    assert revenire_la_cont, "Butonul 'Buna, Stelian' nu este vizibil."
    time.sleep(2)

    # Test accesare sectiunea 'Adrese'
    adrese = browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div[2]/ul[3]/li[2]/a')
    adrese.click()
    assert adrese, "Sectiunea 'Adrese' nu este vizibila."
    time.sleep(2)

    # Test adaugare adresa noua - apasare buton 'ADAUGA ADRESA NOUA'
    adauga_adresa_noua = browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[2]/div[2]/div[3]/div/a')
    adauga_adresa_noua.click()
    assert adauga_adresa_noua, "Butonul 'ADAUGA ADRESA NOUA' nu este vizibil."
    time.sleep(2)

    # Test completare sectiunea 'ADAUGA O ADRESA DE LIVRARE'
    nume_adresa_livrare = browser.find_element(By.NAME, 'lastname')
    assert nume_adresa_livrare, "Caseta 'Nume' nu este vizibila."

    prenume_adresa_livrare = browser.find_element(By.NAME, 'firstname')
    assert prenume_adresa_livrare, "Caseta 'Prenume' nu este vizibila."

    selectie_judet = browser.find_element(By.CSS_SELECTOR, '#_shippingRegion > option:nth-child(11)').click()
    browser.find_element(By.XPATH, '//*[@id="_shippingRegion"]').click()
    selectie_judet = browser.find_element(By.XPATH, '//*[@id="_shippingRegion"]/option[11]')
    time.sleep(2)
    selectie_judet.click()
    click_selectie_judet = browser.find_element(By.CSS_SELECTOR, "#_shippingRegionHolder > label")
    click_selectie_judet.click()
    assert selectie_judet, "Caseta 'Judet' nu este vizibila."
    assert selectie_judet, "Lista 'Judet' nu este vizibila."
    assert selectie_judet, "Judetul ales nu este corect."
    time.sleep(2)

    selectie_localitate = browser.find_element(By.CSS_SELECTOR, '#_shippingCity > option:nth-child(3)').click()
    browser.find_element(By.XPATH, '//*[@id="_shippingCity"]').click()
    selectie_localitate = browser.find_element(By.XPATH, '//*[@id="_shippingCity"]/option[3]')
    time.sleep(2)
    selectie_judet.click()
    click_selectie_localitate = browser.find_element(By.CSS_SELECTOR, "#_shippingCityHolder > label")
    click_selectie_localitate.click()
    assert selectie_localitate, "Caseta 'Localitate' nu este vizibila."
    assert selectie_localitate, "Lista 'Localitate' nu este vizibila."
    assert selectie_localitate, "Localitatea aleasa nu este corecta."
    time.sleep(2)

    adresa = "Strada"
    caseta_adresa = browser.find_element(By.XPATH, '//*[@id="addAddress"]/div[8]/input')
    for letter in adresa:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_adresa.send_keys(letter)
    assert adresa, "Caseta 'Adresa' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    cod_postal = "020544"
    caseta_cod_postal = browser.find_element(By.XPATH, '//*[@id="addAddress"]/div[9]/input')
    for letter in cod_postal:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cod_postal.send_keys(letter)
    assert cod_postal, "Caseta 'Cod postal' nu este vizibila."
    time.sleep(2)

    telefon = "0733150829"
    caseta_telefon = browser.find_element(By.XPATH, '//*[@id="addAddress"]/div[10]/input')
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    # Test apasare buton 'SALVEAZA' din sectiunea 'ADAUGA O ADRESA DE LIVRARE'
    salveaza = browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[2]/form/a')
    salveaza.click()
    assert salveaza, "Butonul 'SALVEAZA' nu este vizibil."
    time.sleep(2)

    # Test accesare sectiunea 'Firme'
    firme = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[3]/li[3]/a')
    firme.click()
    assert firme, "Sectiunea 'Firme' nu este vizibila."
    time.sleep(2)

    # Test adaugare firma noua - apasare buton 'ADAUGA FIRMA NOUA'
    adauga_firma_noua = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/div[2]/div[3]/div/a')
    adauga_firma_noua.click()
    assert adauga_firma_noua, "Butonul 'ADAUGA FIRMA NOUA' nu este vizibil."
    time.sleep(2)

    # Test completare formular 'ADAUGA DATE FIRMA'
    cif = "3321870"
    caseta_cif = browser.find_element(By.ID, '__openApiAutocomplete')
    for letter in cif:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cif.send_keys(letter)
    assert cif, "Caseta 'Cautati firma dupa CUI (doar cifre)' nu este vizibila."
    assert cif, "CUI-ul introdus nu este corect."
    time.sleep(2)

    hover = ActionChains(browser)
    selectie_firma = browser.find_element(By.CLASS_NAME, 'autocomplete-suggestion')
    time.sleep(2)
    hover.move_to_element(selectie_firma)
    ActionChains.perform(hover)
    assert selectie_firma, "Firma afisata nu este corecta."
    time.sleep(2)
    selectie_firma.click()
    assert selectie_firma, "Firma selectata nu este corecta."
    time.sleep(2)

    nume_firma = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[2]/input')
    assert nume_firma, "Caseta 'Nume Firma' nu este vizibila."
    assert nume_firma, "Numele firmei nu este corect."

    cui = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[3]/input')
    assert cui, "Caseta 'CUI' nu este vizibila."
    assert cui, "CUI-ul firmei nu este corect."

    nr_registru = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[4]/input')
    assert nr_registru, "Caseta 'Nr. Registru' nu este vizibila."
    assert nr_registru, "J-ul firmei nu este corect."

    platitor_de_tva = browser.find_element(By.XPATH, '//*[@id="companyVatPayer"]')
    assert platitor_de_tva, "Check box-ul 'Platitor de TVA' nu este vizibil."

    browser.execute_script("window.scrollBy(0,200)")
    time.sleep(2)

    banca = "BANCA TRANSILVANIA"
    caseta_banca = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[6]/input')
    for letter in banca:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_banca.send_keys(letter)
    assert banca, "Caseta 'Banca' nu este vizibila."
    time.sleep(2)

    iban = "RO XX XXXX XXXX XXXX XXXX XXXX"
    caseta_iban = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[7]/input')
    for letter in iban:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_iban.send_keys(letter)
    assert iban, "Caseta 'IBAN' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,125)")
    time.sleep(2)

    judet = browser.find_element(By.XPATH, '//*[@id="_shippingRegion"]/option[27]')
    assert judet, "Caseta 'Judet' nu este vizibila."
    assert judet, "Lista 'Judet' nu este vizibila."
    assert judet, "Judetul nu este corect."

    localitate = browser.find_element(By.XPATH, '//*[@id="_shippingCity"]')
    assert localitate, "Caseta 'Localitate' nu este vizibila."
    assert localitate, "Lista 'Localitate' nu este vizibila."
    assert localitate, "Localitatea nu este corecta."

    adresa_firma = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[13]/input')
    assert adresa_firma, "Caseta 'Adresa' nu este vizibila."
    assert adresa_firma, "Adresa nu este corecta."

    cod_postal_firma = "077175"
    caseta_cod_postal_firma = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[14]/input')
    for letter in cod_postal_firma:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cod_postal_firma.send_keys(letter)
    assert cod_postal_firma, "Caseta 'Cod postal' nu este vizibila."
    assert cod_postal_firma, "Codul postal nu este corect."
    time.sleep(2)

    telefon_firma = "0213501427"
    caseta_telefon_firma = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[15]/input')
    for letter in telefon_firma:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon_firma.send_keys(letter)
    assert telefon_firma, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    # Test apasare buton 'SALVEAZA' din sectiunea 'ADAUGA DATE FIRMA'
    salveaza = browser.find_element(By.XPATH, '//*[@id="doSave"]')
    salveaza.click()
    assert salveaza, "Butonul 'SALVEAZA' nu este vizibil."
    time.sleep(2)

    # Test stergere adresa salvata in sectiunea 'Firme'
    stergere_firma = browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[2]/div[3]/div[1]/div/a[2]')
    stergere_firma.click()
    assert stergere_firma, "Butonul 'Sterge' nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(2)
    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    # Test accesare sectiunea 'Date Personale'
    date_personale = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[4]/li[2]/a')
    date_personale.click()
    assert date_personale, "Sectiunea 'Date Personale' nu este vizibila."
    time.sleep(2)

    # Test formular 'DATE PERSONALE' - precompletat cu datele de contact de la crearea contului, in prealabil pentru utilizator/client
    email_date_personale = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[1]/input')
    assert email_date_personale, "Caseta 'Email' nu este vizibila."
    assert email_date_personale, "Adresa de email introdusa nu este corecta."

    nume_date_personale = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[2]/input')
    assert nume_date_personale, "Caseta 'Nume' nu este vizibila."

    prenume_date_personale = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[3]/input')
    assert prenume_date_personale, "Caseta 'Prenume' nu este vizibila."

    telefon_date_personale = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[4]/input')
    assert telefon_date_personale, "Caseta 'Telefon' nu este vizibila."

    # Test apasare buton 'SALVEAZA' din sectiunea 'DATE PERSONALE'
    salveaza_date_personale = browser.find_element(By.XPATH, '//*[@id="doSave"]')
    salveaza_date_personale.click()
    assert salveaza_date_personale, "Butonul 'SALVEAZA' nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    # Test accesare sectiunea 'Modifica Parola'
    modifica_parola = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[4]/li[3]/a')
    modifica_parola.click()
    assert modifica_parola, "Sectiunea 'Modifica Parola' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,50)")
    time.sleep(2)

    # Test modificare parola cont utilizator/client - completare formular 'MODIFICA PAROLA'
    parola_veche = "Sergiu2019@"
    caseta_parola_veche = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[1]/input')
    for letter in parola_veche:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_parola_veche.send_keys(letter)
    assert parola_veche, "Caseta 'Parola Veche' nu este vizibila."
    assert parola_veche, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    parola_noua = "Sergiu2019@"
    caseta_parola_noua = browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[2]/form/div[2]/input')
    for letter in parola_noua:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_parola_noua.send_keys(letter)
    assert parola_noua, "Caseta 'Parola Noua' nu este vizibila."
    assert parola_noua, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    confirma_parola = "Sergiu2019@"
    caseta_confirma_parola = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[3]/input')
    for letter in confirma_parola:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_confirma_parola.send_keys(letter)
    assert confirma_parola, "Caseta 'Confirma Parola' nu este vizibila."
    assert confirma_parola, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    # Test apasare buton 'SALVEAZA' din sectiunea 'MODIFICA PAROLA'
    salveaza_modifica_parola = browser.find_element(By.XPATH, '//*[@id="doSave"]')
    salveaza_modifica_parola.click()
    assert salveaza_date_personale, "Butonul 'SALVEAZA' nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,125)")
    time.sleep(2)

    # Test accesare sectiunea 'Stergere cont'
    stergere_cont = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[4]/li[4]/a')
    stergere_cont.click()
    assert stergere_cont, "Sectiunea 'Stergere cont' nu este vizibila."
    time.sleep(2)

    # Test apasare buton 'STERGERE CONT'
    buton_stergere_cont = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/a')
    assert buton_stergere_cont, "Butonul 'STERGERE CONT' nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    # Test accesare sectiunea 'Logout' 
    logout = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[5]/li/a')
    logout.click()
    assert logout, "Sectiunea 'Logout' nu este vizibila."
    time.sleep(3)


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
    search_produs = "BICICLETA ROCK MACHINE CROSSRIDE 100 29'' NEGRU/ROSU M-18''"
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


# 7. Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principala si finalizare comanda
def test_produs_1(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(2) 

    # Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principala
    search_produs = "BICICLETA ROCK MACHINE CROSSRIDE 100 29'' NEGRU/ROSU M-18''"
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
    user_email = 'stelian.dragne@yahoo.com'
    email = browser.find_element(By.ID, '_loginEmail')
    for letter in user_email:
        time.sleep(random.uniform(0.05, 0.05))
        email.send_keys(letter)
    assert user_email, "Caseta 'Email' nu este vizibila."
    assert user_email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    user_password = "Sergiu2019@"
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
    mesaj = "Va multumesc pentru operativitate !"
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
    search_produs = "BICICLETA ROCK MACHINE CROSSRIDE 100 29'' NEGRU/ROSU M-18''"
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
    search_produs_2 = "ANVELOPA PE SARMA CONTINENTAL CROSS KING 26, NEGRU, 58-559, 26X2.3"
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
    user_email = 'stelian.dragne@yahoo.com'
    email = browser.find_element(By.ID, '_loginEmail')
    for letter in user_email:
        time.sleep(random.uniform(0.05, 0.05))
        email.send_keys(letter)
    assert user_email, "Caseta 'Email' nu este vizibila."
    assert user_email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    user_password = "Sergiu2019@"
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
    mesaj = "Va multumesc pentru operativitate !"
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


# 9. Test sortare 'Biciclete Mountainbike' din sectiunea 'TOATE PRODUSELE'
def test_sortare_biciclete_mountainbike(browser: webdriver.Chrome):
    # Test accesare site
    browser.get("https://www.mosionroata.ro/")
    time.sleep(2)

    # Test acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    cookie.click()
    assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(2) 

    # Test accesare sectiune 'TOATE PRODUSELE' -> 'Biciclete'
    hover = ActionChains(browser)
    biciclete = browser.find_element(By.CSS_SELECTOR, "#main-menu > div > ul > li.all-product-button.menu-drop > div > ul > li:nth-child(1) > a > i")
    assert biciclete, ("Sectiunea 'Biciclete' nu este vizibila.")
    time.sleep(2)
    hover.move_to_element(biciclete)
    ActionChains.perform(hover)
    time.sleep(2)

    # Test accesare sectiune 'TOATE PRODUSELE' -> 'Biciclete' -> 'Biciclete Mountainbike'
    biciclete_mountainbike = browser.find_element(By.CSS_SELECTOR, '#main-menu > div > ul > li.all-product-button.menu-drop > div > ul > li:nth-child(1) > ul > li:nth-child(2) > div > p > a')
    time.sleep(2)
    hover.move_to_element(biciclete_mountainbike)
    ActionChains.perform(hover)
    time.sleep(2)
    biciclete_mountainbike.click()
    assert biciclete_mountainbike, "Sectiunea 'Biciclete Mountainbike' nu este vizibila."
    time.sleep(2)

    # Test scroll pe verticala pagina 'Biciclete Mountainbike' pentru vizualizare filtre disponibile
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 8:
            break
        time.sleep(1.3)
    time.sleep(2)

    browser.get("https://www.mosionroata.ro/biciclete-mountainbike")
    time.sleep(2)

    # Test accesare filtre in pagina 'Biciclete Mountainbike'
    browser.execute_script("window.scrollBy(0,300)")
    time.sleep(2)

    # Test selectie filtru 'Producatori'
    rock_machine = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[2]/ul/li[4]/label/div')
    rock_machine.click()
    assert rock_machine, "Filtrul 'Rock Machine' nu este vizibil."

    browser.execute_script("window.scrollBy(0,300)")
    time.sleep(2)

    # Test selectie filtru 'Gen'
    barbati = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[4]/ul/li[1]/label/div')
    barbati.click()
    assert barbati, "Filtrul 'Barbati' nu este vizibil."

    browser.execute_script("window.scrollBy(0,350)")
    time.sleep(2)

    # Test selectie filtru 'Diametru roti'
    diametru_roti = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[5]/ul/li/label/div')
    diametru_roti.click()
    assert diametru_roti, "Filtrul '29 inch' nu este vizibil."

    browser.execute_script("window.scrollBy(0,350)")
    time.sleep(2)

    # Test selectie filtru 'Material'
    material = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[6]/ul/li/label/div')
    material.click()
    assert material, "Filtrul 'Aluminiu' nu este vizibil."

    browser.execute_script("window.scrollBy(0,400)")
    time.sleep(2)

    # Test selectie filtru 'Viteze'
    viteze = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[7]/ul/li/label/div')
    viteze.click()
    assert viteze, "Filtrul '21 viteze' nu este vizibil."

    browser.execute_script("window.scrollBy(0,550)")
    time.sleep(2)

    # Test selectie filtru 'Tip furca bicicleta'
    furca_cu_suspensie = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[8]/ul/li/label/div')
    furca_cu_suspensie.click()
    assert furca_cu_suspensie, "Filtrul 'Furca cu suspensie' nu este vizibil."

    browser.execute_script("window.scrollBy(0,550)")
    time.sleep(2)

    # Test selectie filtru 'Suspensie spate'
    suspensie_spate = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[9]/ul/li/label/div')
    suspensie_spate.click()
    assert suspensie_spate, "Filtrul 'Nu' nu este vizibil."

    browser.execute_script("window.scrollBy(0,650)")
    time.sleep(2)

    # Test selectie filtru 'Sistem franare biciclete'
    franare = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[10]/ul/li/label/div')
    franare.click()
    assert franare, "Filtrul 'Pe janta' nu este vizibil."

    browser.execute_script("window.scrollBy(0,750)")
    time.sleep(2)

    # Test selectie filtru 'Culori continute'
    culori = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[11]/ul/li[1]/label/div')
    culori.click()
    assert culori, "Filtrul 'Negru' nu este vizibil."

    browser.execute_script("window.scrollBy(0,1000)")
    time.sleep(2)

    # Test selectie filtru 'Marime Cadru'
    marime = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[12]/ul/li[3]/label/div')
    marime.click()
    assert marime, "Filtrul '53cm' nu este vizibil."

    browser.execute_script("window.scrollBy(0,1000)")
    time.sleep(2)

    # Test selectie filtru 'Status stoc'
    stoc_magazin = browser.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/div[13]/ul/li[1]/label/div')
    stoc_magazin.click()
    assert stoc_magazin, "Filtrul 'Stoc Magazin' nu este vizibil."

    browser.execute_script("window.scrollBy(0,1000)")
    time.sleep(2)

    # Test vizualizare produs asupra caruia au fost aplicate filtrele de selectie
    browser.execute_script("window.scrollTo(0,475)")
    time.sleep(2)

    vezi_variante = browser.find_element(By.XPATH, '//*[@id="category-page"]/div/div[3]/div[3]/div/div/div/div[2]/div[2]/div[1]/a/span')
    vezi_variante.click()
    assert vezi_variante, "Butonul 'VEZI VARIANTE' nu este vizibil."
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,200)")
    time.sleep(3)


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
    nume_si_prenume = "DRAGNE Stelian"
    caseta_nume_si_prenume = browser.find_element(By.NAME, "name")
    for letter in nume_si_prenume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume_si_prenume.send_keys(letter)
    assert nume_si_prenume, "Caseta 'Nume si Prenume' nu este vizibila."
    time.sleep(2)

    telefon = "0733150829"
    caseta_telefon = browser.find_element(By.NAME, "phone")
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    adresa_de_email = "stelian.dragne@yahoo.com"
    caseta_adresa_de_email = browser.find_element(By.NAME, "email")
    for letter in adresa_de_email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_adresa_de_email.send_keys(letter)
    assert adresa_de_email, "Caseta 'Adresa de Email' nu este vizibila."
    assert adresa_de_email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    numar_factura = "2024"
    caseta_numar_factura = browser.find_element(By.NAME, "invoice")
    for letter in numar_factura:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_numar_factura.send_keys(letter)
    assert numar_factura, "Caseta 'Numar Factura' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,200)")
    time.sleep(2)

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

    cont_bancar_pentru_returnare_contravaloare_comanda = "RO XX XXXX XXXX XXXX XXXX XXXX"
    caseta_cont_bancar_pentru_returnare_contravaloare_comanda = browser.find_element(By.NAME, "bank_account")
    for letter in cont_bancar_pentru_returnare_contravaloare_comanda:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cont_bancar_pentru_returnare_contravaloare_comanda.send_keys(letter)
    assert cont_bancar_pentru_returnare_contravaloare_comanda, "Caseta 'Cont bancar pentru returnare contravaloare comanda' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    produs_returnat = "ANVELOPA PE SARMA CONTINENTAL CROSS KING 26, NEGRU, 58-559, 26X2.3"
    caseta_produs_returnat = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[8]/div/input')
    for letter in produs_returnat:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_produs_returnat.send_keys(letter)
    assert produs_returnat, "Caseta 'Produs returnat' nu este vizibila"
    time.sleep(2)

    motivul_returnarii_produsului = "Anvelopa prezinta urme de uzura."
    caseta_produs_returnat = browser.find_element(By.NAME, "reason")
    for letter in motivul_returnarii_produsului:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_produs_returnat.send_keys(letter)
    assert motivul_returnarii_produsului, "Caseta 'Motivul returnarii produsului' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)")
    time.sleep(2)

    observatii_alte_comentarii = "Solicit inlocuirea produsului ANVELOPA PE SARMA CONTINENTAL CROSS KING 26, NEGRU, 58-559, 26X2.3 cu unul nou."
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
    nume_si_prenume = "DRAGNE Stelian"
    caseta_nume_si_prenume = browser.find_element(By.NAME, 'name')
    for letter in nume_si_prenume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume_si_prenume.send_keys(letter)
    assert nume_si_prenume, "Caseta 'Nume si Prenume' nu este vizibila."
    time.sleep(2)

    telefon = "0733150829"
    caseta_telefon = browser.find_element(By.NAME, "phone")
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    adresa_de_email = "stelian.dragne@yahoo.com"
    caseta_adresa_de_email = browser.find_element(By.NAME, "email")
    for letter in adresa_de_email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_adresa_de_email.send_keys(letter)
    assert adresa_de_email, "Caseta 'Adresa de Email' nu este vizibila."
    time.sleep(2)

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

    adresa_de_ridicare_colet = "Strada"
    caseta_adresa_de_ridicare_colet = browser.find_element(By.NAME, "pickup_address")
    for letter in adresa_de_ridicare_colet:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_adresa_de_ridicare_colet.send_keys(letter)
    assert adresa_de_ridicare_colet, "Caseta 'Adresa de Ridicare Colet' nu este vizibila."
    time.sleep(2)

    numar_factura = "2024"
    caseta_numar_factura = browser.find_element(By.NAME, "invoice")
    for letter in numar_factura:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_numar_factura.send_keys(letter)
    assert numar_factura, "Caseta 'Numar Factura' nu este vizibila."
    time.sleep(2)

    data_factura = "21.09.2024"
    caseta_data_factura = browser.find_element(By.NAME, "invoice_date")
    for letter in data_factura:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_data_factura.send_keys(letter)
    assert data_factura, "Caseta 'Data Factura' mu este vizibila."
    time.sleep(2)

    denumire_produs = "BICICLETA ROCK MACHINE CROSSRIDE 100 29'' NEGRU/ROSU M-18''"
    caseta_denumire_produs = browser.find_element(By.NAME, "product")
    for letter in denumire_produs:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_denumire_produs.send_keys(letter)
        assert denumire_produs, "Caseta 'Denumire Produs' nu este vizibila."
    time.sleep(2)

    descrierea_problemei_intampinate = "Cadrul bicicletei este stramb, roata spate este ovala si ghidonul se misca foarte greu stanga-dreapta, iar cateodata ramane blocat."
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
    email = "stelian.dragne@yahoo.com"
    caseta_email = browser.find_element(By.XPATH, '//*[@id="email"]')
    for letter in email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_email.send_keys(letter)
    assert email, "Caseta 'Email' nu este vizibila."
    assert email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    nume = "Stelian DRAGNE"
    caseta_nume = browser.find_element(By.NAME, 'lastname')
    for letter in nume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume.send_keys(letter)
    assert nume, "Caseta 'Nume' nu este vizibila."
    time.sleep(2)

    telefon = "0733150829"
    caseta_telefon = browser.find_element(By.NAME, "phone")
    for letter in telefon:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_telefon.send_keys(letter)
    assert telefon, "Caseta 'Telefon' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,125)")
    time.sleep(1)

    mesaj = "Va rog sa ma contactati cat mai repede posibil. Comanda mea inca nu a fost livrata."
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
    email = "stelian.dragne@yahoo.com"
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