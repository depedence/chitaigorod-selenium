""" Project configuration """
import os


class Config:
    """ Base config """

    # base url
    BASE_URL = 'https://www.chitai-gorod.ru'

    # browser
    BROWSER = 'chrome'
    IS_CI = os.getenv('CI') == 'true'
    HEADLESS = IS_CI
    WINDOW_SIZE = "1920,1080"

    # timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    PAGE_LOAD_TIMEOUT = 30
    API_TIMEOUT = 10

    # paths
    SCREENSHOTS = 'screenshots'
    REPORTS_PATH = 'reports'

    # api headers
    API_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.chitai-gorod.ru/",
        "Origin": "https://www.chitai-gorod.ru",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }

config = Config()
