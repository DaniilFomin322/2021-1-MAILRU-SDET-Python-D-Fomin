import pytest
from _pytest.fixtures import FixtureRequest
from base_page import BasePage
from login_page import LoginPage
from campaign_page import CampaignPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.campaign_page: CampaignPage = request.getfixturevalue('campaign_page')
