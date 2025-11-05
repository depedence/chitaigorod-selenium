import pytest
from pages.catalog_page import CatalogPage

def test_environment_info(driver):
    print(f"User Agent: {driver.execute_script('return navigator.userAgent')}")
    print(f"Window Size: {driver.get_window_size()}")
    print(f"Page Load Strategy: {driver.capabilities['pageLoadStrategy']}")

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
