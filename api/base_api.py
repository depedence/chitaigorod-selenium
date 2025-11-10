import requests
from typing import Optional, Dict
from config.config import config

class BaseAPI:
    """ Base class for API requests """

    def __init__(self):
        self.base_url = config.BASE_URL
        self.timeout = config.API_TIMEOUT
        self.session = requests.Session()
        self.session.headers.update(config.API_HEADERS)

    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        url = f'{self.base_url}{endpoint}'
        print(f'\n GET {url}')

        if params:
            print(f'Params: {params}')

        response = self.session.get(url, params=params, timeout=self.timeout)
        print(f'Status: {response.status_code}')

        return response

    def post(self, endpoint: str, json: Optional[Dict] = None) -> requests.Response:
        url = f'{self.base_url}{endpoint}'
        print(f'\n POST {url}')

        if json:
            print(f' JSON: {json}')

        response = self.session.post(url, json=json, timeout=self.timeout)
        print(f'Status: {response.status_code}')

        return response

    def close(self):
        self.session.close()
