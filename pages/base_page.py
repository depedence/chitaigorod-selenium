from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config.config import config

class BasePage:
    """ Base Page for other Page Object Model """

    def __init__(self, driver, base_url, timeout = 10):
        self.driver = driver
        self.base_url = base_url.rstrip('/')
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path = '/'):
        url = self.base_url + ('' if path.startswith('/') else '/') + path
        self.driver.get(url)

    def click(self, locator):
        """ Wait to be clickable and click """
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def type(self, locator, text, clear: bool = True):
        el = self.wait.until(ec.visibility_of_element_located(locator))

        if clear:
            el.clear()

        el.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text