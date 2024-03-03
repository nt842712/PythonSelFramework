import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self,getData):
        homepage = HomePage(self.driver)

        homepage.getname().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getpassword().send_keys("Password@123")
        homepage.getcheckbox().click()

        self.selectOptionByText(homepage.getDropDown(),getData["gender"])
        time.sleep(5)
        #dropDown.select_by_index(0)

        message = homepage.getLabelName().text
        homepage.getname().clear()
        assert "Name" in message
        print(message)

        time.sleep(3)
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self,request):
        return request.param

