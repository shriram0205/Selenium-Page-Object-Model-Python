import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.home.LoginPage import LoginPage
import HTMLTestRunner
import unittest
from ddt import ddt, data, unpack
from utilities.ReadData import get_csv_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@ddt
class LoginTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:/Python/Scripts/geckodriver.exe")
        base_url = "https://www.google.com/gmail"
        self.driver.get(base_url)

    # this method gets data from csv file and performs data driven testing for different values username and password
    @data(*get_csv_data("/Users/shriram/PycharmProjects/Gmail/testdata.csv"))
    @unpack
    def test_validLogin(self, username, password):
        lp = LoginPage(self.driver)
        lp.login(username, password)
        time.sleep(3)

    # test case to check for correct username and invalid password
    def test_invalidPassword(self):
        lp = LoginPage(self.driver)
        lp.login("shriram4cinsights@gmail.com", "efefefef")
        time.sleep(3)
        password_text = self.driver.find_element(By.XPATH, lp.passwordText)
        assert password_text.text == "Wrong password. Try again."

    # test case to check for correct username and empty password
    def test_emptyPassword(self):
        lp = LoginPage(self.driver)
        lp.login("shriram4cinsights@gmail.com", "")
        time.sleep(3)
        password_text = self.driver.find_element(By.XPATH, lp.passwordText)
        assert password_text.text == "Enter a password"

    # test case to check for empty username
    def test_emptyUsername(self):
        lp = LoginPage(self.driver)
        lp.login_with_invalid_username(" ")
        username_text = lp.get_username_error_text()
        assert username_text.text == "Enter an email or phone number"

    # test case to check for invalid username
    def test_invalidUsername(self):
        lp = LoginPage(self.driver)
        lp.login_with_invalid_username("shriram4cinsight@gmail.com")
        username_text = lp.get_username_error_text()
        assert username_text.text == "Couldn't find your Google Account"

    # to verify forgot Email display text
    def test_validateForgotEmailText(self):
        lp = LoginPage(self.driver)
        lp.forgot_email()
        time.sleep(2)
        forgot_email = lp.get_heading_text()

    # to verify forgot password display text
    def test_validateForgotPasswordText(self):
        lp = LoginPage(self.driver)
        lp.navigate_to_password_page("shriram4cinsights@gmail.com")
        time.sleep(5)
        forgot_password = lp.get_forgot_password_page()
        assert forgot_password.text == "Enter the last password you remember"

    # to verify create button is displayed for every user
    def test_createAccount(self):
        lp = LoginPage(self.driver)
        lp.verify_create_account()
        wait = WebDriverWait(self.driver, 15)
        create_account_text = wait.until(EC.presence_of_element_located((By.XPATH, lp.createAccountText)))
        assert create_account_text.text == "Create your Google Account"

    # validate log out when the user clicks on log button once after logging into GMail
    def test_validateLogOut(self):
        lp = LoginPage(self.driver)
        lp.login("shriram4cinsights@gmail.com", "Test1234!")
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, lp.userNameLogout)))
        lp.logout()
        wait = WebDriverWait(self.driver, 5)
        heading_text = wait.until(EC.presence_of_element_located((By.ID, lp.chooseAnAccount)))
        assert heading_text.text == "Hi Shriram"

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    HTMLTestRunner.main()
