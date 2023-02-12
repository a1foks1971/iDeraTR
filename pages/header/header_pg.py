from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger


class Header(BasePage):
    EXPECTED_TITLES = {
        "DASHBOARD_MENU": "DASHBOARD",
        "ADMINISTRATION_MENU": "ADMINISTRATION",
    }

    ADMINISTRATION_HTML_LI = (By.CSS_SELECTOR, 'ul.header-menu > li.header-menu-item-right')
    ADMINISTRATION_HTML_A = (By.ID, 'navigation-admin')
    ADMINISTRATION_CSS_SELECTOR = '#navigation-admin'
    DASHBOARD_HTML_LI = (By.CSS_SELECTOR, 'ul.header-menu > li:not(.header-menu-item-right)')
    DASHBOARD_HTML_A = (By.ID, 'navigation-dashboard')
    SELECTED_HTML_LI = (By.CSS_SELECTOR, 'ul.header-menu > li.header-menu-item-selected')

    def __init__(self, driver):
        super().__init__(driver)

    def get_selected_menu_title(self):
        _title = self.get_text(self.SELECTED_HTML_LI)
        Logger.log('get_selected_menu_title() : "'+_title+'"')
        return _title

    def click_on_administration_menu(self):
        Logger.log('click_on_administration_menu()')
        self.click_js(self.ADMINISTRATION_CSS_SELECTOR)
        # self.do_click(self.ADMINISTRATION_HTML_A)


