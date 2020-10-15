# Standard imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# My imports
from commands_db import Query, Search, Edit, Delete, Add

class CreateDialog(QDialog):
    def __init__(self, dbPath, path, iconPath, mode):
        dbPath = os.path.join(dbPath, 'project.db')
        super(CreateDialog, self).__init__()
        self.setWindowTitle(mode)
        self.setGeometry(600, 400, 300, 200)
        self.mode = mode
        self.setWindowIcon(QIcon(iconPath))
        self.layout = QVBoxLayout()

        # 1st table
        self.optionDropdown = QComboBox()
        self.optionDropdown.addItems(
            ['','Categoria', 'Marca', 'Modelo', 'Versão'])
        self.optionDropdown.currentIndexChanged.connect(self.Queries)

        # Display/Edit values Layout
        self.displayStacked = QStackedWidget()
        
        # Values to be displayed
        self.displayName = QLineEdit()
        self.displayNameModels = QLineEdit()
        self.displayNameVersion = QLineEdit()
        self.displayFactoryName = QLineEdit()
        self.displayStartYear = QLineEdit()
        self.displayFinishYear = QLineEdit()
        self.displayFuel = QLineEdit()
        self.displayEngineSize = QLineEdit()
        self.displayDoors = QLineEdit()
        self.displaySeats = QLineEdit()
        self.displayHorsepower = QLineEdit()
        self.displayWeigth = QLineEdit()
        self.displayPrice = QLineEdit()
        
        # Views
        view0 = QWidget()
        self.view0Layout = QFormLayout()

        view1 = QWidget()
        self.view1Layout = QFormLayout()

        view2 = QWidget()
        view2Column1 = QWidget()
        view2Column2 = QWidget()
        self.view2Layout = QHBoxLayout()
        displayColumn1 = QFormLayout()
        displayColumn2 = QFormLayout()

        # Creation of views
        ## View0
        self.view0Layout.addRow(QLabel('Nome: '), self.displayName)
        view0.setLayout(self.view0Layout)
        self.displayStacked.addWidget(view0)

        ## View 1
        self.view1Layout.addRow(QLabel('Nome:'), self.displayNameModels)
        self.view1Layout.addRow(QLabel('Nome de Fábrica:'), self.displayFactoryName)
        self.view1Layout.addRow(QLabel('Início de fabrico:'), self.displayStartYear)
        self.view1Layout.addRow(QLabel('Término de fabrico:'), self.displayFinishYear)
        view1.setLayout(self.view1Layout)
        self.displayStacked.addWidget(view1)
        
        ## View 2
        displayColumn1.addRow(QLabel('Nome: '), self.displayNameVersion)
        displayColumn1.addRow(QLabel('Combustível: '), self.displayFuel)
        displayColumn1.addRow(QLabel('Cilindrada: '), self.displayEngineSize)
        displayColumn1.addRow(QLabel('Portas: '), self.displayDoors)
        displayColumn2.addRow(QLabel('Lugares: '), self.displaySeats)
        displayColumn2.addRow(QLabel('Cavalagem: '), self.displayHorsepower)
        displayColumn2.addRow(QLabel('Peso: '), self.displayWeigth)
        displayColumn2.addRow(QLabel('Preço: '), self.displayPrice)
        view2Column1.setLayout(displayColumn1)
        view2Column2.setLayout(displayColumn2)
        self.view2Layout.addWidget(view2Column1)
        self.view2Layout.addWidget(view2Column2)
        view2.setLayout(self.view2Layout)
        self.displayStacked.addWidget(view2)

        # Foward button
        self.functionBtn = QPushButton(self.mode)
        self.functionBtn.pressed.connect(self.Operation)

        self.setLayout(self.layout)

    def AddDlg(self):
        self.option = QComboBox()
        self.option.addItems(
            ['Categoria', 'Marca', 'Modelo', 'Versão'])
        self.option.currentIndexChanged.connect(self.Add)
        
        self.layout.addWidget(self.option)
        self.layout.addWidget(self.displayStacked)
        self.layout.addWidget(self.functionBtn)
    
    def EditDlg(self):
        # Lists
        self.queryDropdown = QComboBox()
        self.queryDropdown.currentIndexChanged.connect(self.Display)
        
        self.layout.addWidget(self.optionDropdown)
        self.layout.addWidget(self.queryDropdown)
        self.layout.addWidget(self.displayStacked)
        self.layout.addWidget(self.functionBtn)
    
    def RemoveDlg(self):
        # Lists
        self.queryDropdown = QComboBox()
        self.queryDropdown.currentIndexChanged.connect(self.Display)
        
        self.layout.addWidget(self.optionDropdown)
        self.layout.addWidget(self.queryDropdown)
        self.layout.addWidget(self.functionBtn)

    def Queries(self):
        self.queryDropdown.clear()
        aux = []
        if self.optionDropdown.currentText() == 'Categoria':
            self.displayStacked.setCurrentIndex(0)
            aux = Query('cat_name', 'Category', [''], '', '', 1)
        elif self.optionDropdown.currentText() == 'Marca':
            self.displayStacked.setCurrentIndex(0)
            aux = Query('bra_name', 'Brand', [''], '', '', 1)
        elif self.optionDropdown.currentText() == 'Modelo':
            self.displayStacked.setCurrentIndex(1)
            aux = Query('mod_name', 'Model', [''], '', '', 1)
        elif self.optionDropdown.currentText() == 'Versão':
            self.displayStacked.setCurrentIndex(2)
            aux = Query('ver_name', 'Version', [''], '', '', 1)
        else:
            # Exit error
            pass

        self.queryDropdown.addItems(aux)

    def Add(self):
        if self.option.currentText() == 'Categoria':
            self.displayStacked.setCurrentIndex(0)
        elif self.option.currentText() == 'Marca':
            self.displayStacked.setCurrentIndex(0)            
        elif self.option.currentText() == 'Modelo':
            self.displayStacked.setCurrentIndex(1)
        elif self.option.currentText() == 'Versão':
            self.displayStacked.setCurrentIndex(2)
        else:
            pass 

    def Display(self):
        # Clear all values
        self.displayName.clear()
        self.displayNameModels.clear()
        self.displayNameVersion.clear()
        self.displayFactoryName.clear()
        self.displayStartYear.clear()
        self.displayFinishYear.clear()
        self.displayFuel.clear()
        self.displayEngineSize.clear()
        self.displayDoors.clear()
        self.displaySeats.clear()
        self.displayHorsepower.clear()
        self.displayWeigth.clear()
        self.displayPrice.clear()
        
        if self.optionDropdown.currentText() == 'Categoria':
            query = Query('*', 'Category', ["", self.queryDropdown.currentText()], 'cat_name', 'OR', 0)
            values = query[1]
            self.displayName.setText(values[0])
            self.displayStacked.setCurrentIndex(0)

        elif self.optionDropdown.currentText() == 'Marca':
            query = Query('*', 'Brand', ['', self.queryDropdown.currentText()], 'bra_name', '', 0)
            values = query[1]
            self.displayName.setText(values[0])
            
            self.displayStacked.setCurrentIndex(0)
        
        elif self.optionDropdown.currentText() == 'Modelo':
            query = Query('*', 'Model', ['', self.queryDropdown.currentText()], 'mod_name', '', 0)
            values = query[1]
            self.displayNameModels.setText(values[0])
            self.displayFactoryName.setText(values[1])
            self.displayStartYear.setText(str(values[2]))
            self.displayFinishYear.setText(str(values[3]))
            
            self.displayStacked.setCurrentIndex(1)
        
        elif self.optionDropdown.currentText() == 'Versão':
            query = Query('*', 'Version', ['', self.queryDropdown.currentText()], 'ver_name', '', 0)
            values = query[1]
            
            self.displayNameVersion.setText(values[0])
            self.displayFuel.setText(values[1])
            self.displayEngineSize.setText(str(values[2]))
            self.displayDoors.setText(str(values[3]))
            self.displaySeats.setText(str(values[4]))
            self.displayHorsepower.setText(str(values[5]))
            self.displayWeigth.setText(str(values[6]))
            self.displayPrice.setText(str(values[7]))
            
            self.displayStacked.setCurrentIndex(2)
        else:
            # Error code
            pass
        
    # DB command
    def Operation(self):
        if self.mode == 'Editar':
            editSucessMSG = QMessageBox()
            editSucessMSG.setWindowTitle('Sucesso')
            editSucessMSG.setText('Entrada editada na Base de Dados com sucesso')
            editSucessMSG.setIcon(QMessageBox.Information)

            editWarningMSG = QMessageBox()
            editWarningMSG.setWindowTitle('Aviso')
            editWarningMSG.setText('Entrada não editada na Base de Dados')
            editWarningMSG.setIcon(QMessageBox.Warning)
            if self.optionDropdown.currentText() == 'Categoria':
                id = Query('cat_id', 'Category', ['', self.queryDropdown.currentText()], 'cat_name', '', 0)          
                Edit('Category', [self.displayName.text()], id[1])
                editSucessMSG.exec_()
            elif self.optionDropdown.currentText() == 'Marca':
                id = Query('bra_id', 'Brand', ['', self.queryDropdown.currentText()], 'bra_name', '', 0)
                Edit('Brand', [self.displayName.text()], id[1])
                editSucessMSG.exec_()
            elif self.optionDropdown.currentText() == 'Modelo':
                id = Query('mod_id', 'Model', ['', self.queryDropdown.currentText()], 'mod_name', '', 0)
                Edit('Model', [self.displayNameModels.text(), self.displayFactoryName.text(), self.displayStartYear.text(), self.displayFinishYear.text()], id[1])
                editSucessMSG.exec_()
            elif self.optionDropdown.currentText() == 'Versão':
                id = Query('ver_id', 'Version', ['', self.queryDropdown.currentText()], 'ver_name', '', 0)
                Edit('Version', [self.displayNameVersion.text(), self.displayFuel.text(), self.displayEngineSize.text(), self.displayDoors.text(), self.displaySeats.text(), self.displayHorsepower.text(), self.displayWeigth.text(), self.displayPrice.text()], id[1])
                editSucessMSG.exec_()
            else:
                # Error code
                editWarningMSG.exec_()
                pass
        
        elif self.mode == 'Remover':
            removeSucessMSG = QMessageBox()
            removeSucessMSG.setWindowTitle('Sucesso')
            removeSucessMSG.setText('Entrada removida da Base de Dados com sucesso')
            removeSucessMSG.setIcon(QMessageBox.Information)

            removeWarningMSG = QMessageBox()
            removeWarningMSG.setWindowTitle('Aviso')
            removeWarningMSG.setText('Entrada não removida da Base de Dados')
            removeWarningMSG.setIcon(QMessageBox.Warning)
            if self.optionDropdown.currentText() == 'Categoria':         
                id = Query('cat_id', 'Category', ['', self.queryDropdown.currentText()], 'cat_name', '', 0)
                Delete('Category', id[1])
                removeSucessMSG.exec_()
            elif self.optionDropdown.currentText() == 'Marca':
                id = Query('bra_id', 'Brand', ['', self.queryDropdown.currentText()], 'bra_name', '', 0)
                Delete('Brand', id[1])
                removeSucessMSG.exec_()
            elif self.optionDropdown.currentText() == 'Modelo':
                id = Query('mod_id', 'Model', ['', self.queryDropdown.currentText()], 'mod_name', '', 0)
                Delete('Model', id[1])
                removeSucessMSG.exec_()
            elif self.optionDropdown.currentText() == 'Versão':
                id = Query('ver_id', 'Version', ['', self.queryDropdown.currentText()], 'ver_name', '', 0)
                Delete('Version', id[1])
                removeSucessMSG.exec_()
            else:
                # Error code
                removeWarningMSG.exec_()
                pass
        
        elif self.mode == 'Adicionar':
            repeated = 0
            # Warning pop-ups
            addSucessMSG = QMessageBox()
            addSucessMSG.setWindowTitle('Sucesso')
            addSucessMSG.setText('Entrada registada na Base de Dados com sucesso')
            addSucessMSG.setIcon(QMessageBox.Information)

            addWarningMSG = QMessageBox()
            addWarningMSG.setWindowTitle('Aviso')
            addWarningMSG.setText('Já existe uma entrada na Base de Dados com os mesmos parâmetros')
            addWarningMSG.setIcon(QMessageBox.Warning)
            
            if self.option.currentText() == 'Categoria':         
                names = Query('cat_name', 'Category', [''], '', '', 1)
                # Verifies if it's a non repeated value
                for x in names:
                    if x == self.displayName.text():
                        repeated = 1
                        break
                # Adds new Category if it's new
                if repeated == 0:
                    Add('Category', [self.displayName.text()])
            elif self.option.currentText() == 'Marca':
                names = Query('bra_name', 'Brand', [''], '', '', 1)
                for x in names:
                    if x == self.displayName.text():
                        repeated = 1
                        break
                if repeated == 0:
                    Add('Category', [self.displayName.text()])
            elif self.option.currentText() == 'Modelo':
                values = Query('*', 'Model', [''], '', '', 0)
                names = values[:][0]
                repeatedID = []
                factoryNames = values[:][1]
                for x in range(names):
                    if names[x] == self.displayModelName.text():
                        repeated = 1
                        repeatedID.append(x)
                for x in range(repeatedID):
                    if factoryName[x] == self.displayFactoryName.text():
                        repeated = 1
                        break
                if repeated == 0:
                    Add('Model', [self.displayModelName.text(), self.displayFactoryName.text(), self.displayStartYear.text(), self.displayFinishYear.text()])
            elif self.option.currentText() == 'Versão':
                values = Query('*', 'Version', [''], '', '', 1)
                names = values[:][0]
                repeatedID = []
                prices = values[:][7]
                for x in range(names):
                    if names[x] == self.displayVersionName.text():
                        repeated = 1
                        repeatedID.append(x)
                for x in range(repeatedID):
                    if factoryName[x] == self.displayPrice.text():
                        repeated = 1
                        break
                if repeated == 0:
                    Add('Version', [self.displayVersionName.text(), self.displayFuel.text(), self.displayEngineSize.text(), self.displayDoors.text(), self.displaySeats.text(), self.displayHorsepower.text(), self.displayWeigth.text(), self.displayPrice.text()])
            else:
                # Error code
                pass
            if repeated == 1:
                # Warnes for the repeted existence
                addWarningMSG.exec_()
            else:
                addSucessMSG.exec_()
        else:
            # Error code
            pass
        
        self.close()


# Invokes dialogs
## Add
def AddDialog(dbPath, path, iconPath, mode):
    addDialog = CreateDialog(dbPath, path, iconPath, mode)
    addDialog.AddDlg()
    
    addDialog.exec_()

## Edit
def EditDialog(dbPath, path, iconPath, mode):
    editDialog = CreateDialog(dbPath, path, iconPath, mode)
    editDialog.EditDlg()

    editDialog.exec_()

## Remove
def RemoveDialog(dbPath, path, iconPath, mode):
    removeDialog = CreateDialog(dbPath, path, iconPath, mode)
    removeDialog.RemoveDlg()
    
    removeDialog.exec_()