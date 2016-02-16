from nose.tools import assert_equal
import time

from shared.FootlooseWebDriver import FootlooseWebDriver
from pages.LogonPage import LogonPage
from pages.MainPage import MainPage
from shared.Constants import Constants

class Test_Automation_Login:

    def setUp(self):
        self.driver = FootlooseWebDriver().get_driver()

    def test_login_failed(self):
        """
        Tests a failed login attempt
        """

        #Load the logon page.
        login_page = LogonPage(self.driver)
        login_page.wait_for_load()

        #Pass in a bogus username and password
        login_page.username().set_value("bogususername")
        login_page.password().set_value("boguspassword")

        #Attempt to login
        login_page.click_submit_button()

        #Wait for 10 seconds for the server to respond to the login attempt
        time.sleep(10)

        #Get the error message
        error_message = login_page.get_error_message()

        assert_equal(error_message, "The username and password combination is not correct")

    def test_successful_login(self):
        """
        Tests a successful login attempt
        """

        #Load the logon page.
        login_page = LogonPage(self.driver)
        login_page.wait_for_load()

        #Pass in a bogus username and password
        login_page.username().set_value(Constants.testusername)
        login_page.password().set_value(Constants.testpassword)

        #Attempt to login
        login_page.click_submit_button()

        #Verify the main page is loaded and the welcome message
        main_page = MainPage(self.driver)
        main_page.wait_for_load()

        welcome_message = main_page.get_welcome_message()

        assert_equal(welcome_message, "Welcome, Art Venere")

    def tearDown(self):
        self.driver.close()

