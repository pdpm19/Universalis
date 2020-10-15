# Login
# Standard imports
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from crypto import DigestSHA256

# Hash do acesso à aplicação
hash = b'\x03\xacgB\x16\xf3\xe1\\v\x1e\xe1\xa5\xe2U\xf0g\x956#\xc8\xb3\x88\xb4E\x9e\x13\xf9x\xd7\xc8F\xf4'

# Login Password Dialog
class LoginDialog(QDialog):
    def __init__(self, paths):
        uiPath = paths[0]
        iconPath = os.path.join(uiPath, 'images', 'Universalis-RM-icon.png')
        super(LoginDialog, self).__init__()
        self.setWindowTitle('Acesso')
        self.setWindowIcon(QIcon(iconPath))  # Insere o icon
        self.numberTries = 0    # number of tries
        
        self.password = QLabel('Palavra-passe:')
        self.passwordField = QLineEdit()
        self.passwordField.setEchoMode(QLineEdit.Password)  # shows ** instead of characters
        
        # Login Buttons (special type of buttons for Dialogs)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.rejected.connect(self.close) # closes the dlg
        self.passwordField.editingFinished.connect(self.Login)  # listenig to see if that field is edited
        self.grid = QGridLayout()
        self.grid.addWidget(self.password, 0,0)
        self.grid.addWidget(self.passwordField, 0,1)
        
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.grid)
        self.layout.addWidget(self.buttonBox)
        
        self.setLayout(self.layout)

    # Checks if the password is correct, user has numberTries, 3, consecutive tries
    def Login(self):
        global hash
        if DigestSHA256(self.passwordField.text()) == hash:
            self.buttonBox.accepted.connect(self.accept)
            return self.passwordField.text()
        elif self.numberTries < 2 :
            self.numberTries = self.numberTries + 1
            self.passwordField.setText("")
            self.passwordField.setPlaceholderText("%d tentativas restantes..." %(3 - self.numberTries))   # warns the user of the number of left tries
        else:
            sys.exit()  # Closes the app