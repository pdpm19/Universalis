import os
# Imports do Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

path = os.path.join(os.getcwd(),'chromedriver_linux')   # vai buscar o path do Chromedriver
driver = webdriver.Chrome(path) # Browser driver, neste caso ChromeDriver do Linux
driver.get('https://google.pt') # Página que será aberta na nova aba do browser
driver.maximize_window()        # Ecrã total

# Localiza o campo do motor de pesquisa
pesquisa = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name('q'))
# Envia dados
pesquisa.send_keys('Olá mundo!')
# Localiza o botão "Pesquisar"
submeter = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name('gNO89b'))
# Carrega nele
submeter.click()
