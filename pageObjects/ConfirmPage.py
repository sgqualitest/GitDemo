from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")

    countrySelect = (By.LINK_TEXT, "India")

    TsCsCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    purchaseButton = (By.CSS_SELECTOR, ".btn-success")

    def dropdownType(self):
        return self.driver.find_element(*ConfirmPage.country)  # use star

    def dropdownSelect(self):
        return self.driver.find_element(*ConfirmPage.countrySelect)

    def checkbox(self):
        return self.driver.find_element(*ConfirmPage.TsCsCheckbox)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)
