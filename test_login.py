import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageObject.LoginPage import LoginPage1

class Test_001_Logins:
    baseURL="https://admin-demo.nopcommerce.com/login"
    username="admin@yourstore.com"
    password="admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title=self.driver.title
        if act_title=="Your store. Login123":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login12(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.lp = LoginPage1(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        time.sleep(5)
        if act_title=="Dashboard / nopCommerce administration123":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login12.png")
            self.driver.close()
            assert False



