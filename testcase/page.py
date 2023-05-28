from locator import *
from element import BasePageElement

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        return "Science" in self.driver.title
    
    def click_nyheter_knapp(self):
        element = self.driver.find_element(*MainPageLocator.NYHET_KNAPP)
        element.click()

class SearchResultsPage(BasePage):

    def is_result_found(self):
        return "No results found." not in self.driver.page_source