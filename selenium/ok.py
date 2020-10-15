# OK
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import time

# def OK(driver, simulationData, windowHandler: int):


def OK(driver, simulationData, windowHandler: int):
    driver.execute_script(
        "window.open('https://www.okteleseguros.pt/simulador/auto/');")
    driver.switch_to_window(driver.window_handles[windowHandler])


    cookiesFieldXPath = '/html/body/div[2]/div[2]/div[2]/a'

    cookiesElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(cookiesFieldXPath))
    cookiesElement.click()


    # Client type
    clientProfessionalXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/span/input'

    if simulationData.tipoCliente == 'Colectivo':
        clientProfessionalElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(clientProfessionalXPath))
        clientProfessionalElement.click()

    # Vehicle
    licencePlateXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[3]/input[1]'
    noLincencePlateXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[3]/div[4]/input'
    vehicleCategoryXpath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/select'
    vehicleYearXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div/select'
    vehicleMonthXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div/select'
    vehicleBrandXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[4]/div[3]/div[2]/select'
    vehicleModelXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[4]/div[4]/div[2]/select'
    print('aqui')
    if simulationData.viaturaMatricula != '':
        licencePlateElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(licencePlateXPath))

    else:
        print('aqui')
        noLincencePlateElent = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(noLincencePlateXPath))
        noLincencePlateElent.click()

        vehicleCategoryElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(vehicleCategoryXpath))
        select = Select(vehicleCategoryElement)
        if simulationData.viaturaCategoria == 'Ligeiro Passageiros/Aluguer':
            vehicleCategory = 'Ligeiro Passageiros'
        elif simulationData.viaturaCategoria == 'Ligeiro Mercadorias':
            vehicleCategory = 'Ligeiro Comercial'
        elif simulationData.viaturaCategoria == 'Motociclo':
            vehicleCategory = 'Motociclo'
        else:
            print('Não existe')
        select.select_by_visible_text(vehicleCategory)
        print('aqui')
        vehicleYear = simulationData.viaturaDataMatricula[len(
            simulationData.viaturaDataMatricula)-4:]
        print(vehicleYear)
        vehicleYearElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(vehicleYearXPath))
        select = Select(vehicleYearElement)
        select.select_by_visible_text(vehicleYear)

        vehicleMonth = simulationData.viaturaDataMatricula[len(
            simulationData.viaturaDataMatricula)-7:len(simulationData.viaturaDataMatricula)-5]
        print(vehicleMonth)
        vehicleMonthElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(vehicleMonthXPath))
        select = Select(vehicleMonthElement)

        if int(vehicleMonth) == 1:
            select.select_by_visible_text('Janeiro')
        elif int(vehicleMonth) == 2:
            select.select_by_visible_text('Fevereiro')
        elif int(vehicleMonth) == 3:
            select.select_by_visible_text('Março')
        elif int(vehicleMonth) == 4:
            select.select_by_visible_text('Abril')
        elif int(vehicleMonth) == 5:
            select.select_by_visible_text('Maio')
        elif int(vehicleMonth) == 6:
            select.select_by_visible_text('Junho')
        elif int(vehicleMonth) == 7:
            select.select_by_visible_text('Julho')
        elif int(vehicleMonth) == 8:
            select.select_by_visible_text('Agosto')
        elif int(vehicleMonth) == 9:
            select.select_by_visible_text('Setembro')
        elif int(vehicleMonth) == 10:
            select.select_by_visible_text('Outubro')
        elif int(vehicleMonth) == 11:
            select.select_by_visible_text('Novembro')
        else:
            select.select_by_visible_text('Dezembro')
        time.sleep(1)

        vehicleBrandElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(vehicleBrandXPath))
        select = Select()
        select.select_by_visible_text(simulationData.viaturaMarca)
        time.sleep(1)
    

    vehicleModelElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(vehicleModelXPath))
    select = Select(simulationData)
    select.select_by_visible_text(simulationData.viaturaModelo)
    time.sleep(1)

    vehicleVersionXPath = '//*[text()="' + simulationData.viaturaVersao +'"]'
    vehicleVersionElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath())
    vehicleVersionElement.click()
    time.sleep(1)

    vehicleImportedXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[2]/div[1]/span/input'
    vehicleNotImportedXPath = '/html/body/div[6]/div[4]/form[1]/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[2]/div[2]/span/input'
    submitXPath = '/html/body/div[6]/div[5]/button[2]'

    if simulationData.viaturaTipoMatricula == 'Importado':
        vehicleImportedElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(vehicleImportedXPath))
    else:
        vehicleNotImportedElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(vehicleNotImportedXPath))
        vehicleNotImportedElement.click()
    submitElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(submitXPath))
    submitElement.click()

    time.sleep(1)
    # Owner
    ownerNIFXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[1]/input'
    ownerNameXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[2]/input'
    ownerEmailXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[3]/input'
    ownerContactXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[4]/input'
    ownerAgeXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[5]/input'
    ownerMaleXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[6]/div[2]/div[2]/span/input'
    ownerFemaleXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[6]/div[2]/div[1]/span/input'
    ownerLicenceXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[7]/input'
    ownerZipcodeXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[8]/input[1]'
    ownerWorkXPath = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[9]/div[2]/select'
    firstEnsurance = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[10]/div[3]/div[2]/div[1]/span/input'
    notFirstEnsurance = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[10]/div[3]/div[2]/div[2]/span/input'
    yearsWithEnsurance = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[10]/div[4]/div[2]/select'
    firstAccident = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[10]/div[5]/input[1]'
    secondAccident = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[10]/div[5]/input[2]'
    thirdAccident = '/html/body/div[6]/div[4]/form[1]/div[2]/div[1]/div[2]/div[10]/div[5]/input[3]'

    ownerNIFElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ownerNIFXPath))
    ownerNIFElement.click()
    ownerNIFElement.send_keys(simulationData.tomadorNIF)
    
    ownerEmailElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ownerEmailXPath))
    ownerEmailElement.click()
    ownerEmailElement.send_keys(simulationData.tomadorEmail)

    ownerContactElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ownerContactXPath))
    ownerContactElement.click()
    ownerContactElement.send_keys(simulationData.tomadorTelefone)

    ownerAgeElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ownerAgeXPath))
    currentYear = simulationData.dataInicio[len(simulationData.dataInicio)-4:]
    birthYear = simulationData.tomadorDataNascimento[len(simulationData.tomadorDataNascimento)-4:]
    ownerAge = int(currentYear) - int(birthYear)
    ownerAgeElement.click()
    ownerAgeElement.send_keys(ownerAge)

    ownerLicenceElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ownerLicenceXPath))
    ownerLicenceElement.click()
    ownerLicenceElement.send_keys(simulationData.tomadorDataCarta[len(simulationData.tomadorDataCarta)-3:])

    ownerZipcodeElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(ownerZipcodeXPath))
    ownerZipcodeElement.click()
    ownerZipcodeElement.send_keys(simulationData.tomadorCodPostal)

class SimulationData:
    def __init__(self, produto, dataInicio, tipoCliente, tomadorMorada, tomadorCodPostal, tomadorTelefone, tomadorNIF, tomadorEmail, tomadorBonus, tomadorDataNascimento, tomadorDataCarta, tomadorCondutorHabitual, tomadorCAE, tomadorPrimeiroSeguro, primeiroSeguro, numeroAcidentes, ultimoAcidente, condutorDataNascimento, condutorDataCarta, condutorCodPostal, viaturaCategoria, viaturaNatureza, viaturaNovaMatricula, viaturaTipoMatricula, viaturaMatricula, viaturaDataMatricula, viaturaMarca, viaturaModelo, viaturaVersao):
        self.produto = produto
        self.dataInicio = dataInicio
        self.tipoCliente = tipoCliente
        self.tomadorMorada = tomadorMorada
        self.tomadorCodPostal = tomadorCodPostal
        self.tomadorTelefone = tomadorTelefone
        self.tomadorNIF = tomadorNIF
        self.tomadorEmail = tomadorEmail
        self.tomadorBonus = tomadorBonus
        self.tomadorDataNascimento = tomadorDataNascimento
        self.tomadorDataCarta = tomadorDataCarta
        self.tomadorCondutorHabitual = tomadorCondutorHabitual
        self.tomadorCAE = tomadorCAE
        self.tomadorPrimeiroSeguro = tomadorPrimeiroSeguro
        self.primeiroSeguro = primeiroSeguro
        self.numeroAcidentes = numeroAcidentes
        self.ultimoAcidente = ultimoAcidente
        self.condutorDataNascimento = condutorDataNascimento
        self.condutorDataCarta = condutorDataCarta
        self.condutorCodPostal = condutorCodPostal
        self.viaturaCategoria = viaturaCategoria
        self.viaturaNatureza = viaturaNatureza
        self.viaturaNovaMatricula = viaturaNovaMatricula
        self.viaturaTipoMatricula = viaturaTipoMatricula
        self.viaturaMatricula = viaturaMatricula
        self.viaturaDataMatricula = viaturaDataMatricula
        self.viaturaMarca = viaturaMarca
        self.viaturaModelo = viaturaModelo
        self.viaturaVersao = viaturaVersao

