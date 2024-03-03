from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop=(By.XPATH, "//*[text()='Shop']")

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    selectDropDown = (By.ID, "exampleFormControlSelect1")
    nameLabel = (By.XPATH, "/html/body/app-root/form-comp/div/form/div[1]/label")



    def shopitem(self):
        return self.driver.find_element(*HomePage.shop)

    def getname(self):
        return self.driver.find_element(*HomePage.email)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getDropDown(self):
        return self.driver.find_element(*HomePage.selectDropDown)

    def getLabelName(self):
        return self.driver.find_element(*HomePage.nameLabel)

