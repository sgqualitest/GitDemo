import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()  # calls getLogger method from BaseClass
        homepage = HomePage(self.driver)
        log.info("Name captured is :" + getData["name"])
        homepage.getName().send_keys(getData["name"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMsg().text

        assert ("Success" in alertText)

        # ADDED THIS LINE TO DEMO GIT CODE UPDATE
        print("I have updated code as a main user GitDemo, so new user can download this....")

        # ADDED THIS LINE TO DEMO GIT CODE UPDATE
        print("I have updated code as a new user GitStuff,....")

        # this will refresh the data in url, so you can fill in with another data set, otherwise it will enter both data in same box
        #i.e. shyamgorasia, test@test.comtest2@test.com etc
        self.driver.refresh()



    # this will let you put multiple data sets in to form so above hardcoding is not needed and can just replace with getData[0] etc
    #@pytest.fixture(params=HomePageData.test_HomePage_data)
    #def getData(self, request):
     #   return request.param

    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param