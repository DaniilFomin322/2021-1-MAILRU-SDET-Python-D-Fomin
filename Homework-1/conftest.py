import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {'https://target.my.com/': url}


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(r'/chromedriver.exe')
    browser.get('https://target.my.com/')
    browser.set_window_size(1600, 1200)
    yield browser
    print("\nquit browser..")
    browser.quit()


def login(browser):
    time.sleep(2)
    browser.find_element_by_xpath("//div[contains(@class, 'responseHead-module-button') and text()='Войти']").click()
    time.sleep(2)
    email= browser.find_element_by_name('email')
    email.clear()
    email.send_keys('tommy58rus@gmail.com')
    time.sleep(2)
    password = browser.find_element_by_name('password')
    password.clear()
    password.send_keys('hqEm6g-8pVDhPvc')
    browser.find_element_by_xpath("//div[contains(@class, 'authForm-module-button') and text()='Войти']").click()
