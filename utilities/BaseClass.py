# call fixtures here
import inspect
import logging

from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# can use this for all test cases - because we want to invoke browser for all tests
# also presence of elements like waiting for the options in dropdown to appear with webdriver wait explicit wait
# common utiltiies
@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile2.log')
        logger.addHandler(fileHandler)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")  # formatter object
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    # this means, you can use this method for all dropdowns when selecting an option i.e. gender, others etc, pass locator and text parameter
    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)