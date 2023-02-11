from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger


class LoginPage(BasePage):
    EMAIL_INPUT_BY = (By.CSS_SELECTOR, "input#name")
    PASSWORD_INPUT_BY = (By.CSS_SELECTOR, "input#password")
    SUBMIT_BUTTON_BY = (By.CSS_SELECTOR, "button#button_primary")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_email(self, user_email):
        Logger.log('fill_email(' + user_email + ')')
        self.do_send_keys(self.EMAIL_INPUT_BY, user_email)

    def fill_password(self, user_password):
        Logger.log('fill_password(' + user_password + ')')
        self.do_send_keys(self.PASSWORD_INPUT_BY, user_password)

    def click_submit(self):
        Logger.log('click_submit()')
        self.do_click(self.SUBMIT_BUTTON_BY)
