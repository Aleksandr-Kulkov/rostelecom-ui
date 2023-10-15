from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_USERNAME = (By.ID, 'username')
    AUTH_PASS = (By.ID, 'password')
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_HEADER = (By.XPATH, '//h1[@class="card-container__title"]')
    AUTH_TAB = (By.XPATH, '//input[@name="tab_type"]')
    AUTH_TAB_PHONE = (By.ID, 't-btn-tab-phone')
    AUTH_TAB_EMAIL = (By.ID, 't-btn-tab-mail')
    AUTH_TAB_LOGIN = (By.ID, 't-btn-tab-login')
