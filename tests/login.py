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
from crypto import DigestSHA256

# Global variables
paths = [path, uiPath, accessPath, dbPath, seleniumPath]
hash = b'\x03\xacgB\x16\xf3\xe1\\v\x1e\xe1\xa5\xe2U\xf0g\x956#\xc8\xb3\x88\xb4E\x9e\x13\xf9x\xd7\xc8F\xf4'

# Test Login
class TestLogin(unittest.TestCase):
    # Login test
    def test_empty(self):
        global paths, hash
        
        # Test empty string
        app = QApplication([])
        log = LoginDialog(paths)
        
        # set value on passwordField
        log.passwordField.setText('')
        log.Login()
        log.Login()
        with self.assertRaises(SystemExit):
            log.Login()
    
    def test_only_chars(self):
        # Test wrong string
        app = QApplication([])
        log = LoginDialog(paths)
        # set value on passwordField
        log.passwordField.setText('helloworld')
        log.Login()
        log.Login()
        with self.assertRaises(SystemExit):
            log.Login()

    def test_only_numbers(self):
        # Test wrong string
        app = QApplication([])
        log = LoginDialog(paths)
        # set value on passwordField
        log.passwordField.setText('0123456789')
        log.Login()
        log.Login()
        with self.assertRaises(SystemExit):
            log.Login()

    def test_chars(self):
        # Test wrong string
        app = QApplication([])
        log = LoginDialog(paths)
        # set value on passwordField
        log.passwordField.setText('HelloWorld')
        log.Login()
        log.Login()
        with self.assertRaises(SystemExit):
            log.Login()

    def test_special_chars(self):
        # Test wrong string
        app = QApplication([])
        log = LoginDialog(paths)
        # set value on passwordField
        log.passwordField.setText('hello@world0123456789')
        log.Login()
        log.Login()
        with self.assertRaises(SystemExit):
            log.Login()

    def test_correct_password(self):
        # Test correct string
        app = QApplication([])
        log = LoginDialog(paths)
        # set value on passwordField
        log.passwordField.setText('1234')
        self.assertEqual(log.Login(), log.passwordField.text())
    

if __name__ == "__main__":
    unittest.main()