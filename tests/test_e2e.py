import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass




class Testone(BaseClass):
    def test_e2e(self):
        log=self.getlogger()
        homepage = HomePage(self.driver)
        checkoutpage = CheckOutPage(self.driver)
        confirmpage = ConfirmPage(self.driver)

        homepage.shopitem().click()
        log.info("Clicking shop Item")

        # service_obj = Service("/Users/ntalesha/Downloads/chromedriver-mac-arm64 4/chromedriver")
        # driver = webdriver.Chrome(service=service_obj)

        #self.driver.find_element(By.XPATH, "//*[text()='Shop']").click()
        #listOfProdELe = self.driver.find_elements(By.XPATH, "//*[@class='card h-100']")

        listOfProdEle = checkoutpage.getcardTitles()

        for ele in listOfProdEle:
            phone = ele.find_element(By.XPATH, "div/h4/a").text
            #phone = checkoutpage.getCardFooter(ele).text
            print(phone)
            if phone == "Blackberry":
                print("Inside")
                ele.find_element(By.XPATH, "div/button").click()
                print("Clicked")

        checkoutpage.getcheckout().click()


        #self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        checkoutpage.getsuccesscheckout().click()
        #self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")
        checkoutpage.getcountry().send_keys("Ind")

        time.sleep(5)
        #wait = WebDriverWait(self.driver, 20)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.verifyLinkPresence("India")



        checkoutpage.getcountryname().click()


        #self.driver.find_element(By.LINK_TEXT, "India").click()
        time.sleep(5)

        #self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR, "#checkbox2"))

        self.driver.execute_script("arguments[0].click();", checkoutpage.getcheckbox())
        # driver.find_element(By.CSS_SELECTOR,"#checkbox2").click()
        #self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        confirmpage.getpurchaseBtn().click()

        #success = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        success = confirmpage.getsuccessmsg().text

        assert "Success! Thank you! " in success
        time.sleep(4)


