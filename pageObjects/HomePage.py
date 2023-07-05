# PAGE OBJECT MECHANISM - put all objects in homepage in here, and call driver from here
# class variables are called as classname. [ ] and self. [] if method


from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    # create a constructor method to call the driver from the testcase
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMsg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)

    def shopItems(self):
        #self.driver.find_element(*HomePage.shop).click()
        return self.driver.find_element(*HomePage.shop) # use star


        # above is just the same as below;
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click() in the test_e2e file