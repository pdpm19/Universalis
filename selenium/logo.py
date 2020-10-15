# Logo
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import time

def Logo(simulationData):
    global webdriver, driver   # Browser doesn't close in the end

    # Logs in Tranquilidade account
    driver.execute_script(
        "window.open('https://www.logo.pt/?&externalLogoff&expandLogin=true&t=AUTOM&r1-portlet=true');")
    driver.switch_to_window(driver.window_handles[3])

    loginCloseButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
        '/html/body/div[1]/div[5]/div[1]/div/div/div[2]/div[1]/img'))
    loginCloseButtonElement.click()

    if simulationData.viaturaCategoria == 'Ligeiro Passageiros' or simulationData.viaturaCategoria == 'Ligeiro Mercadorias':
        vehicleCategoryFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath('/html/body/footer/div[1]/ul/li[1]/a/span'))
        vehicleCategoryFieldElement.click()
    elif simulationData.viaturaCategoria == 'Ligeiro Mercadorias':
        vehicleCategoryFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id('bean.categoriaVeiculo_1'))
        vehicleCategoryFieldElement.click()
    elif simulationData.viaturaCategoria == 'Motociclo':
        vehicleCategoryFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id('bean.categoriaVeiculo_2'))
        vehicleCategoryFieldElement.click()
    elif simulationData.viaturaCategoria == 'Ciclomotor':
        vehicleCategoryFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id('bean.categoriaVeiculo_3'))
        vehicleCategoryFieldElement.click()
    else:
        exit(-1)

    time.sleep(5)

    licenceFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_id('matricula'))
    licenceFieldElement.send_keys(simulationData.viaturaMatricula)

    # monthConstructionFieldElement = WebDriver(driver, 10).until(lambda driver: driver.find_element_by_id('dtConstrucaoMes'))
    # monthConstructionFieldElement.send_keys(simulationData.)

    brandFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_id('marcaMod'))
    brandFieldElement.send_keys(simulationData.viaturaMarca)

    modelFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_id('bean.modeloVeiculo'))
    modelFieldElement.send_keys(simulationData.viaturaModelo)