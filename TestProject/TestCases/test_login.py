# from lib2to3.pgen2 import driver
import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.LoginPage import LoginPageLocators
from Utilities.readProperties import ReadConfig         # IMP to remember
# from Utilities.customLogs import LogGen

import pandas as pd


class Test_01_Login:
    google_url = ReadConfig.getAppURL()     # IMP to remember
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()                # IMP to remember
    # log = logging.getLogger(__name__)
    logger = logging.getLogger(__name__)

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_homePageTitle(self, setup_and_teardown):
        self.logger.info("************** test_homePageTitle ****************")
        self.logger.info("************** Verifying Home Page Title ****************")
        self.driver = setup_and_teardown                 # IMP to remember
        print('TC test_homePageTitle')
        # self.driver.get(self.google_url)
        actual_login_title = self.driver.title
        if actual_login_title == 'OrangeHRM':
            print('Page title verified')
            self.driver.close()
            self.logger.info("************** Home Page Title TestCase passed ****************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************** Home Page Title TestCase failed ****************")
            assert False

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_login(self, setup_and_teardown):
        self.logger.info("************** test_login ****************")
        self.logger.info("************** Verifying Login Test ****************")
        self.driver = setup_and_teardown             # IMP to remember

        self.login_obj = LoginPageLocators(self.driver)     # IMP to remember
        self.login_obj.set_username(self.username)
        self.login_obj.set_password(self.password)
        self.login_obj.click_login()
        time.sleep(2)
        home_title = self.driver.title
        if home_title == 'OrangeHRM':
            self.driver.close()
            self.logger.info("************** Login TestCase passed ****************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("************** Login TestCase failed ****************")
            assert False

    # @pytest.mark.sanity
    def test_verifyTabs(self, setup_and_teardown):
        self.logger.info("************** test_verifyTabs ****************")
        self.logger.info("************** Verifying Tabs names ****************")
        self.driver = setup_and_teardown        # IMP to remember

        actual_login_title = self.driver.title
        if actual_login_title == 'OrangeHRM':
            self.driver.close()
            self.logger.info("************** Verifying Tabs names TestCase passed ****************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_verifyTabs.png")
            self.driver.close()
            self.logger.info("************** Verifying Tabs names TestCase failed ****************")
            assert False



