from nose.tools import assert_equal

from shared.FootlooseWebDriver import FootlooseWebDriver
from pages.LogonPage import LogonPage
from pages.AccountsPage import AccountsPage

class Test_Automation_AccountPage:

    def setUp(self):
        self.driver = FootlooseWebDriver().get_driver()

        # All test require successful login attempt
        LogonPage(self.driver).login_in()

    def test_account_and_transaction_grids_load(self):
        """
        Tests a successful login attempt
        """

        accounts_page = AccountsPage(self.driver)
        accounts_page.wait_for_load()

        assert_equal(accounts_page.has_account_table(), True)
        assert_equal(accounts_page.has_transaction_table(), True)

    def tearDown(self):
        self.driver.close()

