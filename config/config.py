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

    # paths
    SCREENSHOTS = 'screenshots'
    REPORTS_PATH = 'reports'

config = Config()