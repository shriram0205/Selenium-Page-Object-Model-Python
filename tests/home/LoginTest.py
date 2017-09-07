import time
from selenium import webdriver
from pages.home.LoginPage import LoginPage
import HTMLTestRunner
import unittest
from ddt import ddt, data, unpack
from utilities.ReadData import getCSVData

@ddt
class LoginTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:/Python/Scripts/geckodriver.exe")

    # this method gets data from the csv file and performs data driven testing for different usernames and passwords
    @data(*getCSVData("/Users/shriram/PycharmProjects/Gmail/testdata.csv"))
    @unpack
    def test_validLogin(self, userName, passWord):
        baseURL="https://www.google.com/gmail"
        self.driver.get(baseURL)
        lp=LoginPage(self.driver)
        lp.login(userName,passWord)
        time.sleep(3)
        self.assertEqual("Inbox (1) - shriram4cinsights@gmail.com - Gmail",self.driver.title)

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    HTMLTestRunner.main()

