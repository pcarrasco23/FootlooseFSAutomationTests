from selenium.webdriver.support.ui import WebDriverWait
from pages.MainPage import MainPage
from shared.Constants import Constants
from elements.PageElement import PageElement

class ContactInformationPage(MainPage):

    home_address_edit_button_xpath = "//form[@id='Home_address_form']/div/div[@class='editablebuttons']/button[@class='btn btn-primary btn-xs']"

    def __init(self, driver):
        MainPage.__init__(self, driver)

    def wait_for_load(self):
         WebDriverWait(self.driver, Constants.default_wait).until(
            lambda driver: driver.find_element_by_class_name("contactinfo"))

    def home_streetaddress(self):
        return PageElement(self.driver, "Home_streetaddress")

    def home_city(self):
        return PageElement(self.driver, "Home_city")

    def home_state(self):
        return PageElement(self.driver, "Home_state")

    def home_zip(self):
        return PageElement(self.driver, "Home_zip")

    def edit_home_address(self):
        home_address_edit_button = self.driver.find_element_by_xpath(self.home_address_edit_button_xpath)
        home_address_edit_button.click()


