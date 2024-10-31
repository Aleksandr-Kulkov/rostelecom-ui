from graduatework.pages.base_page import BasePage
from graduatework.pages.locators import AuthLocators
from graduatework.settings import auth_page_url
import time


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = auth_page_url
        driver.get(url)
        # Создание нужных элементов
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.header = driver.find_element(*AuthLocators.AUTH_HEADER)
        self.tab = driver.find_element(*AuthLocators.AUTH_TAB)
        self.tab_phone = driver.find_element(*AuthLocators.AUTH_TAB_PHONE)
        self.tab_email = driver.find_element(*AuthLocators.AUTH_TAB_EMAIL)
        self.tab_login = driver.find_element(*AuthLocators.AUTH_TAB_LOGIN)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()
        time.sleep(3)

    def header_click(self):
        self.header.click()

    def tab_phone_click(self):
        self.tab_phone.click()

    def tab_email_click(self):
        self.tab_email.click()

    def tab_login_click(self):
        self.tab_login.click()
