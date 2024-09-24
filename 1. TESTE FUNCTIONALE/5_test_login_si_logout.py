"""

    5.  Test "Intra pe cont" pe site, in cont de utilizator/client creat in prealabil, verificare sectiuni disponibile, si apoi 'Logout'.
        In prealabil s-a creat un cont de utilizator/client, necesar ulterior in cadrul urmatoarelor teste.   Acest test va efectua logarea pe contul de utilizator/client, deja creat.

"""




from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
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

    email_inregistrare_cont = "........" # Se introduce adresa de email dorita
    email = browser.find_element(By.ID, "__emailRegister")
    for letter in email_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        email.send_keys(letter)
    assert email_inregistrare_cont, "Caseta 'Email' nu este vizibila."
    assert email_inregistrare_cont, "Email-ul introdus nu este corect."
    time.sleep(2)

    nume_inregistrare_cont = "........" # Se introduce numele dorit
    nume = browser.find_element(By.ID, "__lastnameRegister")
    for letter in nume_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        nume.send_keys(letter)
    assert nume_inregistrare_cont, "Caseta 'Nume' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)") 
    time.sleep(2)

    prenume_inregistrare_cont = "........" # Se introduce prenumele dorit
    prenume = browser.find_element(By.ID, "__firstnameRegister")
    for letter in prenume_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        prenume.send_keys(letter)
    assert email_inregistrare_cont, "Caseta 'Prenume' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,75)") 
    time.sleep(2)

    parola_inregistrare_cont = "........" # Se introduce parola dorita
    parola = browser.find_element(By.ID, "__passwordRegister")
    for letter in parola_inregistrare_cont:
        time.sleep(random.uniform(0.05, 0.05))
        parola.send_keys(letter)
    assert parola_inregistrare_cont, "Caseta 'Parola' nu este vizibila."
    assert parola_inregistrare_cont, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)") 
    time.sleep(2)

    confirmare_parola_inregistrare_cont = "........" # Se reintroduce parola dorita
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

    user_email = "........" # Se introduce adresa de email cu care s-a creat anterior contul de utilizator/client
    email = browser.find_element(By.ID, '_loginEmail')
    for letter in user_email:
        time.sleep(random.uniform(0.05, 0.05))
        email.send_keys(letter)
    assert user_email, "Caseta 'Email' nu este vizibila."
    assert user_email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    user_password = "........" # Se introduce parola cu care s-a creat anterior contul de utilizator/client
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
    numar_comanda = "........" # Se introduce numar de comanda real sau fictiv
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

    # Test accesare sectiune 'Status comanda'
    status_comanda = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/ul[2]/li[4]/a')
    status_comanda.click()
    assert status_comanda, "Sectiunea 'Status comanda' nu este disponibila."
    time.sleep(2)

    # Test cautare dupa numar comanda, in sectiunea 'Status comanda' 
    status_numar_comanda = "........" # Se introduce numar de comanda real sau fictiv
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
    nume_si_prenume = "........" # Se introduce nume si prenume
    caseta_nume_si_prenume = browser.find_element(By.NAME, "name")
    for letter in nume_si_prenume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume_si_prenume.send_keys(letter)
    assert nume_si_prenume, "Caseta 'Nume si Prenume' nu este vizibila."
    time.sleep(2)

    telefon = "........" # Se introduce numar de telefon
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

    numar_factura = "........" # Se introduce numar de factura real sau fictiv
    caseta_numar_factura = browser.find_element(By.NAME, "invoice")
    for letter in numar_factura:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_numar_factura.send_keys(letter)
    assert numar_factura, "Caseta 'Numar Factura' nu este vizibila."
    assert numar_factura, "Numarul facturii nu este corect."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,200)")
    time.sleep(2)

    # Pentru : data_factura_an, data_factura_luna si data_factura_zi, vor trebui actualizare reperele calendaristice din site, in functie de disponibilitate
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

    cont_bancar_pentru_returnare_contravaloare_comanda = "........" # Se introduce numar de cont real sau fictiv
    caseta_cont_bancar_pentru_returnare_contravaloare_comanda = browser.find_element(By.NAME, "bank_account")
    for letter in cont_bancar_pentru_returnare_contravaloare_comanda:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cont_bancar_pentru_returnare_contravaloare_comanda.send_keys(letter)
    assert cont_bancar_pentru_returnare_contravaloare_comanda, "Caseta 'Cont bancar pentru returnare contravaloare comanda' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    produs_returnat = "........" # Se introduce orice produs care se regaseste pe site-ul 'https://www.mosionroata.ro/'
    caseta_produs_returnat = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[8]/div/input')
    for letter in produs_returnat:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_produs_returnat.send_keys(letter)
    assert produs_returnat, "Caseta 'Produs returnat' nu este vizibila"
    time.sleep(2)

    motivul_returnarii_produsului = "........" # Se introduce textul dorit
    caseta_produs_returnat = browser.find_element(By.NAME, "reason")
    for letter in motivul_returnarii_produsului:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_produs_returnat.send_keys(letter)
    assert motivul_returnarii_produsului, "Caseta 'Motivul returnarii produsului' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)")
    time.sleep(2)

    observatii_alte_comentarii = "........" # Se introduce textul dorit
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
    assert revenire_la_cont, "Butonul 'Buna, '........' nu este vizibil."
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
    # Numele si prenumele vor fi preluate din contul de utilizator/client, deja creat
    nume_adresa_livrare = browser.find_element(By.NAME, 'lastname')
    assert nume_adresa_livrare, "Caseta 'Nume' nu este vizibila."

    prenume_adresa_livrare = browser.find_element(By.NAME, 'firstname')
    assert prenume_adresa_livrare, "Caseta 'Prenume' nu este vizibila."

    # In functie de necesitate, va trebui modificat codul prin adaugarea reperelor din site
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

    adresa = "........" # Se introduce adresa dorita
    caseta_adresa = browser.find_element(By.XPATH, '//*[@id="addAddress"]/div[8]/input')
    for letter in adresa:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_adresa.send_keys(letter)
    assert adresa, "Caseta 'Adresa' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(2)

    cod_postal = "........" # Se introduce Codul postal dorit
    caseta_cod_postal = browser.find_element(By.XPATH, '//*[@id="addAddress"]/div[9]/input')
    for letter in cod_postal:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cod_postal.send_keys(letter)
    assert cod_postal, "Caseta 'Cod postal' nu este vizibila."
    time.sleep(2)

    telefon = "........" # Se introduce numarul de telefon dorit
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
    cif = "........" # Se introduce CIF-ul dorit
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

    banca = "........" # Se introduce numele bancii dorit
    caseta_banca = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[6]/input')
    for letter in banca:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_banca.send_keys(letter)
    assert banca, "Caseta 'Banca' nu este vizibila."
    time.sleep(2)

    iban = "........" # Se introduce contul bancar dorit
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

    cod_postal_firma = "........" # Se introduce Codul postal dorit
    caseta_cod_postal_firma = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[14]/input')
    for letter in cod_postal_firma:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_cod_postal_firma.send_keys(letter)
    assert cod_postal_firma, "Caseta 'Cod postal' nu este vizibila."
    assert cod_postal_firma, "Codul postal nu este corect."
    time.sleep(2)

    telefon_firma = "........" # Se introduce numarul de telefon dorit
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
    parola_veche = "........" # Se introduce parola initiala
    caseta_parola_veche = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[2]/form/div[1]/input')
    for letter in parola_veche:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_parola_veche.send_keys(letter)
    assert parola_veche, "Caseta 'Parola Veche' nu este vizibila."
    assert parola_veche, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    parola_noua = "........" # Se introduce parola noua
    caseta_parola_noua = browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[2]/form/div[2]/input')
    for letter in parola_noua:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_parola_noua.send_keys(letter)
    assert parola_noua, "Caseta 'Parola Noua' nu este vizibila."
    assert parola_noua, "Parola introdusa nu este corecta. Parola trebuie sa contina minim 8 caractere, cel putin o litera mare, cel putin o cifra si cel putin un caracter special."
    time.sleep(2)

    confirma_parola = "........" # Se introduce parola noua, pentru confirmare
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