from selenium import webdriver
from shared.Constants import Constants

class FootlooseWebDriver(object):

    def __init__(self):
        if Constants.browser == "chrome":
            self.driver =  webdriver.Chrome(executable_path = Constants.chromedriverpath)
        else:
            self.driver = webdriver.Firefox()

        self.driver.get(Constants.url)

    def get_driver(self):
        return self.driver
