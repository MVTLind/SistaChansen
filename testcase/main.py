import unittest
from selenium import webdriver
import page

class SciFiRadioButton(unittest.Testcase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.sfbok.se/")

    def tearDown(self):
        self.driver.close()