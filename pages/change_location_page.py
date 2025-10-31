from pages.base_page import BasePage
from selenium.webdriver.common.by import By as by

class ChangeLocation(BasePage):
    PATH = '/'

    # Locators
    header_location = (by.CLASS_NAME, 'header-location')
    change_location_btn = (by.CSS_SELECTOR, '.chg-app-button.chg-app-button--secondary.chg-app-button--l')
    change_modal = (by.CLASS_NAME, 'ui-modal__slot-wrapper')
    location = (by.XPATH, '//button[text()="Казань"]')

    # Actions
    def open_location(self):
        self.open(self.PATH)

    # Suites
    def check_location(self, location):
        header = self.get_text(self.header_location)
        print(f'LOG: Location is {header}')

        assert location in header

    def change_location(self, location):
        self.click(self.header_location)
        self.click(self.change_location_btn)

        self.is_visible(self.change_modal)
        self.click(self.location)

        self.is_not_visible(self.change_modal)
        self.check_location(location)