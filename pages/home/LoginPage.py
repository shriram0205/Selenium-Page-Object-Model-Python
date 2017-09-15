from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # web elements of the Login Page
    username = "identifierId"
    usernameNext = ".//*[@id='identifierNext']"
    password = "password"
    passwordNext = ".//*[@id='passwordNext']"
    usernameErrorText = ".//*[@id='view_container']/form/div[2]/div/div[1]/div[1]/div/div[2]/div[2]"
    forgotEmailText = ".//*[@id='view_container']/form/div[2]/div/div[1]/button"
    forgotPasswordText = ".//*[@id='view_container']/form/div[2]/div/div[2]/div[2]/div[2]/div"
    userNameLogout = ".//*[@id='gb']/div[1]/div[1]/div[2]/div[5]/div[1]/a/span"
    logoutButton = "gb_71"
    chooseAnAccount = "headingText"
    options = ".//*[@id='view_container']/form/div[2]/div/div[2]/div[2]/div"
    createAccount = ".//*[@id='SIGNUP']/div"
    createAccountText = ".//*[@id='wrapper']/div[2]/h1"
    forgotPasswordPage=".//*[@id='challenge']/content/div/div[1]"
    passwordText=".//*[@id='password']/div[2]/div[2]"


    def __init__(self, driver):
        self.driver = driver

    # methods to find the web elements using different locators.
    def get_username_field(self):
        return self.driver.find_element(By.ID, self.username)

    def get_username_link(self):
        return self.driver.find_element(By.XPATH, self.usernameNext)

    def get_password_field(self):
        return self.driver.find_element(By.NAME, self.password)

    def get_password_link(self):
        return self.driver.find_element(By.XPATH, self.passwordNext)

    def get_forgot_email_text(self):
        return self.driver.find_element(By.XPATH, self.forgotEmailText)

    def get_username_error_text(self):
        return self.driver.find_element(By.XPATH, self.usernameErrorText)

    def get_forgot_password_text(self):
        return self.driver.find_element(By.XPATH, self.forgotPasswordText)

    def get_username_logout(self):
        return self.driver.find_element(By.XPATH, self.userNameLogout)

    def get_logout_button(self):
        return self.driver.find_element(By.ID, self.logoutButton)

    def get_heading_text(self):
        return self.driver.find_element(By.ID, self.chooseAnAccount)

    def get_options(self):
        return self.driver.find_element(By.XPATH, self.options)

    def get_create_account(self):
        return self.driver.find_element(By.XPATH, self.createAccount)

    def get_create_account_text(self):
        return self.driver.find_element(By.XPATH, self.createAccountText)

    def get_forgot_password_page(self):
        return self.driver.find_element(By.XPATH, self.forgotPasswordPage)

    def get_password_text(self):
        return self.driver.find_element(By.XPATH, self.passwordText)


    # method to set username
    def enter_user_name(self, email):
        self.get_username_field().send_keys(email)

    # method to set password
    def enter_password(self, password):
            self.get_password_field().send_keys(password)

    # method to click next button after entering username
    def click_user_name(self):
        self.get_username_link().click()

    # method to click next button after entering password
    def click_password(self):
        self.get_password_link().click()

    # method to click user before logging out
    def click_username_logout(self):
        self.get_username_logout().click()

    # method to logout of GMail
    def click_logout_button(self):
        self.get_logout_button().click()

    # method to click on forgot email
    def click_forgot_email(self):
        self.get_forgot_email_text().click()

    # method to click on forgot password
    def click_forgot_password(self):
        self.get_forgot_password_text().click()

    # method to perform login to GMail
    def login(self, username, password):
        self.enter_user_name(username)
        self.click_user_name()
        time.sleep(3)
        self.enter_password(password)
        self.click_password()

    # method to login with invalid credentials
    def login_with_invalid_username(self, username):
        self.enter_user_name(username)
        self.click_user_name()

    # method to logout once the user has logged in
    def logout(self):
        self.click_username_logout()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.ID, self.logoutButton)))
        self.click_logout_button()

    # method to navigate to password page after entering username
    def navigate_to_password_page(self, username):
        self.enter_user_name(username)
        self.click_user_name()
        time.sleep(2)
        self.click_forgot_password()

    # method to navigate to create account page
    def verify_create_account(self):
        self.get_options().click()
        time.sleep(5)
        #wait = WebDriverWait(self.driver, 15)
        #wait.until(EC.presence_of_element_located((By.XPATH, self.createAccount)))
        self.get_create_account().click()

    # method to navigate to forgot password page
    def forgot_email(self):
        self.click_forgot_email()



