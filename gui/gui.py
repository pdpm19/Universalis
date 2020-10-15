# GUI
# Standard Imports
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# My Imports
from loginDlg import LoginDialog
from editDlg import EditDialog, RemoveDialog, AddDialog
from commands_db import Query, Search
from automatization import Automatization
from crypto import DecryptFile, KeyGenerator

# Global Variables
uiPath = ''
accessPath = ''
dbPath = ''
seleniumPath = ''
paths = ''
password = ''

# Simulation values
class SimulationData:
    def __init__(self, produto, dataInicio, tipoCliente, tomadorNome,tomadorMorada, tomadorCodPostal, tomadorTelefone, tomadorNIF, tomadorEmail, tomadorBonus, tomadorDataNascimento, tomadorDataCarta, tomadorCondutorHabitual, tomadorCAE, tomadorPrimeiroSeguro, primeiroSeguro, numeroAcidentes, ultimoAcidente, condutorDataNascimento, condutorDataCarta, condutorCodPostal, viaturaCategoria, viaturaNatureza, viaturaNovaMatricula, viaturaTipoMatricula, viaturaMatricula, viaturaDataMatricula, viaturaMarca, viaturaModelo, viaturaVersao):
        self.produto = produto
        self.dataInicio = dataInicio
        self.tipoCliente = tipoCliente
        self.tomadorNome = tomadorNome
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

# Makes input into Table Mode View
class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

# Threads the Automatization part
class ThreadAutomatization(QRunnable):
    def __init__(self, data, paths, password):
        super(ThreadAutomatization, self).__init__()
        self.data = data
        self.paths = paths
        self.password = password
    
    @pyqtSlot()    
    def run(self):
        Automatization(self.paths, self.password, self.data)

# GUI 
class GUI(QMainWindow):
    def __init__(self, width, heigth, windowTitle):
        super(GUI, self).__init__()
        self.setGeometry(800, 600, width, heigth)
        iconPath = os.path.join(uiPath, 'images', 'Universalis-RM-icon.png')
        self.setWindowIcon(QIcon(iconPath))  # Insere o icon
        self.setWindowTitle(windowTitle)
        self.threadpool = QThreadPool()

        # Headline font
        self.headline = QFont("Arial", 14, QFont.Bold)

        # Main stacked (Homepage-Vehicle-Health)
        self.stacked = QStackedWidget()
        
        # Scrollable
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.stacked)
        
        
        self.homepageWidgets = QWidget()
        self.homepageLayout = QVBoxLayout()
        self.HomepageUI()

        self.vehicleWidgets = QWidget()
        self.vehicleLayout = QVBoxLayout()
        self.VehicleUI()

        self.healthWidgets = QWidget()
        self.healthLayout = QVBoxLayout()
        self.HealthUI()

        self.settingsStacked = QStackedWidget()
        self.SettingsUI()
        
        self.stacked.addWidget(self.homepageWidgets)
        self.stacked.addWidget(self.vehicleWidgets)
        self.stacked.addWidget(self.healthWidgets)
        self.stacked.addWidget(self.settingsStacked)
        self.setCentralWidget(self.scroll)
        
    # Homepage
    def HomepageUI(self):
        # Insere o logo
        logo = QLabel()
        logoPath = os.path.join(uiPath, 'images', 'Universalis-RM-small.png')
        pixmap = QPixmap(logoPath)  
        logo.resize(200, 200)
        logo.setPixmap(pixmap)
        self.homepageLayout.addWidget(logo)

        # Buttons
        homepageBtnGrid = QWidget()
        homepageBtnGridLayout = QGridLayout()

        homepageVehicleBtn = QPushButton('Viatura')
        homepageVehicleBtn.pressed.connect(self.VehicleConnect)
        
        homepageHealthBtn = QPushButton('Vida')
        homepageHealthBtn.pressed.connect(self.HealthConnect)

        homepageSettingsBtn = QPushButton()
        settigsPath = os.path.join(uiPath, 'images', 'settings.png')
        homepageSettingsBtn.setIcon(QIcon(settigsPath))
        homepageSettingsBtn.pressed.connect(self.SettingsConnect)
        
        homepageBtnGridLayout.addWidget(homepageVehicleBtn, 0,0)
        homepageBtnGridLayout.addWidget(homepageHealthBtn, 0,1)
        homepageBtnGridLayout.addWidget(homepageSettingsBtn, 1,1)
        homepageBtnGrid.setLayout(homepageBtnGridLayout)
        self.homepageLayout.addWidget(homepageBtnGrid)

        self.homepageWidgets.setLayout(self.homepageLayout)
        self.homepageLayout.setAlignment(logo, Qt.AlignCenter)   

    def VehicleConnect(self):
        self.stacked.setCurrentIndex(1)

    def HealthConnect(self):
        self.stacked.setCurrentIndex(2)

    def SettingsConnect(self):
        self.stacked.setCurrentIndex(3)
    
    # Vehicle
    def VehicleUI(self):
        ## Ensurance
        ensurance = QWidget()
        ensuranceLayout = QGridLayout()
        
        ## Owner
        owner = QWidget()
        ownerLayout = QGridLayout()
        ownerColumn1 = QWidget()
        ownerColumn1Layout = QFormLayout()
        self.ownerColumn2 = QStackedWidget()
        onwerIndividual = QWidget()
        onwerIndividualLayout = QFormLayout()
        onwerColective = QWidget()
        onwerColectiveLayout = QFormLayout()

        ## First Ensurance
        firstEnsuranceQuestion = QWidget()
        firstEnsuranceQuestionLayout = QGridLayout()
        self.firstEnsurance = QWidget()
        firstEnsuranceLayout = QGridLayout()

        ## Driver
        self.driver = QWidget()
        driverLayout = QGridLayout()
        driverColumn1 = QWidget()
        driverColumn1Layout = QFormLayout()
        driverColumn2 = QWidget()
        driverColumn2Layout = QFormLayout()

        ## Vehicle
        vehicle = QWidget()
        vehicleLayout = QGridLayout()

        ## Buttons
        buttons = QWidget()
        buttonsLayout = QHBoxLayout()
        
        ensuranceHeader = QLabel('Dados Seguro')
        ensuranceHeader.setFont(self.headline)
        ensuranceHeader.setMaximumWidth(180)
        ensuranceLayout.addWidget(ensuranceHeader, 0,0)
        
        ensuranceLayout.addWidget(QLabel('Produto'), 1,0)
        self.ensuranceProductField = QComboBox()
        self.ensuranceProductField.addItems(self.QueryProducts())
        self.ensuranceProductField.currentIndexChanged.connect(self.QueryCategories)
        ensuranceLayout.addWidget(self.ensuranceProductField, 1,1)

        ensuranceLayout.addWidget(QLabel('Data Início Seguro:'), 1,2)
        self.ensuranceStartingDateField = QDateEdit()
        self.ensuranceStartingDateField.setCalendarPopup(True)
        self.ensuranceStartingDateField.setDisplayFormat("dd/MM/yyyy")
        self.ensuranceStartingDateField.setDateTime(QDateTime.currentDateTime())
        self.ensuranceStartingDateField.setMinimumDateTime(QDateTime.currentDateTime())
        ensuranceLayout.addWidget(self.ensuranceStartingDateField, 1,3)

        ensuranceLayout.addWidget(QLabel('Tipo de Cliente:'), 2,0)
        self.ensuranceIndividualClientField = QRadioButton('Individual')
        self.ensuranceIndividualClientField.setChecked(True)
        self.ensuranceIndividualClientField.toggled.connect(self.HideDriver)
        self.ensuranceColectiveClientField = QRadioButton('Colectivo') 
        self.ensuranceColectiveClientField.toggled.connect(self.HideDriver)
        self.ensuranceColectiveClientField.toggled.connect(lambda: self.driver.hide)
        ensuranceLayout.addWidget(self.ensuranceIndividualClientField, 2,1)
        ensuranceLayout.addWidget(self.ensuranceColectiveClientField, 2,2)
        
        ensurance.setLayout(ensuranceLayout)
        
        ### Global owner
        ownerHeader = QLabel('Dados Tomador')
        ownerHeader.setMaximumWidth(180)
        ownerHeader.setFont(self.headline)
        ownerLayout.addWidget(ownerHeader, 0,0)
        ownerLayout.addWidget(ownerColumn1, 1,0)
        ownerLayout.addWidget(self.ownerColumn2, 1,1)
        
        self.ownerNameField = QLineEdit()
        ownerColumn1Layout.addRow(QLabel('Nome:'), self.ownerNameField)
        
        self.ownerAdrressField = QLineEdit()
        ownerColumn1Layout.addRow(QLabel('Morada:'), self.ownerAdrressField)
        
        self.ownerZIPCodeField = QLineEdit()
        ownerColumn1Layout.addRow(QLabel('Código Postal:'), self.ownerZIPCodeField)

        self.ownerCellphoneField = QLineEdit()
        ownerColumn1Layout.addRow(QLabel('Telefone:'), self.ownerCellphoneField)

        self.ownerNIFField = QLineEdit()
        ownerColumn1Layout.addRow(QLabel('NIF:'), self.ownerNIFField)

        self.ownerEmailField = QLineEdit()
        ownerColumn1Layout.addRow(QLabel('Email:'), self.ownerEmailField)

        self.ownerBonus = QCheckBox()
        ownerColumn1Layout.addRow(QLabel('Bónus:'), self.ownerBonus)

        ### Stacked
        self.ownerBirthdateField = QDateEdit()
        self.ownerBirthdateField.setCalendarPopup(True)
        self.ownerBirthdateField.setDisplayFormat("dd/MM/yyyy")
        onwerIndividualLayout.addRow(QLabel('Data de Nascimento:'), self.ownerBirthdateField)
        
        self.ownerLicenceField = QDateEdit()
        self.ownerLicenceField.setCalendarPopup(True)
        self.ownerLicenceField.setDisplayFormat("dd/MM/yyyy")
        onwerIndividualLayout.addRow(QLabel('Data Carta:'), self.ownerLicenceField)

        self.ownerDriverField = QCheckBox()
        self.ownerDriverField.stateChanged.connect(self.HideDriver)
        onwerIndividualLayout.addRow(QLabel('Tomador é condutor habitual:'), self.ownerDriverField)
        
        self.ownerCAEField = QLineEdit()
        onwerColectiveLayout.addRow(QLabel('CAE:'), self.ownerCAEField)

        onwerIndividual.setLayout(onwerIndividualLayout)
        onwerColective.setLayout(onwerColectiveLayout)
        self.ownerColumn2.addWidget(onwerIndividual)
        self.ownerColumn2.addWidget(onwerColective)
        ownerColumn1.setLayout(ownerColumn1Layout)

        owner.setLayout(ownerLayout)

        ## First Ensurance
        self.firstEnsuranceYesField = QRadioButton('Sim')
        self.firstEnsuranceNoField = QRadioButton('Não')
        self.firstEnsuranceYesField.toggled.connect(self.HideFirstEnsurance)
        firstEnsuranceQuestionLayout.addWidget(QLabel('1º Seguro Automóvel:'), 0,0)
        firstEnsuranceQuestionLayout.addWidget(self.firstEnsuranceYesField, 0,1)
        firstEnsuranceQuestionLayout.addWidget(self.firstEnsuranceNoField, 1,1)
        firstEnsuranceQuestion.setLayout(firstEnsuranceQuestionLayout)
        
        self.firstEnsuranceDateField = QDateEdit()
        self.firstEnsuranceDateField.setCalendarPopup(True)
        self.firstEnsuranceDateField.setDisplayFormat("dd/MM/yyyy")
        firstEnsuranceLayout.addWidget(QLabel('Seguro Desde:'), 0,0)
        firstEnsuranceLayout.addWidget(self.firstEnsuranceDateField, 0,1)

        self.firstEnsuranceDateAccidentField = QDateEdit()
        self.firstEnsuranceDateAccidentField.setCalendarPopup(True)
        self.firstEnsuranceDateAccidentField.setDisplayFormat("dd/MM/yyyy")
        firstEnsuranceLayout.addWidget(QLabel('Data Último Sinistro:'), 1,0)
        firstEnsuranceLayout.addWidget(self.firstEnsuranceDateAccidentField, 1,1)

        self.firstEnsuranceNumberAccidentField = QComboBox()
        self.firstEnsuranceNumberAccidentField.addItems(['Zero', 'Um', 'Dois'])
        firstEnsuranceLayout.addWidget(QLabel('Nº Sinistros nos Últimos 2 anos:'), 0,3)
        firstEnsuranceLayout.addWidget(self.firstEnsuranceNumberAccidentField, 0,4)
    
        self.firstEnsurance.setLayout(firstEnsuranceLayout)
        
        ## Driver
        driverHeader = QLabel('Dados Condutor')
        driverHeader.setFont(self.headline)
        driverHeader.setMaximumWidth(180)
        driverLayout.addWidget(driverHeader, 0,0)

        self.driverBirthDateField = QDateEdit()
        self.driverBirthDateField.setCalendarPopup(True)
        self.driverBirthDateField.setDisplayFormat("dd/MM/yyyy")
        driverColumn1Layout.addRow(QLabel('Data Nascimento:'), self.driverBirthDateField)

        self.driverLicenceField = QDateEdit()
        self.driverLicenceField.setCalendarPopup(True)
        self.driverLicenceField.setDisplayFormat("dd/MM/yyyy")
        driverColumn1Layout.addRow(QLabel('Data Carta:'), self.driverLicenceField)
        driverColumn1.setLayout(driverColumn1Layout)

        self.driverZIPCodeField = QLineEdit()
        driverColumn2Layout.addRow(QLabel('Código Postal:'), self.driverZIPCodeField)
        driverColumn2.setLayout(driverColumn2Layout)
        driverLayout.addWidget(driverColumn1, 1,0)
        driverLayout.addWidget(driverColumn2, 1,1)
        self.driver.setLayout(driverLayout)        

        ## vehicle
        vehicleHeader = QLabel('Dados Viatura')
        vehicleHeader.setFont(self.headline)
        vehicleHeader.setMaximumWidth(180)
        vehicleLayout.addWidget(vehicleHeader, 0,0)

        vehicleLayout.addWidget(QLabel('Categoria:'), 1,0)
        self.vehicleCategoryField = QComboBox()
        self.vehicleCategoryField.setFixedWidth(250)
        self.vehicleCategoryField.currentIndexChanged.connect(self.QueryBrands)
        vehicleLayout.addWidget(self.vehicleCategoryField, 1,1)
        
        vehicleLayout.addWidget(QLabel('Natureza:'), 1,3)
        self.vehicleNatureField = QComboBox()
        self.vehicleNatureField.addItems(['Aluguer', 'Outro'])
        vehicleLayout.addWidget(self.vehicleNatureField, 1,4)
        
        vehicleLayout.addWidget(QLabel('Matricula Nova:'), 2,0)
        self.vehicleNewLicenceField = QRadioButton('Sim')
        # self.vehicleNewLicenceField.toggled.connect()
        vehicleLayout.addWidget(self.vehicleNewLicenceField, 2,1)
        self.vehicleNoNewLicenceField = QRadioButton('Não')
        vehicleLayout.addWidget(self.vehicleNoNewLicenceField, 2,2)

        vehicleLayout.addWidget(QLabel('Matricula:'), 2,3)
        self.vehicleLicencePlateCategoryField = QComboBox()
        self.vehicleLicencePlateCategoryField.addItems(['Matricula Nacional', 'Importado', 'Matricula Reboque'])
        vehicleLayout.addWidget(self.vehicleLicencePlateCategoryField, 2,4)
        
        self.vehicleLicencePlateField = QLineEdit()
        vehicleLayout.addWidget(self.vehicleLicencePlateField, 2,5)

        vehicleLayout.addWidget(QLabel('Data 1ª Matricula:'), 2,6)
        self.vehicle1stLicencePlateField = QDateEdit()
        self.vehicle1stLicencePlateField.setCalendarPopup(True)
        self.vehicle1stLicencePlateField.setDisplayFormat("dd/MM/yyyy")
        vehicleLayout.addWidget(self.vehicle1stLicencePlateField, 2,7)

        vehicleLayout.addWidget(QLabel('Marca:'), 3,0)
        self.vehicleBrandField = QComboBox()
        self.vehicleBrandField.currentIndexChanged.connect(self.QueryModels)
        vehicleLayout.addWidget(self.vehicleBrandField, 3,1)
        
        vehicleLayout.addWidget(QLabel('Modelo:'), 3,2)
        self.vehicleModelField = QComboBox()
        self.vehicleModelField.currentIndexChanged.connect(self.QueryVersions)
        vehicleLayout.addWidget(self.vehicleModelField, 3,3)

        vehicleLayout.addWidget(QLabel('Versão:'), 3,4)
        self.vehicleVersionField = QComboBox()
        vehicleLayout.addWidget(self.vehicleVersionField, 3,5)       
        
        infoBtn = QPushButton()
        infoPath = os.path.join(uiPath, 'images', 'info.png')
        infoBtn.setIcon(QIcon(infoPath))
        infoBtn.setMaximumSize(QSize(24,24))
        infoBtn.pressed.connect(self.VersionInfo)
        vehicleLayout.addWidget(infoBtn, 3,6)

        vehicle.setLayout(vehicleLayout)
        
        ## Buttons
        backBtn = QPushButton('Voltar')
        backBtn.pressed.connect(self.ClearVehicleSimulation)
        simulationBtn = QPushButton('Simular')
        simulationBtn.pressed.connect(self.VehicleSimulation)

        buttonsLayout.addWidget(backBtn)
        buttonsLayout.addWidget(simulationBtn)

        buttons.setLayout(buttonsLayout)
        
        self.vehicleLayout.addWidget(ensurance)
        self.vehicleLayout.addWidget(owner)
        self.vehicleLayout.addWidget(firstEnsuranceQuestion)
        self.vehicleLayout.addWidget(self.firstEnsurance)
        self.vehicleLayout.addWidget(self.driver)
        self.vehicleLayout.addWidget(vehicle)
        self.vehicleLayout.addWidget(buttons)
        self.vehicleWidgets.setLayout(self.vehicleLayout)
    
    # Queries to DB
    def QueryProducts(self):
        return Query('pro_name', 'Product', [''], '', '', 0)
    
    def QueryCategories(self):
        if(self.ensuranceProductField.currentIndex() != 0):
            self.vehicleCategoryField.clear()
            self.vehicleBrandField.clear()
            self.vehicleModelField.clear()
            self.vehicleVersionField.clear()
            categories = Search(self.ensuranceProductField.currentIndex(), 'product_id')
            self.vehicleCategoryField.addItems(Query('cat_name', 'Category', categories, 'cat_id', 'OR', 0))
    
    def QueryBrands(self):
        if(self.vehicleCategoryField.currentIndex() != 0):
            self.vehicleBrandField.clear()
            self.vehicleModelField.clear()
            self.vehicleVersionField.clear()
            self.categoryID = Query('cat_id', 'Category', ['', self.vehicleCategoryField.currentText()], 'cat_name', '', 0)
            brandsIDFromCategory = Search(self.categoryID[1], 'category_id')
            self.vehicleBrandField.addItems(Query('bra_name', 'Brand', brandsIDFromCategory, 'bra_id', 'OR', 0))

    def QueryModels(self):
        if(self.vehicleBrandField.currentIndex() != 0):
            vehicleModels = ['']
            self.vehicleModelField.clear()
            self.vehicleVersionField.clear()
            self.brandID = Query('bra_id', 'Brand', ['', self.vehicleBrandField.currentText()], 'bra_name', '', 0)
            modelsIDFromBrand = Search(self.brandID[1], 'brand_id')
            modelsIDFromCategory = Query('model_id', 'CatMod', ['', self.categoryID[1]], 'category_id', '', 0)
            for x in modelsIDFromBrand:
                for y in modelsIDFromCategory:
                    if x == y:
                        vehicleModels.append(x)
            self.vehicleModelField.addItems(Query('mod_name', 'Model', vehicleModels, 'mod_id', 'OR', 0))
        
    def QueryVersions(self):
        if(self.vehicleModelField.currentIndex() != 0):
            self.vehicleVersionField.clear()
            modelID = Query('mod_id', 'Model', ['', self.vehicleModelField.currentText()], 'mod_name', '', 0)
            vehicleVersions = Search(modelID[1], 'model_id')
            self.vehicleVersionField.addItems(Query('ver_name', 'Version', vehicleVersions, 'ver_id', 'OR', 0))

    # Gives the whole info about that Version
    def VersionInfo(self):
        if(self.vehicleVersionField.currentIndex() > 0):
            dlg = QDialog()
            dlg.setWindowTitle('Versão')
            dlg.setGeometry(600, 400, 820, 200)
            layout = QVBoxLayout()

            self.table = QTableView()

            data = [['Modelo', 'Combustível', 'Cilindrada', 'Portas', 'Lugares', 'Cavalagem', 'Peso', 'Valor Novo']]
            query = Query('*', 'Version', ['',self.vehicleVersionField.currentText()], 'ver_name', '', 0)
            
            name, fuel, engineSize, doors, seats, horsepower, weigth, price = query[1]

            data.append([name,fuel, engineSize, doors, seats, horsepower, weigth, price])
            
            self.model = TableModel(data)
            self.table.setModel(self.model)
            layout.addWidget(self.table)
            dlg.setLayout(layout)

            dlg.exec_()

    # Hides the First Ensurance
    def HideFirstEnsurance(self):
        if self.firstEnsuranceYesField.isChecked():
            self.firstEnsurance.hide()
        else:
            self.firstEnsurance.show()

    # Hides the Driver
    def HideDriver(self):
        if self.ensuranceIndividualClientField.isChecked():
            self.ownerColumn2.setCurrentIndex(0)
            if self.ownerDriverField.isChecked():
                self.driver.hide()
            else:
                self.driver.show()
        else:
            self.driver.hide()
            self.ownerColumn2.setCurrentIndex(1)

    # Clears all fields 
    def ClearVehicleSimulation(self):
        # Ensurance
        self.ensuranceProductField.setCurrentIndex(0)
        self.ensuranceStartingDateField.setDateTime(QDateTime.currentDateTime())

        # Client
        self.ownerAdrressField.clear()
        self.ownerZIPCodeField.clear()
        self.ownerCellphoneField.clear()
        self.ownerNIFField.clear()
        self.ownerEmailField.clear()
        self.ownerBonus.setChecked(False)
        
        # individual
        # self.ownerBirthdateField.setDateTime(QDateTime)
        # self.ownerLicenceField
        self.ownerDriverField.setChecked(False)
        # Colective
        self.ownerCAEField.clear()

        # self.firstEnsuranceDateField
        self.firstEnsuranceNumberAccidentField.setCurrentIndex(0)
        #self.firstEnsuranceDateAccidentField
        
        # Driver
        # self.driverBirthDateField
        # self.driverLicenceField
        self.driverZIPCodeField.clear()

        # Vehicle
        self.vehicleLicencePlateCategoryField.setCurrentIndex(0)
        self.vehicleNatureField.setCurrentIndex(0)
        self.vehicleLicencePlateField.clear()
        # self.vehicle1stLicencePlateField
        self.vehicleCategoryField.clear()
        self.vehicleBrandField.clear()
        self.vehicleModelField.clear()
        self.vehicleVersionField.clear()

        self.stacked.setCurrentIndex(0)
    
    def DateConvert(self, date):
        d = date.date().day()
        day = ""
        month = ""
        if d < 10:
            day = "0" + str(d)
        else:
            day = str(d)
        m = date.date().month()
        if m < 10:
            month = "0" + str(m)
        else:
            month = str(m)
        year = date.date().year()
        sDate = day + str('/') + month + str('/') + str(year)
        return sDate
    
    # Sends the information
    def VehicleSimulation(self):
        if(self.ensuranceColectiveClientField.isChecked()):
            ensuranceClient = 'Colectivo'
        else:
            ensuranceClient = 'Individual'
        data = SimulationData(self.ensuranceProductField.currentText(), self.DateConvert(self.ensuranceStartingDateField), ensuranceClient, self.ownerNameField.text(),self.ownerAdrressField.text(),  self.ownerZIPCodeField.text(), self.ownerCellphoneField.text(), self.ownerNIFField.text(), self.ownerEmailField.text(), self.ownerBonus.isChecked(), self.DateConvert(self.ownerBirthdateField), self.DateConvert(self.ownerLicenceField), self.ownerDriverField.isChecked(), self.ownerCAEField.text(), self.firstEnsuranceYesField.isChecked(), self.DateConvert(self.firstEnsuranceDateField), self.firstEnsuranceNumberAccidentField.currentText(), self.DateConvert(self.firstEnsuranceDateAccidentField), self.DateConvert(self.driverBirthDateField), self.DateConvert(self.driverLicenceField), self.driverZIPCodeField.text(), self.vehicleCategoryField.currentText(), self.vehicleNatureField.currentText(), self.vehicleNewLicenceField.isChecked(), self.vehicleLicencePlateCategoryField.currentText(), self.vehicleLicencePlateField.text(), self.DateConvert(self.vehicle1stLicencePlateField), self.vehicleBrandField.currentText(), self.vehicleModelField.currentText(), self.vehicleVersionField.currentText())
        thread_auto = ThreadAutomatization(data, paths, password)
        self.threadpool.start(thread_auto)
    
    # Health
    def HealthUI(self):
        ## Ensurance
        ensurance = QWidget()
        ensuranceLayout = QGridLayout()

        ## Protection Plan

        ## People's data

        ## Education

        ## Buttons
        buttons = QWidget()
        buttonsLayout = QHBoxLayout()

        ## Ensurance
        ensuranceHeader = QLabel('Dados Seguro')
        ensuranceHeader.setFont(self.headline)
        ensuranceLayout.addWidget(ensuranceHeader, 0,0)
        
        ensuranceLayout.addWidget(QLabel('Produto:'), 1,0)
        self.ensuranceHealthProductField = QComboBox()
        self.ensuranceHealthProductField.addItems(['','VIDM2 - VIDA MAIS', 'VIDDO - VIDA + VENCER', 'VIDMA - VIDA MAIS', 'VIPRS - VIDA PROFISSIONAIS SAÚDE', 'VISFI - PLANO VIDA SEM FRONTEIRAS IND', 'VTCA3 . VIDA CRÉDITO CASA 3 ATUALIZAÇÃO', 'VTCC3 - VIDA CRÉDITO CASA 3.0'])
        ensuranceLayout.addWidget(self.ensuranceHealthProductField, 1,1)
        
        ensuranceLayout.addWidget(QLabel('Data Início Seguro:'), 1,2)
        self.ensuranceHealthStartingDateField = QDateEdit()
        self.ensuranceHealthStartingDateField.setCalendarPopup(True)
        self.ensuranceHealthStartingDateField.setDateTime(QDateTime.currentDateTime())
        self.ensuranceHealthStartingDateField.setMinimumDateTime(QDateTime.currentDateTime())
        self.ensuranceHealthStartingDateField.setDisplayFormat("dd/MM/yyyy")
        ensuranceLayout.addWidget(self.ensuranceHealthStartingDateField, 1,3)

        ensuranceLayout.addWidget(QLabel('Duração Seguro:'), 2,0)
        self.ensuranceDurationField = QComboBox()
        self.ensuranceDurationField.addItems(['Ano e Seguintes'])
        ensuranceLayout.addWidget(self.ensuranceDurationField, 2,1)

        ensuranceLayout.addWidget(QLabel('Prazo Empréstimo (anos):'), 3,0)
        self.ensuranceLoanYearsField = QSpinBox()
        self.ensuranceLoanYearsField.setMinimum(0)
        self.ensuranceLoanYearsField.setMaximum(99)
        ensuranceLayout.addWidget(self.ensuranceLoanYearsField, 3,1)
        
        ensurance.setLayout(ensuranceLayout)

        ## 
        ## Buttons
        backBtn = QPushButton('Voltar')
        backBtn.pressed.connect(lambda: self.stacked.setCurrentIndex(0))
        buttonsLayout.addWidget(backBtn)

        simulationBtn = QPushButton('Simular')
        # simulationBtn.pressed.connect()
        buttonsLayout.addWidget(simulationBtn)
        buttons.setLayout(buttonsLayout)

        self.healthLayout.addWidget(ensurance)
        self.healthLayout.addWidget(buttons)
        self.healthWidgets.setLayout(self.healthLayout)

    # Settings
    def SettingsUI(self):
        buttons = QWidget()
        buttonsLayout = QVBoxLayout()
        
        settingsWidgets = QWidget()
        settingsLayout = QVBoxLayout()

        '''
        self.table = QTableView()
        data = [['Utilizador', 'Palavra-passe']] 
        users = []
        passwords = []
        values = ''
    
        decrypted = DecryptFile(accessPath + path + 'acessos.csv.enc', KeyGenerator(1, password))
        aux = 0
        userAux = ''
        passwordAux = ''

        for c in decrypted:
            if c == '\n':
                passwords.append(passwordAux)
                passwordAux = ''
                aux = 0
            elif c == ';':
                users.append(userAux)
                userAux = ''
                aux = 1
            elif aux == 0 and c != ';':
                userAux = userAux + c
            else:
                passwordAux = passwordAux + c
        for i in range(len(users)):
            data.append([users[i], passwords[i]])
        
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.settingsLayout.addWidget(self.table)
        '''

        self.dbWidget = QWidget()
        self.DBManagerUI()
        
        
        dbBtn = QPushButton('Gerir Base de Dados')
        dbBtn.pressed.connect(lambda: self.settingsStacked.setCurrentIndex(1))
        buttonsLayout.addWidget(dbBtn)


        self.accessWidget = QWidget()
        self.AccessManagerUI()

        accessBtn = QPushButton('Gerir Acessos')
        accessBtn.pressed.connect(lambda: self.settingsStacked.setCurrentIndex(10))
        buttonsLayout.addWidget(accessBtn)

        backBtn = QPushButton('Voltar')
        backBtn.pressed.connect(lambda: self.stacked.setCurrentIndex(0))
        buttonsLayout.addWidget(backBtn)

        buttons.setLayout(buttonsLayout)
        
        settingsLayout.addWidget(buttons)
        settingsWidgets.setLayout(settingsLayout)
        self.settingsStacked.addWidget(settingsWidgets)
        self.settingsStacked.addWidget(self.dbWidget)

    # DB functions
    def DBManagerUI(self):
        layout = QVBoxLayout()
        
        menuWidget = QWidget()
        menuLayout = QVBoxLayout()
        
        addEntry = QPushButton('Adicionar entrada')
        addEntry.pressed.connect(self.AddEntryDlg)
        
        editEntry = QPushButton('Editar entrada')
        editEntry.pressed.connect(self.EditEntryDlg)
        
        removeEntry = QPushButton('Remover entrada')
        removeEntry.pressed.connect(self.RemoveEntryDlg)
        
        backBtn = QPushButton('Voltar')
        backBtn.pressed.connect(lambda: self.settingsStacked.setCurrentIndex(0))
        
        menuLayout.addWidget(addEntry)
        menuLayout.addWidget(editEntry)
        menuLayout.addWidget(removeEntry)
        menuLayout.addWidget(backBtn)
        menuWidget.setLayout(menuLayout)

        layout.addWidget(menuWidget)
        self.dbWidget.setLayout(layout)
    
    # Calls the dialog
    def EditEntryDlg(self):
        EditDialog(dbPath, path, uiPath + path + 'images' + path + 'Universalis-RM-icon.png', 'Editar')
    def RemoveEntryDlg(self):
        RemoveDialog(dbPath, path, uiPath + path + 'images' + path + 'Universalis-RM-icon.png', 'Remover')
    def AddEntryDlg(self):
        AddDialog(dbPath, path, uiPath + path + 'images' + path + 'Universalis-RM-icon.png', 'Adicionar')
    def AccessManagerUI(self):
        print('ola')
# Calls the GUI
def GUILoad(args):
    global uiPath, accessPath, dbPath, paths, seleniumPath, password
    paths = args
    uiPath = args[0]
    accessPath = args[1]
    dbPath = args[2]
    seleniumPath = args[3]
    app = QApplication([])

    # Login Password Dialog
    login = LoginDialog(paths)
    if login.exec_():
        password = login.Login()
        # Accepts the login
        window = GUI(800, 600, 'Simulador')
        window.show()
    sys.exit(app.exec_())
