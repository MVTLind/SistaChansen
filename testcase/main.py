import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SciFiRadioButton(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.sfbok.se/")


    #def test_title(self):
    #    mainPage = page.MainPage()
    #    assert mainPage.is_title_matches()
    
    def tearDown(self):
        self.driver.close()

    def test_filterblirsynliga(self):
    # Test name: Filter blir synliga
    # Step # | name | target | value
    # 1 | open | / | 
        self.driver.get("https://www.sfbok.se/")
    # 2 | setWindowSize | 800x700 | 
        self.driver.set_window_size(800, 700)
    # 3 | assertElementPresent | linkText=Katalog | 
        elements = self.driver.find_elements(By.LINK_TEXT, "Katalog")
        assert len(elements) > 0
    # 4 | click | linkText=Katalog | 
        self.driver.find_element(By.LINK_TEXT, "Katalog").click()
    # 5 | assertElementPresent | linkText=Prylar & kläder | 
        elements = self.driver.find_elements(By.LINK_TEXT, "Prylar & kläder")
        assert len(elements) > 0
    # 6 | click | linkText=Prylar & kläder | 
        self.driver.find_element(By.LINK_TEXT, "Prylar & kläder").click()
    # 7 | assertText | css=.page-header | Prylar & kläder
        assert self.driver.find_element(By.CSS_SELECTOR, ".page-header").text == "Prylar & kläder"
    # 8 | click | css=.glyphicon-plus:nth-child(1) | 
        self.driver.find_element(By.CSS_SELECTOR, ".glyphicon-plus:nth-child(1)").click()
    # 9 | click | css=.search-filter-block:nth-child(1) > .dropdown > .btn | 
        self.driver.find_element(By.CSS_SELECTOR, ".search-filter-block:nth-child(1) > .dropdown > .btn").click()
    # 10 | click | css=.search-filter-block:nth-child(1) .ng-scope:nth-child(5) .ng-pristine | 
        self.driver.find_element(By.CSS_SELECTOR, ".search-filter-block:nth-child(1) .ng-scope:nth-child(5) .ng-pristine").click()
    # 11 | click | css=.btn-warning | 
        self.driver.find_element(By.CSS_SELECTOR, ".btn-warning").click()
    # 12 | assertElementPresent | css=.view-display-id-page | 
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".view-display-id-page")
        assert len(elements) > 0
    # 13 | close |  | 
        self.driver.close()

    # def test_iSBNverensstmmermedbokvidskning(self):
    # # Test name: ISBN överensstämmer med bok vid sökning
    # # Step # | name | target | value
    # # 1 | open | / | 
    #     self.driver.get("https://www.sfbok.se/")
    # # 2 | setWindowSize | 800x700 | 
    #     self.driver.set_window_size(800, 700)
    # # 3 | click | name=keys | 
    #     self.driver.find_element(By.NAME, "keys").click()
    # # 4 | type | name=keys | frankenstein
    #     self.driver.find_element(By.NAME, "keys").send_keys("frankenstein")
    # # 5 | sendKeys | name=keys | ${KEY_ENTER}
    #     self.driver.find_element(By.NAME, "keys").send_keys(Keys.ENTER)
    # # 6 | click | linkText=Frankenstein | 
    #     self.driver.find_element(By.XPATH, "/produkt/frankenstein-713133").click()
    # # 7 | click | css=.meta > .field-name-isbn .field-item | 
    #     self.driver.find_element(By.CSS_SELECTOR, ".meta > .field-name-isbn .field-item").click()
    # # 8 | click | name=keys | 
    #     self.driver.find_element(By.NAME, "keys").click()
    # # 9 | type | name=keys | 9781435159624
    #     self.driver.find_element(By.NAME, "keys").send_keys("9781435159624")
    # # 10 | sendKeys | name=keys | ${KEY_ENTER}
    #     self.driver.find_element(By.NAME, "keys").send_keys(Keys.ENTER)
    # # 11 | click | linkText=Frankenstein | 
    #     self.driver.find_element(By.XPATH, "/produkt/frankenstein-713133").click()
    # # 12 | close |  | 
    #     self.driver.close()  

if __name__ == "__main__":
    unittest.main()