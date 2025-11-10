import pytest
from pages.change_location_page import ChangeLocation

@pytest.mark.ui
@pytest.mark.location
@pytest.mark.smoke
def test_location_moscow(driver):
    page = ChangeLocation(driver)

    page.open_location()

    page.check_location('Москва')

@pytest.mark.ui
@pytest.mark.location
@pytest.mark.smoke
def test_change_location_to_kazan(driver):
    page = ChangeLocation(driver)

    page.open_location()

    page.change_location('Казань')
