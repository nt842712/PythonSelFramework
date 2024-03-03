from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self , driver):
        self.driver = driver

    listofcardTitle = (By.XPATH, "//*[@class='card h-100']")
    cardFooter = (By.XPATH, "div/h4/a")
    checkout = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    successcheckout = (By.CSS_SELECTOR, ".btn.btn-success")
    country = (By.CSS_SELECTOR, "#country")
    countryName = (By.LINK_TEXT, "India")
    checkbox=(By.CSS_SELECTOR, "#checkbox2")


    def getcheckbox(self):
        return self.driver.find_element(*CheckOutPage.checkbox)

    #self.driver.find_element(By.CSS_SELECTOR, "#checkbox2")
    def getcountry(self):
        return self.driver.find_element(*CheckOutPage.country)

    def getcountryname(self):
        return self.driver.find_element(*CheckOutPage.countryName)

    def getcountryname(self):
        return self.driver.find_element(*CheckOutPage.countryName)



    #self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")


    def getcardTitles(self):
        return self.driver.find_elements(*CheckOutPage.listofcardTitle)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getcheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def getsuccesscheckout(self):
        return self.driver.find_element(*CheckOutPage.successcheckout)