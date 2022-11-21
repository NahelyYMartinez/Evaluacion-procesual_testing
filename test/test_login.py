import unittest
from selenium import webdriver
from tasks.login_page import LoginPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from time import sleep


class Test_Login(unittest.TestCase):
    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    __user = 'nahely@gmail.com'
    __password = '123456'
    __user_incorrect = 'nahelyyanez@gmail.com'



    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test1_init_web(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)
        sleep(3)
    def test2_login_incorrect(self):
        driver = self.driver
        LoginPage().incorrect_login(driver, self.__user_incorrect, self.__password)
        self.assertTrue("user incorrect")
        sleep(3)
    def test3_login_correct(self):
        driver = self.driver
        LoginPage().correct_login(driver, self.__user, self.__password)
        self.assertTrue("user correct")


    # @classmethod
    # def tearDownClass(cls):
    # cls.driver.quit()
