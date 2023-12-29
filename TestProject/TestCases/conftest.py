import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

from pageObject.LoginPage import LoginPageLocators

sys.path.append('C:\\Users\\lenovo\\PycharmProjects\\TestProject\\pageObject')


# Below 'setup' method for normal PyTest Framework @pytest.fixture() def setup(browser, env): if browser == 'chrome':
# serv_obj = Service("C:\\Users\\lenovo\\Downloads\\seleniumGridFiles\\chromedriver.exe") driver = webdriver.Chrome(
# service=serv_obj) print("Launching Chrome browser") driver.get(LoginPageLocators.url) # driver.maximize_window()
# driver.execute_script("window.moveTo(0, 0); window.resizeTo(window.screen.availWidth, window.screen.availHeight);")
# driver.implicitly_wait(30) login_obj2 = LoginPageLocators(driver) driver.find_element(By.XPATH,
# login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN) driver.find_element(By.XPATH,
# login_obj2.first_link_on_google_search).click() return driver elif browser == 'firefox': serv_obj = Service(
# "C:\\Users\\lenovo\\Downloads\\seleniumGridFiles\\geckodriver.exe") driver = webdriver.Firefox(service=serv_obj)
# print("Launching Firefox browser") driver.get(LoginPageLocators.url) # driver.maximize_window()
# driver.execute_script( "window.moveTo(0, 0); window.resizeTo(window.screen.availWidth,
# window.screen.availHeight);") driver.implicitly_wait(30) login_obj2 = LoginPageLocators(driver)
# driver.find_element(By.XPATH, login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN)
# driver.find_element(By.XPATH, login_obj2.first_link_on_google_search).click() return driver elif browser == 'edge':
# serv_obj = Service("C:\\Users\\lenovo\\Downloads\\seleniumGridFiles\\msedgedriver.exe") driver = webdriver.Edge(
# service=serv_obj) print("Launching Edge browser") driver.get(LoginPageLocators.url) # driver.maximize_window()
# driver.execute_script( "window.moveTo(0, 0); window.resizeTo(window.screen.availWidth,
# window.screen.availHeight);") driver.implicitly_wait(30) login_obj2 = LoginPageLocators(driver)
# driver.find_element(By.XPATH, login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN)
# driver.find_element(By.XPATH, login_obj2.first_link_on_google_search).click() return driver else: print("Abe sale
# valid browser naam daal be") driver.quit()


# 2nd Method
# # Below 'setup_and_teardown' method for normal PyTest Framework
# @pytest.fixture()
# def setup_and_teardown(browser, env):
#     desired_cap = None
#     if browser == 'chrome':
#         desired_cap = DesiredCapabilities.CHROME.copy()
#         global driver
#         serv_obj = Service("C:\\Users\\lenovo\\Downloads\\seleniumGridFiles\\chromedriver.exe")
#         # driver = webdriver.Chrome(service=serv_obj)
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install))
#
#         print("Launching Chrome browser")
#         driver.get(LoginPageLocators.url)
#         driver.maximize_window()
#         driver.implicitly_wait(30)
#         login_obj2 = LoginPageLocators(driver)
#         driver.find_element(By.XPATH, login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN)
#         driver.find_element(By.XPATH, login_obj2.first_link_on_google_search).click()
#         return driver
#     elif browser == 'firefox':
#         desired_cap = DesiredCapabilities.FIREFOX.copy()
#         serv_obj = Service("C:\\Users\\lenovo\\Downloads\\seleniumGridFiles\\geckodriver.exe")
#         driver = webdriver.Firefox(service=serv_obj)
#         print("Launching Firefox browser")
#         driver.get(LoginPageLocators.url)
#         driver.maximize_window()
#         driver.implicitly_wait(30)
#         login_obj2 = LoginPageLocators(driver)
#         driver.find_element(By.XPATH, login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN)
#         driver.find_element(By.XPATH, login_obj2.first_link_on_google_search).click()
#         return driver
#     elif browser == 'edge':
#         desired_cap = DesiredCapabilities.EDGE.copy()
#         serv_obj = Service("C:\\Users\\lenovo\\Downloads\\seleniumGridFiles\\msedgedriver.exe")
#         driver = webdriver.Edge(service=serv_obj)
#         print("Launching Edge browser")
#         driver.get(LoginPageLocators.url)
#         driver.maximize_window()
#         driver.implicitly_wait(30)
#         login_obj2 = LoginPageLocators(driver)
#         driver.find_element(By.XPATH, login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN)
#         driver.find_element(By.XPATH, login_obj2.first_link_on_google_search).click()
#         return driver
#     else:
#         print("Abe saale valid browser naam daal be")
#         driver.quit()


# 3rd Method
# Below 'setup_remote' method for normal PyTest Framework

# global driver
@pytest.fixture()
def setup_and_teardown(browser):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Remote(command_executor='http://192.168.1.3:4444/wd/hub',
                                  options=options
                                  )
        driver.maximize_window()
        driver.get(LoginPageLocators.url)
        driver.implicitly_wait(30)
        login_obj2 = LoginPageLocators(driver)
        driver.find_element(By.XPATH, login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN)
        driver.find_element(By.XPATH, login_obj2.first_link_on_google_search).click()
        time.sleep(2)
        return driver
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_experimental_option("detach", True)
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Remote(command_executor='http://192.168.1.2:4444/wd/hub',
                                  options=options
                                  )
        driver.maximize_window()
        driver.get(LoginPageLocators.url)
        driver.implicitly_wait(30)
        login_obj2 = LoginPageLocators(driver)
        driver.find_element(By.XPATH, login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN)
        driver.find_element(By.XPATH, login_obj2.first_link_on_google_search).click()
        time.sleep(2)
        return driver
    else:
        print("Abe saale valid browser naam daal be")
        # driver.quit()

    # driver = webdriver.Chrome(options=options)
    # driver.get('https://www.facebook.com/')

    #
    # global driver
    # driver = None
    # desired_cap = None
    #
    # if browser == 'chrome':
    #     desired_cap = DesiredCapabilities.CHROME.copy()
    # elif browser == 'firefox':
    #     desired_cap = DesiredCapabilities.FIREFOX.copy()
    # elif browser == 'edge':
    #     desired_cap = DesiredCapabilities.EDGE.copy()
    # else:
    #     print("Abe saale valid browser naam daal be")

    # Connect to Selenium Grid Hub
    # capabilities = {
    #     "platformName": "Android",
    #     "platformVersion": "12",
    # }
    # driver = webdriver.Remote(command_executor='http://192.168.1.3:4444/wd/hub', desired_capabilities=desired_cap)
    #
    # driver.maximize_window()
    # driver.get(LoginPageLocators.url)
    # driver.implicitly_wait(30)
    # login_obj2 = LoginPageLocators(driver)
    # driver.find_element(By.XPATH, login_obj2.google_search_editbox).send_keys("orangehrm demo", Keys.RETURN)
    # driver.find_element(By.XPATH, login_obj2.first_link_on_google_search).click()
    # # return driver
    #
    # yield driver  # This is the value returned by the fixture

    # Teardown code (optional)
    # if driver is not None:
    #     driver.quit()


def pytest_addoption(parser):  # This will get value from CLI/hooks
    parser.addoption("--browser")
    # parser.addoption("--env")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# @pytest.fixture()
# def env(request):                   # This will return the Browser value to setup method
#     return request.config.getoption("--env")
