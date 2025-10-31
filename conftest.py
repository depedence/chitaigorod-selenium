import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from config.config import config

def get_chrome_options():
    """ Chrome settings """
    options = Options()

    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')

    prefs = {
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.media_stream": 2,
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 2,
        "profile.default_content_setting_values.ppapi_broker": 2,
        "profile.default_content_setting_values.automatic_downloads": 2
    }
    options.add_experimental_option("prefs", prefs)

    # Headless
    if config.HEADLESS:
        options.add_argument('--headless=new')

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    return options

@pytest.fixture(scope='function')
def driver():
    """ WebDriver fixture """
    options = get_chrome_options()
    driver = webdriver.Chrome(options=options)

    # Timeout settings
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)

    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
            '''
    })

    driver.get(config.BASE_URL)

    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )

    # Local Storage
    driver.execute_script('window.localStorage.setItem("chg_user_location","true");')
    driver.execute_script('window.localStorage.setItem("chg_is_adult_confirmed","true");')

    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture(scope='function', autouse=True)
def log_test_info(request):
    """ Auto log test """
    print(f"\n{'-' * 80}")
    print(f"Starting test: {request.node.name}")
    print(f"{'-' * 80}")

    yield

    print(f"\n{'-' * 80}")
    print(f"Finished test: {request.node.name}")
    print(f"{'-' * 80}")