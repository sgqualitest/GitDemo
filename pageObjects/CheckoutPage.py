from selenium.webdriver.common.by import By
class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    productTitles = (By.CSS_SELECTOR, ".card-title a")
    # above is same as: products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    productNameButton = (By.CSS_SELECTOR, ".card-footer button")

    checkOutButton1 = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    checkOutButton2 = (By.XPATH, "//button[@class='btn btn-success']")



    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutPage.productTitles)  # use star

    def getProductNameButton(self):
        return self.driver.find_elements(*CheckOutPage.productNameButton)  # use star

    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton1)

    def checkOutItemsFinal(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton2)

