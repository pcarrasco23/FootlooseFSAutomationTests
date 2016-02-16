import time

from pages.BasePage import BasePage
from elements.PageElement import PageElement
from shared.Constants import Constants
from selenium.webdriver.support.ui import WebDriverWait


class LogonPage(BasePage):

    submit_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def wait_for_load(self):
        WebDriverWait(self.driver, Constants.default_wait).until(lambda driver: driver.find_element_by_xpath(self.submit_button_xpath))

    def username(self):
        return PageElement(self.driver, "username")

    def password(self):
        return PageElement(self.driver, "password")

    def click_submit_button(self):
        element = self.driver.find_element_by_xpath(self.submit_button_xpath)
        element.click()

    def get_error_message(self):
        element = self.driver.find_element_by_id("error_message")
        return element.text

    def login_in(self):
        self.wait_for_load()
        self.username().set_value(Constants.testusername)
        self.password().set_value(Constants.testpassword)
        self.click_submit_button()
        time.sleep(10)

