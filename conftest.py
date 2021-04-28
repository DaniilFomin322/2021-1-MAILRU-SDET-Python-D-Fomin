from fixtures import *
import pytest
from selenium import webdriver


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
    browser = webdriver.Chrome(
        executable_path=r'C:\Users\Ekaterina\PycharmProjects\2021-1-MAILRU-SDET-Python-D-Fomin\chromedriver.exe',
        options=options)
    browser.get(config['url'])
    browser.set_window_size(1600, 1200)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(r'C:\Users\Ekaterina\PycharmProjects\pythonProject\lection\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()