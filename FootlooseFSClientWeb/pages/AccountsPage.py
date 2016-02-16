from pages.MainPage import MainPage
from shared.Constants import Constants
from selenium.webdriver.support.ui import WebDriverWait


class AccountsPage(MainPage):

    def __init(self, driver):
        MainPage.__init__(self, driver)

    def wait_for_load(self):
         WebDriverWait(self.driver, Constants.default_wait).until(
            lambda driver: driver.find_element_by_id("accounttable"))

    def has_account_table(self):
         WebDriverWait(self.driver, Constants.default_wait).until(
            lambda driver: driver.find_element_by_id("accounttable"))
         return True

    def has_transaction_table(self):
         WebDriverWait(self.driver, Constants.default_wait).until(
            lambda driver: driver.find_element_by_id("transactiontable"))
         return True