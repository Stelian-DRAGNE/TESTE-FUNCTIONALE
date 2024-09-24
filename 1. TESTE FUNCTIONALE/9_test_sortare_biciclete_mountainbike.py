"""

    9.  Test sortare 'Biciclete Mountainbike' din sectiunea 'TOATE PRODUSELE'.
        Acest test va efectua sortarea produselor 'Biciclete Mountainbike' din sectiunea "TOATE PRODUSELE", in urma aplicarii filtrelor dorite, disponibile pe pagina 'Biciclete Mountainbike'.

"""




from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
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