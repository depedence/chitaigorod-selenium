from pages.base_page import BasePage
from selenium.webdriver.common.by import By as by

class MenuPage(BasePage):
    PATH = '/'

    # Locators
    certificate_menu = (by.NAME, 'Сертификаты')
    certificate_page = (by.CLASS_NAME, 'certificate-page')

    bonusProgram_menu = (by.NAME, 'Программа лояльности')
    bonusProgram_page = (by.CLASS_NAME, 'bonus-program-page')

    sale_menu = (by.NAME, 'Распродажа')
    sale_page = (by.CLASS_NAME, 'app-wrapper__content')

    # Actions
    def open_menu(self):
        self.open(self.PATH)

    # Suites
    def certificate_check(self):
        self.click(self.certificate_menu)
        self.is_visible(self.certificate_page)

    def bonusProgram_check(self):
        self.click(self.bonusProgram_menu)
        self.is_visible(self.bonusProgram_page)

    def sale_check(self):
        self.click(self.bonusProgram_menu)
        self.is_visible(self.sale_page)