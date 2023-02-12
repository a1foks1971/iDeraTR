from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger


class Top(BasePage):
    USER_LOGGED_IN_BY = (By.CSS_SELECTOR, "#navigation-user .navigation-username")

    def __init__(self, driver):
        super().__init__(driver)

    def get_user_full_name(self):
        usr = self.get_text(self.USER_LOGGED_IN_BY)
        Logger.log('get_user_full_name() : "'+usr+'"')
        return usr
