# Tranquilidade
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import time

def Tranquilidade(driver, user: str, password: str, simulationData, windowHandler: int):
    if windowHandler == 0:
        # Logs in Tranquilidade account
        driver.get(
            'https://portal.tranquilidade.pt/web/spa/login/?p_enc=R3PWru0d4LAxzoY0AYoInQ%3D%3D')
        driver.maximize_window()
        driver.switch_to_window(driver.window_handles[0])
    
    else:
        driver.execute_script(
            "window.open('https://portal.tranquilidade.pt/web/spa/login/?p_enc=R3PWru0d4LAxzoY0AYoInQ%3D%3D');")
        driver.switch_to_window(driver.window_handles[windowHandler])

    # Localizators, ID, Class, Type,...
    userFieldID = 'loginSn'
    passwordFieldID = 'loginPwd'
    submitButtonFieldClass = 'form-signin-submit'

    # Tries to find the elements, has 10 seconds to find each element
    userFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_id(userFieldID))
    passwordFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_id(passwordFieldID))
    submitButtonFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_class_name(submitButtonFieldClass))

    # Fills the elements in homepage
    userFieldElement.send_keys(user)
    passwordFieldElement.send_keys(password)
    submitButtonFieldElement.click()
    
    # Car Simulation
    driver.get('https://pparceiros.tranquilidade.pt/group/cstextra/simulacao/-/simuladores-adhoc-app-simulacao/simulacaoInicio/normal?p_auth=hDGT5BOY&p_enc=TGnudm%2BHNxNzDSKr1iZZOU6andUqqOs6jzIlOzE8EuxaYkMLejGR6iBVou%2Bjo2We')

    # Fills the elements in simulation
    time.sleep(5)
    print('1')
    # Product type
    productFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('beancontratoprodutovalue_0'))
    if simulationData.produto == 'AUT2R - AUTOMÓVEL 2 RODAS':
        select = Select(productFieldElement)        # Dropdown method to select the desired option
        select.select_by_visible_text('AUT2R - AUTOMÓVEL 2 RODAS')
        time.sleep(5)
        print('2')
        if simulationData.viaturaCategoria == 'Velocipede':
            vehicleCategory = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('beancontratotipoVeiculo_0'))
            select = Select(vehicleCategory)
            select.select_by_visible_text('Velocipedes')
    print('3')
    startingDateFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.dataInicioContrato'))
    startingDateFieldElement.click()
    startingDateFieldElement.send_keys(simulationData.dataInicio)
    print('4')
    # Client Type
    if simulationData.tipoCliente == 'Colectivo':
        print('4.1')
        clientTypeFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.codTipoEntidade_1'))
        clientTypeFieldElement.click()
        time.sleep(5)
        print('4.2')
    print('5')
    # Owner info
    driver.execute_script('window.scrollTo(0, 768)')
    clientAddressFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.moradaPrincipal.moradaFormatada'))
    clientAddressFieldElement.send_keys(simulationData.tomadorMorada)
    print('6')
    clientNIFFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.nif'))
    clientNIFFieldElement.send_keys(simulationData.tomadorNIF)
    print('7')
    clientZIPCodeFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.moradaPrincipal.codigoPostal'))
    clientZIPCodeFieldElement.click()
    clientZIPCodeFieldElement.send_keys(simulationData.tomadorCodPostal)
    print('8')
    clientCellphoneFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.telefonePrincipal'))
    clientCellphoneFieldElement.send_keys(simulationData.tomadorTelefone)
    print('9')
    clientEmailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.emailPrincipal'))
    clientEmailFieldElement.send_keys(simulationData.tomadorEmail)
    if simulationData.tomadorBonus == True:
        clientBonusFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.experienciaSeguros.indBonus30_0'))
        clientBonusFieldElement.click()
    print('10')
    if simulationData.tipoCliente == 'Individual':
        clientBirthdateFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.dataNascimento'))
        clientBirthdateFieldElement.click()
        clientBirthdateFieldElement.send_keys(simulationData.tomadorDataNascimento)
        print('11')
        clientLicencedateFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.dtCarta'))
        clientLicencedateFieldElement.click()
        clientLicencedateFieldElement.send_keys(simulationData.tomadorDataCarta)
        print('12')
        if simulationData.tomadorCondutorHabitual == False:
            clientUsualDriverFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorCondutorHabitual_0'))
            clientUsualDriverFieldElement.click()
            print('13')
    else:
        print('14')
        clientCAEFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.descricaoCAE'))
        clientCAEFieldElement.send_keys(simulationData.tomadorCAE)  
        print('15')
    # 1st Ensurance
    driver.execute_script('window.scrollTo(0, 768)') 
    if simulationData.tomadorPrimeiroSeguro == True:
        print('16')
        firstEnsuranceFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.experienciaSeguros.indPrimeiroSeguro_0'))
        firstEnsuranceFieldElement.click()
        print('17')
    else:
        print('18')
        firstEnsuranceDateFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.experienciaSeguros.dtInicioPrimeiroContrato'))
        firstEnsuranceDateFieldElement.send_keys(simulationData.primeiroSeguro)
        print('19')
        if simulationData.numeroAcidentes == 'Zero':
            print('20')
            numberAccidentsFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.experienciaSeguros.sinistrosMenosDoisAnos_0'))
            numberAccidentsFieldElement.click()
            print('21')
        else:
            if simulationData.numeroAcidentes == 'Um':
                print('22')
                numberAccidentsFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.experienciaSeguros.sinistrosMenosDoisAnos_1'))
                numberAccidentsFieldElement.click()
                print('23') 
            else:
                print('24')
                numberAccidentsFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.experienciaSeguros.sinistrosMenosDoisAnos_2'))
                numberAccidentsFieldElement.click()
                print('25')
            print('26')    
            lastAccidentDateFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.tomadorSeguro.experienciaSeguros.dtUltimoSinistro'))
            lastAccidentDateFieldElement.send_keys(simulationData.ultimoAcidente)
            print('27')
    # Driver
    driver.execute_script('window.scrollTo(0, 768)') 
    if simulationData.tipoCliente == 'Individual' and simulationData.tomadorCondutorHabitual == False:
        print('28')
        driverBirthDateFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.condutorHabitual.dtNascimento'))
        driverBirthDateFieldElement.click()
        driverBirthDateFieldElement.send_keys(simulationData.condutorDataNascimento)
        print('29')
        driverZIPCodeFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.condutorHabitual.codPostal'))
        driverZIPCodeFieldElement.click()
        driverZIPCodeFieldElement.send_keys(simulationData.condutorCodPostal)
        print('30')
        driverLicenceFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.condutorHabitual.dtCarta'))
        driverLicenceFieldElement.click()
        driverLicenceFieldElement.send_keys(simulationData.condutorDataCarta)
        print('31')
    # Vehicle
    print('32')
    driver.execute_script('window.scrollTo(0, 768)') 
    vehicleCategoryFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.codCategoria'))
    select = Select(vehicleCategoryFieldElement)
    select.select_by_visible_text(simulationData.viaturaCategoria)
    print('33')
    vehicleNatureFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.codNatureza'))
    select = Select(vehicleNatureFieldElement)
    select.select_by_visible_text(simulationData.viaturaNatureza)
    print('34')
    if simulationData.viaturaNovaMatricula == False:
        print('35')
        vehicleNewLicenceFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.indicadoresUN18.indNovaMatricula_1'))
        vehicleNewLicenceFieldElement.click()
        print('36')
        vehicleLicenceTypeFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.dadosMatricula.codTipoMatricula'))
        select = Select(vehicleLicenceTypeFieldElement)
        select.select_by_visible_text(simulationData.viaturaTipoMatricula)
        print('37')
        vehicleLicenceFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('matriculaNacionalVeiculo'))
        vehicleLicenceFieldElement.send_keys(simulationData.viaturaMatricula)
        print('38')
        vehicleLicenceDateFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.dadosMatricula.dtMatricula'))
        vehicleLicenceDateFieldElement.send_keys(simulationData.viaturaDataMatricula)
        print('39')
    print('40')
    vehicleBrandFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.dadosVeiculo.marca'))
    select = Select(vehicleBrandFieldElement)
    select.select_by_visible_text(simulationData.viaturaMarca)
    print('41')
    vehicleModelFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.dadosVeiculo.modelo'))
    select = Select(vehicleModelFieldElement)
    select.select_by_visible_text(simulationData.viaturaModelo)
    print('42')
    vehicleVersionFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('bean.contrato.veiculo.dadosVeiculo.versao'))
    select = Select(vehicleVersionFieldElement)
    select.select_by_visible_text(simulationData.viaturaVersao)
    print('43')
    submitFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('idSimulacaoValidar'))
    submitFieldElement.click()
    print('44')