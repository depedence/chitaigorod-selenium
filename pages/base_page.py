from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config.config import config

class BasePage:
    """ Base Page for other Page Object Model """

    def __init__(self, driver, base_url = config.BASE_URL, timeout=None):
        self.driver = driver
        self.base_url = base_url.rstrip('/')
        self.wait = WebDriverWait(driver, timeout or config.EXPLICIT_WAIT)

    def open(self, path = '/'):
        url = self.base_url + ('' if path.startswith('/') else '/') + path
        self.driver.get(url)

    def click(self, locator):
        """ Wait to be clickable and click """
        element = self.wait.until(ec.element_to_be_clickable(locator))

        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click()', element)
            print(f'LOG: Element {locator} was clicked from JavaScript')

    def type(self, locator, text, clear: bool = True):
        el = self.wait.until(ec.visibility_of_element_located(locator))

        if clear:
            el.clear()

        el.send_keys(text)
        return el

    def is_visible(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))

    def is_not_visible(self, locator):
        self.wait.until(ec.invisibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text