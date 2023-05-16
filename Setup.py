import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
chromedriver = "C:\Program Files (x86)\chromedriver.exe"
s = Service(chromedriver)
driver = webdriver.Chrome(service=s)

driver.get("https://www.sfbok.se/")
print(driver.title)
driver.quit()