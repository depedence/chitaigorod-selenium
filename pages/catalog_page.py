from pages.base_page import BasePage
from selenium.webdriver.common.by import By as by

class CatalogPage(BasePage):
    PATH = '/'

    # Locators
    catalog_btn = (by.CSS_SELECTOR, '.header-sticky__catalog button')
    catalog_menu = (by.CLASS_NAME, 'categories-menu')

    supplies_for_artists = (by.NAME, 'Товары для художников')
    paints = (by.NAME, 'Краски')
    gouache = (by.NAME, 'Гуашь')
    gouache_header = (by.CLASS_NAME, 'global-left-right-indent app-catalog__header')

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