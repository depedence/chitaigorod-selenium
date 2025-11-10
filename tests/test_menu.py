import pytest
from pages.menu_page import MenuPage

@pytest.mark.ui
@pytest.mark.menu
@pytest.mark.smoke
def test_certificate_menu(driver):
    page = MenuPage(driver)

    page.open_menu()
    page.certificate_check()

@pytest.mark.ui
@pytest.mark.menu
@pytest.mark.smoke
def test_bonusProgram_menu(driver):
    page = MenuPage(driver)

    page.open_menu()
    page.bonusProgram_check()

@pytest.mark.ui
@pytest.mark.menu
@pytest.mark.smoke
def test_sale_menu(driver):
    page = MenuPage(driver)

    page.open_menu()
    page.sale_check()
