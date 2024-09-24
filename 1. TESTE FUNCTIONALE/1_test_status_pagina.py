"""

    1.  Test verificare status pagina principala.
        Acest test va verifica daca pagina principala a site-ului ales pentru testare este activa si nu returneaza un cod de eroare, cel pregonizat fiind 200.

"""




from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
import pytest




# Accesare browser CHROME
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