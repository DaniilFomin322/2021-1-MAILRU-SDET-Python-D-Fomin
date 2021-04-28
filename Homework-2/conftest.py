from fixtures import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome")
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--debug_log', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}


@pytest.fixture(scope="function")
def driver(config):
    print("\nstart chrome browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(config['url'])
    browser.set_window_size(1600, 1200)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
