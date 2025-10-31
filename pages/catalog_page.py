from pages.base_page import BasePage
from selenium.webdriver.common.by import By as by

class CatalogPage(BasePage):
    PATH = '/'

    # Locators
    welcome_modal = (by.CLASS_NAME, 'tippy-box')
    close_welcome_modal_btn = (by.CSS_SELECTOR, '.tippy-content .chg-app-button--breeze')

    catalog_btn = (by.CSS_SELECTOR, '.header-sticky__catalog button')
    catalog_menu = (by.CLASS_NAME, 'categories-menu')

    supplies_for_artists = (by.XPATH, '//span[text()="Товары для художников"]')
    paints = (by.XPATH, '//span[text()="Краски"]')
    gouache = (by.XPATH, '//span[text()="Гуашь"]')
    gouache_header = (by.CSS_SELECTOR, '.global-left-right-indent.app-catalog__header')

    # Actions
    def open_catalog(self):
        self.open(self.PATH)

    # Suites
    def open_and_check_catalog(self):
        self.click(self.catalog_btn)
        self.is_visible(self.catalog_menu)

    def catalog_is_working(self):
        self.open_and_check_catalog()

        self.click(self.supplies_for_artists)
        self.click(self.paints)
        self.click(self.gouache)

        self.is_visible(self.gouache_header)