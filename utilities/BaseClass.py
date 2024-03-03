import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:


    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 20)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        dropDown = Select(locator)
        dropDown.select_by_visible_text(text)
    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # fileHandler object

        logger.setLevel(logging.DEBUG)
        #logger.debug("A debug statement is executed")
        #logger.info("Information statement")
        #logger.warning("Something is warning")
        #logger.error("A major error has happened")
        #logger.critical("Critical error")
        return logger
