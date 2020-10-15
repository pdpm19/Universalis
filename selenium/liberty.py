# Liberty
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import time

def Liberty(user: str, password: str, simulationData):
    global webdriver, driver

    # Opens a new tab
    driver.execute_script(
        "window.open('https://connect.libertyseguros.pt/Login/Login.aspx?IntegratedLogin=False');")
    driver.switch_to_window(driver.window_handles[1])

    # Localizators
    userFieldXPath = "//input[@name='LibertyTheme_wtwb$block$wtContent$LibertyTheme_wt19$block$wtColumn1$wtTxtUsername']"
    passwordFieldXPath = "//input[@name='LibertyTheme_wtwb$block$wtContent$LibertyTheme_wt19$block$wtColumn1$wtTxtPassword']"
    submitButtonFieldXPath = "//input[@name='LibertyTheme_wtwb$block$wtContent$LibertyTheme_wt19$block$wtColumn1$wtloginBtn']"

    # Tries to find the elements, has 10 seconds to find each element
    userFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(userFieldXPath))
    passwordFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(passwordFieldXPath))
    submitButtonFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(submitButtonFieldXPath))

    # Fills the elements in homepage
    userFieldElement.click()
    userFieldElement.send_keys(user)
    passwordFieldElement.click()
    passwordFieldElement.send_keys(password)
    submitButtonFieldElement.click()
