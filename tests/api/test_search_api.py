import pytest

@pytest.mark.api
def test_search_status_code(search_api, test_author):
    response = search_api.search_products(test_author)

    print(f"\nResponse status: {response.status_code}")
    print(f"\nResponse URL: {response.url}")

    assert response.status_code in [200, 301, 302, 404], \
        f"Unexpected status: {response.status_code}"

@pytest.mark.api
def test_search_content_type(search_api, test_author):
    response = search_api.search_products(test_author)

    content_type = response.headers.get("Content-Type", "")
    print(f"\n📊 Content-Type: {content_type}")

    assert content_type != "", "Content-Type is empty"
