from base_page import BasePage
from locators import CampaignPageLocators


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    def create_campaign(self):
        self.click(self.locators.LOGIN_BTN_SIGN_IN)
        email = self.find(self.locators.EMAIL_FIELD)
        email.clear()
        email.send_keys('Tommy58rus@gmail.com')
        password = self.find(self.locators.PASSWORD_FIELD)
        password.clear()
        password.send_keys('hqEm6g-8pVDhPvc')
        self.click(self.locators.MODAL_BTN)
        self.click(self.locators.CAMPAIGN_CREATE_LOCATOR)
        self.click(self.locators.CAMPAIGN_TRAFFIC_LOCATOR)
        campaign_url = self.find(self.locators.CAMPAIGN_URL_LOCATOR)
        campaign_url.clear()
        campaign_url.send_keys('https://target.my.com')
        campaign_name = self.find(self.locators.CAMPAIGN_NAME_LOCATOR)
        campaign_name.clear()
        campaign_name.send_keys('Test_campaign')
        self.click(self.locators.CAMPAIGN_INTEREST_LOCATOR)
        self.click(self.locators.CAMPAIGN_INTEREST_LOCATOR_2)
        self.click(self.locators.CAMPAIGN_BANNER_FORMAT_LOCATOR)
        upload_image = self.find(self.locators.CAMPAIGN_IMAGE_UPLOAD_BUTTON_LOCATOR)
        upload_image.send_keys(r"C:\Users\Ekaterina\Desktop\Shrek.jpg")
        self.click(self.locators.CAMPAIGN_IMAGE_CROPPER_BUTTON_LOCATOR)
        self.click(self.locators.CAMPAIGN_BANNER_SUBMIT_BUTTON_LOCATOR)
        self.click(self.locators.CAMPAIGN_SUBMIT_BUTTON_LOCATOR)
        self.find(self.locators.CAMPAIGN_LIST_LOCATOR)

    def delete_campaign(self):
        self.click(self.locators.CAMPAIGN_DELETE_LOCATOR)
        self.click(self.locators.CAMPAIGN_DELETE_LOCATOR_2)









