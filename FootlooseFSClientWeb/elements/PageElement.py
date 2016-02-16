class PageElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def get_value(self):
        element = self.driver.find_element_by_id(self.locator)
        return element.get_attribute("value")

    def set_value(self, value):
        element = self.driver.find_element_by_id(self.locator)
        element.send_keys(value)
