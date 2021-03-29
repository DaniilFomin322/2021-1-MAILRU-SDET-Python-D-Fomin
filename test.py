import pytest
import time


@pytest.mark.UI
def test_login(browser):
    browser.get('https://target.my.com/')
    time.sleep(2)
    element = browser.find_element_by_class_name('responseHead-module-button-1BMAy4')
    element.click()
    time.sleep(2)
    email = browser.find_element_by_class_name('authForm-module-input-9t5W5U.input-module-input-1xGLR8')
    email.clear()
    email.send_keys('tommy58rus@gmail.com')
    time.sleep(2)
    password = browser.find_element_by_class_name('authForm-module-inputPassword-2Atq4Q.input-module-input-1xGLR8')
    password.clear()
    password.send_keys('hqEm6g-8pVDhPvc')
    login = browser.find_element_by_class_name('authForm-module-button-2G6lZu')
    login.click()
    after_login_url = browser.current_url
    expected_after_login_url = "https://target.my.com/dashboard"
    assert after_login_url == expected_after_login_url


@pytest.mark.UI
def test_logout(browser):
    browser.get('https://target.my.com/')
    time.sleep(2)
    element = browser.find_element_by_class_name('responseHead-module-button-1BMAy4')
    element.click()
    time.sleep(2)
    email = browser.find_element_by_class_name('authForm-module-input-9t5W5U.input-module-input-1xGLR8')
    email.clear()
    email.send_keys('tommy58rus@gmail.com')
    time.sleep(2)
    password = browser.find_element_by_class_name('authForm-module-inputPassword-2Atq4Q.input-module-input-1xGLR8')
    password.clear()
    password.send_keys('hqEm6g-8pVDhPvc')
    login = browser.find_element_by_class_name('authForm-module-button-2G6lZu')
    login.click()
    time.sleep(2)
    profile = browser.find_element_by_class_name('right-module-userNameWrap-34ibLS')
    profile.click()
    time.sleep(2)
    logout = browser.find_elements_by_class_name('rightMenu-module-rightMenuItem-2BKs3G')[1]
    logout.click()
    time.sleep(2)
    after_logout_url = browser.current_url
    expected_after_logout_url = "https://target.my.com/"
    assert after_logout_url == expected_after_logout_url


@pytest.mark.UI
def test_edit(browser):
    browser.get('https://target.my.com/')
    browser.set_window_size(1600, 1200)
    time.sleep(2)
    element = browser.find_element_by_class_name('responseHead-module-button-1BMAy4')
    element.click()
    time.sleep(2)
    email = browser.find_element_by_class_name('authForm-module-input-9t5W5U.input-module-input-1xGLR8')
    email.clear()
    email.send_keys('tommy58rus@gmail.com')
    time.sleep(2)
    password = browser.find_element_by_class_name('authForm-module-inputPassword-2Atq4Q.input-module-input-1xGLR8')
    password.clear()
    password.send_keys('hqEm6g-8pVDhPvc')
    login = browser.find_element_by_class_name('authForm-module-button-2G6lZu')
    login.click()
    time.sleep(2)
    profile_info = browser.find_elements_by_class_name('center-module-buttonWrap-D2syOt')[5]
    profile_info.click()
    time.sleep(2)
    fio = browser.find_elements_by_class_name('input__inp.js-form-element')[0]
    fio.clear()
    fio.send_keys('Жмышенко Валерий Альбертович')
    phone = browser.find_elements_by_class_name('input__inp.js-form-element')[1]
    phone.clear()
    phone.send_keys('79252281488')
    contact_email = browser.find_elements_by_class_name('input__inp.js-form-element')[2]
    contact_email.clear()
    contact_email.send_keys('test@test.ru')
    save_button = browser.find_element_by_class_name('button.button_submit')
    save_button.click()
    time.sleep(1)
    assert browser.find_element_by_class_name('_notification._notification_success-bg.js-group-form-success-bg')


@pytest.mark.parametrize(
    'link',
    [
                    'https://target.my.com/segments/segments_list',
                    'https://target.my.com/billing#deposit'
        ]
            )
def test_check_pages(browser,link):
    browser.get('https://target.my.com/')
    browser.set_window_size(1600, 1200)
    time.sleep(2)
    element = browser.find_element_by_class_name('responseHead-module-button-1BMAy4')
    element.click()
    time.sleep(2)
    email = browser.find_element_by_class_name('authForm-module-input-9t5W5U.input-module-input-1xGLR8')
    email.clear()
    email.send_keys('tommy58rus@gmail.com')
    time.sleep(2)
    password = browser.find_element_by_class_name('authForm-module-inputPassword-2Atq4Q.input-module-input-1xGLR8')
    password.clear()
    password.send_keys('hqEm6g-8pVDhPvc')
    login = browser.find_element_by_class_name('authForm-module-button-2G6lZu')
    login.click()
    time.sleep(2)
    page_second = browser.find_element_by_class_name('center-module-button-cQDNvq.center-module-segments-3y1hDo')
    page_second.click()
    second_page = browser.current_url
    expected_second_page = "https://target.my.com/segments/segments_list"
    assert second_page == expected_second_page
    time.sleep(1)
    page_third = browser.find_element_by_class_name('center-module-button-cQDNvq.center-module-billing-x3wyL6')
    page_third.click()
    time.sleep(2)
    third_page = browser.current_url
    expected_third_page = "https://target.my.com/billing#deposit"
    assert third_page == expected_third_page
