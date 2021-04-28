from base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):

    locators = LoginPageLocators()

    def login_invalid_email(self):
        self.click(self.locators.LOGIN_BTN_SIGN_IN)
        email = self.find(self.locators.EMAIL_FIELD)
        email.clear()
        email.send_keys('dadadada')
        password = self.find(self.locators.PASSWORD_FIELD)
        password.clear()
        password.send_keys('14882280')
        self.click(self.locators.MODAL_BTN)
        self.find(self.locators.ERROR_LOCATOR)

    def login_invalid_password(self):
        self.click(self.locators.LOGIN_BTN_SIGN_IN)
        email = self.find(self.locators.EMAIL_FIELD)
        email.clear()
        email.send_keys('Tommy58rus@gmail.com')
        password = self.find(self.locators.PASSWORD_FIELD)
        password.clear()
        password.send_keys('14882280')
        self.click(self.locators.MODAL_BTN)
        self.find(self.locators.ERROR_PASSWORD_LOCATOR)
