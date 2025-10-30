from pages.base_page import BasePage
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys

class SearchPage(BasePage):
    PATH = '/'
    AUTHOR = 'Пелевин'
    PRODUCT_NAME = 'Путешествие в Элевсин'

    # Locators
    search_textbox = (by.CSS_SELECTOR, '.search-form__input')
    search_list = (by.CSS_SELECTOR, '.suggests-list')
    first_block = (by.CSS_SELECTOR, 'article.app-products-list__item:nth-child(1)')
    product_header = (by.CSS_SELECTOR, '.product-detail-page__title')
    buy_btn = (by.CSS_SELECTOR, '.product-buttons__main-action')

    cart = (by.CSS_SELECTOR, 'button.header-controls__btn:nth-child(4)')
    indicator = (by.CSS_SELECTOR, '.chg-indicator')
    delete_btn = (by.CSS_SELECTOR, '.cart-item__delete-button')
    delete_msg = (by.CSS_SELECTOR, '.cart-item-deleted__title')

    # Actions
    def open_search(self):
        self.open(self.PATH)

    def type_author(self):
        element = self.type(self.search_textbox, self.AUTHOR)
        element.send_keys(keys.ENTER)

    def get_first_block_attribute(self):
        info = self.get_text(self.first_block)
        assert self.AUTHOR in info

    def go_to_product(self):
        self.click(self.first_block)

    def get_product_header(self):
        header = self.get_text(self.product_header)
        assert self.PRODUCT_NAME in header

    def tap_buy_button(self):
        self.click(self.buy_btn)

    def indicator_is_visible(self):
        self.is_visible(self.indicator)

    def delete_msg_is_visible(self):
        return self.is_visible(self.delete_msg)

    # Suites
    def add_product_to_cart(self):
        self.go_to_product()
        self.get_product_header()
        self.tap_buy_button()
        self.indicator_is_visible()

    def delete_product_from_cart(self):
        self.click(self.cart)
        self.click(self.delete_btn)
        self.delete_msg_is_visible()