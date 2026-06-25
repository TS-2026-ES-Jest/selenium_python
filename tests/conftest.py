import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # executa o teste sem abrir o navegador

    navegador = webdriver.Chrome(options=options)
    yield navegador
    navegador.quit()


@pytest.fixture(scope="session")
def driver_visivel():
    navegador = webdriver.Chrome()
    yield navegador
    time.sleep(5)                           # aguarda n segundos antes de fechar o navegador
    navegador.quit()