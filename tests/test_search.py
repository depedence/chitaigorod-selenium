import pytest
from pages.search_page import SearchPage

@pytest.mark.ui
@pytest.mark.search
@pytest.mark.smoke
def test_search_product(driver):
    page = SearchPage(driver)

    page.open_search()
    page.type_author()
    page.get_first_block_attribute()
    page.add_product_to_cart()

@pytest.mark.ui
@pytest.mark.search
@pytest.mark.smoke
def test_cart(driver):
    page = SearchPage(driver)

    page.open_search()
    page.type_author()

    page.add_product_to_cart()

    page.delete_product_from_cart()
