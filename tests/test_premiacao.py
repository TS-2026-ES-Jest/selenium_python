import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from constants import TEST_CASES, URL_BASE

def test_classificacao(driver_visivel, test_case):
    # Arrange
    distancia = test_case["distancia"]
    litros = test_case["litros"]

    driver_visivel.get(URL_BASE)

    # Act
    inputs = driver_visivel.find_elements(By.CLASS_NAME, "campo-calculo")
    button = driver_visivel.find_element(By.CLASS_NAME, "botao-calcular")

    inputs[0].clear()
    inputs[1].clear()

    inputs[0].send_keys(distancia)
    inputs[1].send_keys(litros)

    time.sleep(1)
    button.click()
    time.sleep(1)

    # Assert
    consumo = driver_visivel.find_element(By.CLASS_NAME, "resultado-consumo")
    classificacao = driver_visivel.find_element(By.CLASS_NAME, "resultado-classificacao")
    assert (consumo.text == test_case["consumo"] and classificacao.text == test_case["classificacao"])

driver = webdriver.Chrome()

for i in range(0, len(TEST_CASES)):
    test_classificacao(driver, TEST_CASES[i])

driver.close()

