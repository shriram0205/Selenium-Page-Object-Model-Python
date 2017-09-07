from selenium.webdriver.common.by import By
import time

class LoginPage():
    username = "identifierId"
    usernameNext = ".//*[@id='identifierNext']"
    password ="password"
    passwordNext = ".//*[@id='passwordNext']"

    def __init__(self, driver):
        self.driver=driver

    def getUsernameField(self):
        return self.driver.find_element(By.ID, self.username)
    def getUserNameLink(self):
        return self.driver.find_element(By.XPATH,self.usernameNext)
    def getPasswordField(self):
        return self.driver.find_element(By.NAME,self.password)
    def getPasswordLink(self):
        return self.driver.find_element(By.XPATH,self.passwordNext)

    def enterUserName(self, email):
        self.getUsernameField().send_keys(email)

    def enterPassword(self, password):
            self.getPasswordField().send_keys(password)

    def clickUserName(self):
        self.getUserNameLink().click()
    def clickPassWord(self):
        self.getPasswordLink().click()


    def login(self, username, password):
        self.enterUserName(username)
        self.clickUserName()
        time.sleep(3)
        self.enterPassword(password)
        self.clickPassWord()