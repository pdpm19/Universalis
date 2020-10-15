# Tests
import unittest
import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

path = os.sep
workingDirectory = os.getcwd()
workingDirectory = workingDirectory[:len(workingDirectory)-5]
print(workingDirectory)
accessPath = os.path.join(workingDirectory, 'Access')
dbPath = os.path.join(workingDirectory, 'DB')
uiPath = os.path.join(workingDirectory, 'UI')
seleniumPath = os.path.join(workingDirectory, 'Selenium')

sys.path.append(accessPath)
sys.path.append(dbPath)
sys.path.append(uiPath)
sys.path.append(seleniumPath)

# My imports
from loginDlg import LoginDialog
from editDlg import EditDialog, RemoveDialog, AddDialog
from commands_db import Query, Search, Edit, Delete, Add
from automatization import Automatization
from crypto import DecryptFile, KeyGenerator, DigestSHA256

# Global variables
paths = [path, uiPath, accessPath, dbPath, seleniumPath]

class TestDBInsert(unittest.TestCase):
    # Possible insertion
    def test_insertion(self):
        global dbPath, path, uiPath
        app = QApplication([])
        add = EditDialog(dbPath, path, uiPath + path + 'Imagens' + path + 'Universalis-RM-icon.png', 'Adicionar')
        # Category,...
        add.option.setCurrentIndex(1)
        # 
        add.displayStacked.setCurrentIndex(3)
    # Impossible insertion
'''    
class TestDBEdit(unittest.TestCase):

class TestDBRemove(unittest.TestCase):
'''

if __name__ == "__main__":
    unittest.main()