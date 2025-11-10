from api.base_api import BaseAPI

class SearchAPI(BaseAPI):
    def search_products(self, query: str):
        possible_endpoints = [
            "/api/v2/search/product",
            "/api/v1/search",
            "/search/api",
            "/api/search"
        ]

        params = {'phrase': query}

        endpoint = possible_endpoints[0]

        return self.get(endpoint, params=params)
