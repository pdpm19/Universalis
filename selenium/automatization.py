# Website automatization
import os
import time
import sys
from crypto import KeyGenerator, DecryptFile, DigestSHA256
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
# Websites
from acp import ACP
from caravela import Caravela
from ok import OK
from tranquilidade import Tranquilidade
accessPath = ''

def Automatization(args, password, simulationData):
    global path, accessPath, seleniuimPath, webdriverPath, driver
    accessPath = args[1]
    seleniuimPath = args[3]

    # Gets the OS running the program so it can match the Webdriver version
    osType = sys.platform
    if osType.startswith('linux'):
        webdriverPath = os.path.join(seleniuimPath, 'WebDriver', 'chrome', 'chromedriver_linux')
    elif osType.startswith('win32') or osType.startswith('cygwin'):
        webdriverPath = os.path.join(seleniuimPath, 'WebDriver','chrome', 'chromedriver_windows.exe')
    elif osType.startswith('darwin'):
        webdriverPath = os.path.joion(seleniuimPath, 'WebDriver', 'chrome',  'chromedriver_mac')
    else:
        # Error code
        sys.exit()

    # Decrypts the access file, for those websites with access
    users = []
    passwords = []

    decrypted = DecryptFile(os.path.join(accessPath, 'acessos.csv.enc'), KeyGenerator(2, DigestSHA256(password)))
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

    # Iniciates the webdriver (Chrome in my case)
    driver = webdriver.Chrome(webdriverPath)
    '''
    # Simulation functions calls
    Tranquilidade(users[0], passwords[0], simulationData)
    # Necessito da nova pass
    Liberty(users[1], passwords[1], simulationData)
    Caravela(users[1], passwords[1], simulationData)
    '''
    
    Caravela(driver, users[1], passwords[1], simulationData, 0)
    # Websites extra
    ACP(driver, simulationData , 1)
    #OK(driver, simulationData, 2)
    Tranquilidade(driver, users[0], passwords[0], simulationData, 2)

