# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class TestCITestavScifibokhandlen():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    wait = WebDriverWait(self.driver, 10)
    self.driver.implicitly_wait(10)  

  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
    
  

  
  def test_iSBNverensstmmermedbokvidskning(self):
    # Test name: ISBN överensstämmer med bok vid sökning
    # Step # | name | target | value
    # 1 | open | / | 
    driver = self.driver.get("https://www.sfbok.se/")
    # 2 | setWindowSize | 800x700 | 
    self.driver.set_window_size(800, 700)
    # 3 | click | name=keys | 
    self.driver.find_element(By.NAME, "keys").click()
    # 4 | type | name=keys | frankenstein
    self.driver.find_element(By.NAME, "keys").send_keys("frankenstein")
    # 5 | sendKeys | name=keys | ${KEY_ENTER}
    self.driver.find_element(By.NAME, "keys").send_keys(Keys.ENTER)
    # 6 | click | linkText=Frankenstein |
    self.driver.find_element(By.XPATH, '//*[@id="block-system-main"]/div/div/div[3]/div/div[6]/article/h2/a').click()
    # 7 | assertText | css=.meta > .field-name-isbn .field-item | 9781435159624
    assert self.driver.find_element(By.CSS_SELECTOR, ".meta > .field-name-isbn .field-item").text == "9781435159624"
    # 8 | click | name=keys | 
    self.driver.find_element(By.NAME, "keys").click()
    # 9 | type | name=keys | 9781435159624
    self.driver.find_element(By.NAME, "keys").send_keys("9781435159624")
    # 10 | sendKeys | name=keys | ${KEY_ENTER}
    self.driver.find_element(By.NAME, "keys").send_keys(Keys.ENTER)
    # 11 | click | linkText=Frankenstein | 
    self.driver.find_element(By.LINK_TEXT, "Frankenstein").click()
    # 12 | assertText | css=.meta > .field-name-isbn .field-item | 9781435159624
    assert self.driver.find_element(By.CSS_SELECTOR, ".meta > .field-name-isbn .field-item").text == "9781435159624"
    # 13 | close |  | 
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
  
  def test_snabblnkNyheter(self):
    # Test name: Snabblänk Nyheter
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.sfbok.se/")
    # 2 | setWindowSize | 800x700 | 
    self.driver.set_window_size(800, 700)
    # 3 | assertElementPresent | css=.view-header > .block-title | Nyheter
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".view-header > .block-title")
    assert len(elements) > 0
    # 4 | click | linkText=Nyheter | 
    self.driver.find_element(By.LINK_TEXT, "Nyheter").click()
    # 5 | assertText | css=.page-header | Veckans nyheter
    assert self.driver.find_element(By.CSS_SELECTOR, ".page-header").text == "Veckans nyheter"
    # 6 | close |  | 
    self.driver.close()
  
  def test_direktknapptillvanligafrgor(self):
    # Test name: Direktknapp till vanliga frågor
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.sfbok.se/")
    # 2 | setWindowSize | 800x700 | 
    self.driver.set_window_size(800, 700)
    # 3 | click | css=.kundo-knowledge-widget__text | 
    self.driver.find_element(By.CSS_SELECTOR, ".kundo-knowledge-widget__text").click()
    # 4 | selectFrame | index=2 | 
    self.driver.switch_to.frame(2)
    # 5 | click | css=.widget-button--pop-out > .icon | 
    self.vars["window_handles"] = self.driver.window_handles
    # 6 | //storeWindowHandle | root | 
    self.driver.find_element(By.CSS_SELECTOR, ".widget-button--pop-out > .icon").click()
    # 7 | selectWindow | handle=${win6916} | 
    self.vars["win6916"] = self.wait_for_window(2000)
    # 9 | close |  | 
    self.driver.switch_to.window(self.vars["win6916"])
    self.driver.find_element(By.ID, "kundo-knowledge-embed").click()
    self.driver.close()
  
  def test_ppetider(self):
    # Test name: Öppetider
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.sfbok.se/")
    # 2 | setWindowSize | 796x816 | 
    self.driver.set_window_size(796, 816)
    # 3 | assertText | css=#store-bar > .container |           Stockholm\n          Göteborg\n          Malmö\n         Idag\n10:00-19:00\nImorgon\n10:00-19:00\nÖppettider och adresser
    assert self.driver.find_element(By.CSS_SELECTOR, "#store-bar > .container").text == "          Stockholm\\\\n          Göteborg\\\\n          Malmö\\\\n         Idag\\\\n10:00-19:00\\\\nImorgon\\\\n10:00-19:00\\\\nÖppettider och adresser"
    # 4 | click | linkText=Öppettider och adresser | 
    self.driver.find_element(By.LINK_TEXT, "Öppettider och adresser").click()
    # 5 | click | css=.views-row-1 p:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".views-row-1 p:nth-child(2)").click()
    # 6 | assertText | css=.views-row-1 p:nth-child(2) | Ordinarie öppettider:\nmån–fre 10:00–19:00\nlör 10:00–18:00\nsön 12:00–17:00
    assert self.driver.find_element(By.CSS_SELECTOR, ".views-row-1 p:nth-child(2)").text == "Ordinarie öppettider:\\\\nmån–fre 10:00–19:00\\\\nlör 10:00–18:00\\\\nsön 12:00–17:00"
    # 7 | click | linkText=Stockholmsbutiken | 
    self.driver.find_element(By.LINK_TEXT, "Stockholmsbutiken").click()
    # 8 | click | css=p:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)").click()
    # 9 | assertText | css=p:nth-child(2) | Ordinarie öppettider:\nmån–fre 10:00–19:00\nlör 10:00–18:00\nsön 12:00–17:00
    assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)").text == "Ordinarie öppettider:\\\\nmån–fre 10:00–19:00\\\\nlör 10:00–18:00\\\\nsön 12:00–17:00"
    # 10 | close |  | 
    self.driver.close()