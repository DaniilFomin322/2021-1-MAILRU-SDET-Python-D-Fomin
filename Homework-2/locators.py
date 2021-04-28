from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginLocators(BasePageLocators):
    LOGIN_BTN_SIGN_IN = (By.XPATH, "//div[contains(@class, 'responseHead-module-button') and text()='Войти']")
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    MODAL_BTN = (By.XPATH, "//div[contains(@class, 'authForm-module-button') and text()='Войти']")


class LoginPageLocators(LoginLocators):
    ERROR_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-notify')]/div[contains(@class, "
                               "'notify-module-notifyBlock-')]")
    ERROR_PASSWORD_LOCATOR = (
        By.XPATH, "//div[contains(@class, 'formMsg_text') and text()='Invalid login or password']")


class CampaignPageLocators(LoginLocators):
    CAMPAIGN_CREATE_LOCATOR = (By.XPATH, "//div[text()='Создать кампанию']")
    CAMPAIGN_PRICE_PER_CLICK_LOCATOR = (By.XPATH, "input[contains(@class, 'input__inp js-price-slider-input')]")
    CAMPAIGN_TRAFFIC_LOCATOR = (By.CLASS_NAME, 'column-list-item._traffic')
    CAMPAIGN_URL_LOCATOR = (By.XPATH, "//input[contains(@placeholder, 'Введите ссылку')]")
    CAMPAIGN_NAME_LOCATOR = (By.XPATH, "//input[contains(@maxlength, '255')]")
    CAMPAIGN_INTEREST_LOCATOR = (By.XPATH, "//div[contains(@data-scroll-name, 'setting-interests_soc_dem')]")
    CAMPAIGN_INTEREST_LOCATOR_2 = (By.XPATH, "//label[contains(@title, 'Родители детей')]")
    CAMPAIGN_BANNER_FORMAT_LOCATOR = (By.ID, "patterns_4")
    CAMPAIGN_IMAGE_UPLOAD_BUTTON_LOCATOR = (
    By.XPATH, "//div[contains(@class, 'upload-module-wrapper')]/input[@type='file']")
    CAMPAIGN_IMAGE_CROPPER_BUTTON_LOCATOR = (By.CLASS_NAME, 'image-cropper__save.js-save')
    CAMPAIGN_BANNER_SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//div[@data-test='submit_banner_button']")
    CAMPAIGN_SUBMIT_BUTTON_LOCATOR = (By.CLASS_NAME, 'footer__button.js-save-button-wrap')
    CAMPAIGN_LIST_LOCATOR = (By.XPATH, "//a[@title='Test_campaign']")
    CAMPAIGN_DELETE_LOCATOR = (By.XPATH,
                               "//div[contains(@class, 'main-module-Cell-Z2qWrE')]/div[contains(@class, 'settingsCell-module-settingsCellWrap')]/div[contains(@class, 'icon-settings')]")
    CAMPAIGN_DELETE_LOCATOR_2 = (By.XPATH, "//li[@title='Удалить']")
