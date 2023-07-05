# define all tests under class, and all tests under methods - good practice
# tests copied from e2etestpractice in sgtest
# can give actions/operations in here, but have the elements/locators in the pageobjects
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# use parameter BaseClass which has all the invoke browser code in so it inherits
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger() # calls getLogger method from BaseClass
        homePage = HomePage(self.driver)
        homePage.shopItems().click() # can give operations in testcase, but the object goes in pageobject class

        log.info("getting all product titles")
        checkOutPage = CheckOutPage(self.driver)

        products = checkOutPage.getProductTitles()
        i = -1

        for product in products:
            productName = product.text
            log.info(product.text)
            if productName == "Blackberry":
                checkOutPage.getProductNameButton()[i].click()  # this will check if button is present inside div/h4/a under blackberry

        checkOutPage.checkOutItems().click()
        # same as self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

        checkOutPage.checkOutItemsFinal().click()
        # same as self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        log.info("Entering country name as ind")
        # auto suggestive dropdown

        confirmPage = ConfirmPage(self.driver)

        confirmPage.dropdownType().send_keys("ind")
        #self.driver.find_element(By.ID, "country").send_keys("ind")

        # results take time to display so use explicit wait
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

        self.verifyLinkPresence("India")

        confirmPage.dropdownSelect().click()
        #self.driver.find_element(By.LINK_TEXT, "India").click()

        confirmPage.checkbox().click()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        confirmPage.purchase().click()
        #self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text  # can just use any of the classnames if there's multiple

        log.info("Text received from application is: " + successText)
        # this will check if partial text is in that variable. saves you putting the whole text by ==
        #assert "Success! Thank you!" in successText

        #fail test - for screenshot purpose
        assert "Success! hellllllo Thank you!" in successText