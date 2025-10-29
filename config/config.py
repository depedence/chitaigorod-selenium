""" Project configuration """

class Config:
    """ Base config """

    # base url
    BASE_URL = 'https://www.chitai-gorod.ru'

    # browser
    BROWSER = 'chrome'
    HEADLESS = False
    WINDOW_SIZE = "1920,1080"

    # timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    PAGE_LOAD_TIMEOUT = 30

    # paths
    SCREENSHOTS = 'screenshots'
    REPORTS_PATH = 'reports'

config = Config()