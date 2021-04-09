import pytest
from base import BaseCase
from login_page import LoginPage
from campaign_page import CampaignPage


class TestOne(BaseCase):
    @pytest.mark.UI
    def test_negative_login_invalid_email(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_invalid_email()
        assert "Введите email или телефон" in self.driver.page_source

    @pytest.mark.UI
    def test_negative_login_invalid_password(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_invalid_password()
        assert "Invalid login or password" in self.driver.page_source

    @pytest.mark.UI
    def test_campaign_create(self):
        self.campaign_page = CampaignPage(self.driver)
        self.campaign_page.create_campaign()
        assert "Test_campaign" in self.driver.page_source
        self.campaign_page.delete_campaign()
