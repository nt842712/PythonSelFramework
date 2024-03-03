from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    purchaseBtn = (By.CSS_SELECTOR, "input[type='submit']")
    successmsg = (By.CLASS_NAME, "alert-success")

    def getpurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getsuccessmsg(self):
        return self.driver.find_element(*ConfirmPage.successmsg)



