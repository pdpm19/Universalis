# Caravela
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import time


def Caravela(driver, user: str, password: str, simulationData, windowHandler: int):
    if windowHandler != 0:
        driver.execute_script(
            "window.open('http://egis.caravelaseguros.pt/eGIS/logon.jsp');")

        driver.switch_to_window(driver.window_handles[windowHandler])

    else:
        driver.get('http://egis.caravelaseguros.pt/eGIS/logon.jsp')
        driver.maximize_window()
        driver.switch_to_window(driver.window_handles[windowHandler])

    userFieldXPath = '/html/body/div/table/tbody/tr/td[2]/form/table/tbody/tr[3]/td/input'
    passwordFieldXPath = '/html/body/div/table/tbody/tr/td[2]/form/table/tbody/tr[5]/td/input'
    submitFieldXPath = '/html/body/div/table/tbody/tr/td[2]/form/table/tbody/tr[6]/td/input'

    # User info
    userElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(userFieldXPath))
    passwordElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(passwordFieldXPath))
    submitElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(submitFieldXPath))

    # Sends the data to form
    userElement.send_keys(user)
    passwordElement.send_keys(password)
    submitElement.click()

    simulationFieldXPath = '/html/body/div[1]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table[1]/tbody/tr/td/table/tbody/tr[1]/td[2]/a'
    simulationElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(simulationFieldXPath))

    simulationElement.click()
    iframeXPath = '/html/body/div[1]/table/tbody/tr[1]/td[2]/iframe'
    # Changes to correct iframe
    iframeElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(iframeXPath))
    driver.switch_to.frame(iframeElement)

    vehicleXPath = '/html/body/form/center/table/tbody/tr[12]/td[2]/a'

    vehicleElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(vehicleXPath))
    vehicleElement.click()

    # Tomador
    nifXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[1]/td/span/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input'
    zipcodeXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[1]/td/span/div/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input[2]'
    zipcodeSubmitXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[1]/td/span/div/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/span[1]/input'

    # Condições do seguro
    startingEnsuranceXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/input'
    conditionsXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[9]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'

    # Condutor Hab.
    birthdateXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/input'
    driverLicenceXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/input'
    ensuranceYearsXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input'
    lastAccidentDateXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[7]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/input'
    segurnetCertificationXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[9]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'
    fiveYearsAccidentsXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[10]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'
    twoYearsAccidentsXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[11]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'

    # Vehicle
    firstLicenceXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[4]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/input' 
    categoryXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[4]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'
    selectVehicleXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[4]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[5]/td/table/tbody/tr/td[2]/span[1]/input'
    licencePlateTypeXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[4]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[7]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'
    licencePlateXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[4]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[7]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/input'
    vehicleUseXPath = '/html/body/div[1]/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[4]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table[1]/tbody/tr[18]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'
    brandXPath = '/html/body/form[1]/table[1]/tbody/tr/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'
    modelXPath = '/html/body/form[1]/table[1]/tbody/tr/td/span/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'
    versionXPath = '/html/body/form[1]/table[1]/tbody/tr/td/span/div/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/select'
    searchXPath = '/html/body/form[1]/table[2]/tbody/tr[2]/td/span/input'

    # Sends data to Forms
    # Tomador
    nifElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(nifXPath))
    zipcodeElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(zipcodeXPath))
    zicodeSearchElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(zipcodeSubmitXPath))
    nifElement.send_keys(simulationData.tomadorNIF)
    zipcodeElement.send_keys(simulationData.tomadorCodPostal)
    zicodeSearchElement.click()

    # Condições do seguro
    time.sleep(3)
    # driver.execute_script('%s.contentWindow.scrollTo(0, 768);' %iframe)
    startingEnsuranceElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(startingEnsuranceXPath))
    conditionsElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(conditionsXPath))
    data = simulationData.dataInicio[6:] + \
        simulationData.dataInicio[2:6] + simulationData.dataInicio[:2]
    startingEnsuranceElement.clear()    
    startingEnsuranceElement.send_keys(data)

    # Condutor Hab.
    # driver.execute_script('window.scrollTo(0, 768)')
    birthdateElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(birthdateXPath))
    driverLicenceElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(driverLicenceXPath))
    ensuranceYearsElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(ensuranceYearsXPath))
    lastAccidentDateElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(lastAccidentDateXPath))
    segurnetCertificationElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(segurnetCertificationXPath))
    fiveYearsAccidentsElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(fiveYearsAccidentsXPath))
    twoYearsAccidentsElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(twoYearsAccidentsXPath))
    data = simulationData.tomadorDataNascimento[6:] + \
        simulationData.tomadorDataNascimento[2:6] + \
        simulationData.tomadorDataNascimento[:2]
    print(data)
    birthdateElement.clear()
    birthdateElement.send_keys(data)

    data = simulationData.tomadorDataCarta[6:] + \
        simulationData.tomadorDataCarta[2:6] + \
        simulationData.tomadorDataCarta[:2]
    driverLicenceElement.send_keys(data)
    # ensuranceYearsElement.send_keys('1')
    # Se não existiram acidentes, mete a data da carta
    # lastAccidentDateElement.send_keys('2020/05/13')

    # Vehicle
    # driver.execute_script('window.scrollTo(0, 768)')
    firstLicenceElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(firstLicenceXPath))
    categoryElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(categoryXPath))
    selectVehicleElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(selectVehicleXPath))
    licencePlateElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(licencePlateXPath))
    licencePlateTypeElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(licencePlateTypeXPath))

    select = Select(licencePlateTypeElement)
    for each_option in select.options:
        if simulationData.viaturaTipoMatricula in each_option.text:
            value = each_option.get_attribute("value")
            select.select_by_value(value)
            break
    data = simulationData.viaturaDataMatricula[6:] + \
        simulationData.viaturaDataMatricula[2:6] + \
        simulationData.viaturaDataMatricula[:2]
    firstLicenceElement.clear()
    firstLicenceElement.send_keys(data)
    licencePlateElement.send_keys(simulationData.viaturaMatricula)
    selectVehicleElement.click()

    brandElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(brandXPath))
    modelElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(modelXPath))
    versionElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(versionXPath))
    searchElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(searchXPath))

    time.sleep(1)
    brandElement.send_keys(simulationData.viaturaMarca.upper())

    time.sleep(1)
    select = Select(modelElement)
    for each_option in select.options:
        if simulationData.viaturaModelo.upper() in each_option.text:
            value = each_option.get_attribute("value")
            select.select_by_value(value)
            break

    time.sleep(1)
    select = Select(versionElement)
    for each_option in select.options:
        if simulationData.viaturaVersao.upper() in each_option.text:
            value = each_option.get_attribute("value")
            select.select_by_value(value)
            break

    # Meter um wait para a página esperar pela selecçaõ da versão correta
    # No futuro, meter a aceder à BD e comparar os valores em novo e selecionar a correta
