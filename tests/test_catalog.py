import pytest
from pages.catalog_page import CatalogPage

@pytest.mark.catalog
@pytest.mark.smoke
def test_catalog_is_visible(driver):
    page = CatalogPage(driver)

    page.open_catalog()

    page.open_and_check_catalog()

@pytest.mark.catalog
@pytest.mark.smoke
def test_catalog_is_working(driver):
    page = CatalogPage(driver)

    page.open_catalog()

    page.catalog_is_working()