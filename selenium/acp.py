# ACP
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import time

def ACP(driver, simulationData, windowHandler: int):
    localData = simulationData
    driver.execute_script(
        "window.open('https://www.acp.pt/saude-e-seguros/simuladores/simulador-seguro-automovel');")
    driver.switch_to_window(driver.window_handles[windowHandler])

    cookiesFieldXPath = '/html/body/div[1]/div/button'
    licencePlateDateFieldXPath = '//*[@id="inputMatriculaData"]'
    categoryFieldXPath = '//*[@id="inputTipo"]'
    brandFieldXPath = '//*[@id="inputMarca"]'
    modelFieldXPath = '//*[@id="inputModelo"]'
    versionFieldXPath = '//*[@id="inputVersao"]'
    licencePlateFieldXPath = '//*[@id="inputMatricula"]'
    fowardFieldXPath = '/html/body/div[1]/div/div[2]/div/div/div/a'
    iframeXPath = '/html/body/form/div[9]/div[3]/div/p[2]/iframe'

    cookiesElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(cookiesFieldXPath))
    cookiesElement.click()

    driver.execute_script('window.scrollTo(0, 768)')

    # Changes to correct iframe
    iframeElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(iframeXPath))
    driver.switch_to.frame(iframeElement)

    # Vehicle info
    licencePlateDateElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(licencePlateDateFieldXPath))
    categoryElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(categoryFieldXPath))
    brandElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(brandFieldXPath))
    modelElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(modelFieldXPath))
    versionElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(versionFieldXPath))
    licencePlateElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(licencePlateFieldXPath))
    fowardElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(fowardFieldXPath))

    # Sends the data to forms
    licencePlateDateElement.click()
    licencePlateDateElement.send_keys(simulationData.viaturaDataMatricula)
    if simulationData.viaturaCategoria == 'Ligeiro Instrução' or simulationData.viaturaCategoria == 'Ligeiro Mercadorias' or simulationData.viaturaCategoria == 'Ligeiro Passageiros/Aluguer' or simulationData.viaturaCategoria == 'Táxi':
        select = Select(categoryElement)
        select.select_by_visible_text('Ligeiro de passageiros')
    else:
        # Waits 10 seconds for humam input
        time.sleep(10)
    
    time.sleep(1)
    select = Select(brandElement)
    select.select_by_visible_text(simulationData.viaturaMarca.upper())
    
    time.sleep(1)
    select = Select(modelElement)
    for each_option in select.options:
        if simulationData.viaturaModelo in each_option.text:
            value = each_option.get_attribute("value")
            select.select_by_value(value)
            break
    
    time.sleep(1)
    select = Select(versionElement)
    for each_option in select.options:
        if simulationData.viaturaVersao in each_option.text:
            value = each_option.get_attribute("value")
            select.select_by_value(value)
            break
    
    licencePlateElement.send_keys(simulationData.viaturaMatricula)
    
    fowardElement.click()
    
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(1)
    # Owner data
    nameXPath = '/html/body/div[1]/div/div[2]/div/div/form/div[2]/div[1]/div/input'
    nifXPath = '/html/body/div[1]/div/div[2]/div/div/form/div[2]/div[2]/div/input'
    birthdateXPath = '/html/body/div[1]/div/div[2]/div/div/form/div[3]/div[1]/div/input'
    licenceDateXPath = '/html/body/div[1]/div/div[2]/div/div/form/div[3]/div[2]/div/input'
    zipcodeXPath = '/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input'
    insuranceYearsXPath = '/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[2]/div/select'
    yearWithoutAccidentXPath = '/html/body/div[1]/div/div[2]/div/div/form/div[5]/div[1]/div/select'
    utilizationConditionsXPath = '/html/body/div[1]/div/div[2]/div/div/form/div[7]/div/input[2]'
    submitButtonXPath = '/html/body/div[1]/div/div[2]/div/div/form/button'

    nameElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(nameXPath))
    nifElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(nifXPath))
    birthdateElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(birthdateXPath))
    licenceDateElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(licenceDateXPath))
    zipcodeElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(zipcodeXPath))
    insuranceYearsElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(insuranceYearsXPath))
    yearWithoutAccidentElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(yearWithoutAccidentXPath))
    utilizationConditionsElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(utilizationConditionsXPath))
    submitButtonElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(submitButtonXPath))
    
    #### GUI has no Name field, so waits for humam input ####
    # nameElement.click()
    # nameElement.send_keys('text')
    nifElement.send_keys(simulationData.tomadorNIF)
    print('AQUI')
    print(simulationData.tomadorDataNascimento)

    birthdateElement.send_keys(simulationData.tomadorDataNascimento)
    licenceDateElement.send_keys(simulationData.tomadorDataCarta)
    zipcodeElement.send_keys(simulationData.tomadorCodPostal)

    if simulationData.tomadorPrimeiroSeguro == True:
        ensuranceYears = '0'
        accidentYears = '0'
    else:
        startYear = int(simulationData.condutorDataCarta[len(simulationData.condutorDataCarta)-4:])
        ensuranceYears = 2020 - startYear
        if ensuranceYears > 10:
            ensuranceYears = '10+'
        else:
            ensuranceYears = str(ensuranceYears)
        
        lastAccidentYear = int(simulationData.condutorDataCarta[len(simulationData.condutorDataCarta)-4:])
        accidentYears = 2020 - lastAccidentYear
        if accidentYears > 10:
            accidentYears = '10+'
        else:
            accidentYears = str(accidentYears)
    
    time.sleep(1)
    select = Select(insuranceYearsElement)
    for each_option in select.options:
        if ensuranceYears in each_option.text:
            value = each_option.get_attribute("value")
            select.select_by_value(value)
            break
    
    
    time.sleep(1)
    select = Select(yearWithoutAccidentElement)
    for each_option in select.options:
        if accidentYears in each_option.text:
            value = each_option.get_attribute("value")
            select.select_by_value(value)
            break
    
    # utilizationConditionsElement.click()
