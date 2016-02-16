from nose.tools import assert_equal

import time
import random
from shared.FootlooseWebDriver import FootlooseWebDriver
from pages.LogonPage import LogonPage
from pages.MainPage import MainPage
from pages.ContactInformationPage import ContactInformationPage


class TestUIAutomation_ContactInformationPageTests:

    def setUp(self):
        self.driver = FootlooseWebDriver().get_driver()
        LogonPage(self.driver).login_in()

    def test_edit_and_save_home_address(self):
        streetaddress = random.randint()
        MainPage(self.driver).navigate_to_contact_information()

        contact_info_page = ContactInformationPage(self.driver)
        contact_info_page.wait_for_load()
        contact_info_page.edit_home_address()
        contact_info_page.home_streetaddress().set_value("123 Anywhere")

        time.sleep(5)

