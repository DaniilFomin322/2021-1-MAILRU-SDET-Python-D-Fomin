import pytest
import time
import conftest


@pytest.mark.UI
def test_login(browser):
    conftest.login(browser)
    after_login_url = browser.current_url
    expected_after_login_url = "https://target.my.com/dashboard"
    assert after_login_url == expected_after_login_url


@pytest.mark.UI
def test_logout(browser):
    conftest.login(browser)
    time.sleep(2)
    browser.find_element_by_xpath("//div[contains(@class, 'right-module-userNameWrap')]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//a[contains(@class, 'rightMenu-module-rightMenuLink') and text()='Выйти']").click()
    time.sleep(2)
    after_logout_url = browser.current_url
    expected_after_logout_url = "https://target.my.com/"
    assert after_logout_url == expected_after_logout_url


@pytest.mark.UI
def test_edit(browser):
    conftest.login(browser)
    time.sleep(2)
    browser.find_element_by_xpath("//a[contains(@href, 'profile')]").click()
    time.sleep(2)
    fio = browser.find_element_by_xpath("//div[@data-name='fio']/div[@class='input__wrap']/input[@type='text']")
    fio.clear()
    fio.send_keys('Жмышенко Валерий Альбертович')

    phone = browser.find_element_by_xpath("//div[@data-name='phone']/div[@class='input__wrap']/input[@type='text']")
    phone.clear()
    phone.send_keys('79252281488')

    contact_email = browser.find_element_by_xpath(
        "//div[@cid='view216']/div[@class='input__wrap']/input[@type='text']")
    contact_email.clear()
    contact_email.send_keys('test@test.ru')
    save_button = browser.find_element_by_class_name('button__text')
    save_button.click()
    time.sleep(3)
    assert browser.find_element_by_class_name('_notification._notification_success-bg.js-group-form-success-bg')


@pytest.mark.parametrize(
    'link',
    [
                    'https://target.my.com/segments/segments_list',
                    'https://target.my.com/billing#deposit'
        ]
            )
def test_check_pages(browser, link):
    conftest.login(browser)
    time.sleep(2)
    browser.find_element_by_xpath("//a[contains(@href, 'segments')]").click()
    time.sleep(2)
    assert browser.current_url == "https://target.my.com/segments/segments_list"
    time.sleep(1)
    browser.find_element_by_xpath("//a[contains(@href, 'billing')]").click()
    time.sleep(2)
    assert browser.current_url == "https://target.my.com/billing#deposit"
