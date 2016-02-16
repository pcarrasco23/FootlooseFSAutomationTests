from pages.BasePage import BasePage
from shared.Constants import Constants
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):

    contact_information_anchor_xpath = "//a[@href='#/contactinfo']"

    def __init(self, driver):
        BasePage.__init__(self, driver)

    def wait_for_load(self):
         WebDriverWait(self.driver, Constants.default_wait).until(
            lambda driver: driver.find_element_by_class_name("body-content"))

    def get_welcome_message(self):
        WebDriverWait(self.driver, Constants.default_wait).until(
            lambda driver: driver.find_element_by_tag_name("h2"))
        element = self.driver.find_element_by_tag_name("h2")
        return element.text

    def navigate_to_contact_information(self):
        element = self.driver.find_element_by_xpath(self.contact_information_anchor_xpath)
        element.click();
