from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger
from utils.functions import sleep_sec


class Header(BasePage):
    EXPECTED_TITLES = {
        "DASHBOARD_MENU": "DASHBOARD",
        "ADMINISTRATION_MENU": "ADMINISTRATION",
    }

    ADMINISTRATION_HTML_LI_BY = (By.CSS_SELECTOR, 'ul.header-menu > li.header-menu-item-right')
    ADMINISTRATION_SELECTED_HTML_LI_BY \
        = (By.CSS_SELECTOR, 'ul.header-menu > li.header-menu-item-right.header-menu-item-selected')
    ADMINISTRATION_HTML_A_BY = (By.ID, 'navigation-admin')
    ADMINISTRATION_CSS_SELECTOR = '#navigation-admin'
    DASHBOARD_HTML_LI_BY = (By.CSS_SELECTOR, 'ul.header-menu > li:not(.header-menu-item-right)')
    DASHBOARD_HTML_A_BY = (By.ID, 'navigation-dashboard')
    SELECTED_HTML_LI_BY = (By.CSS_SELECTOR, 'ul.header-menu > li.header-menu-item-selected')

    def __init__(self, driver):
        super().__init__(driver)

    def get_selected_menu_title(self):
        _title = self.get_text(self.SELECTED_HTML_LI_BY)
        Logger.log('header_pg: get_selected_menu_title() : "'+_title+'"')
        return _title

    def click_on_administration_menu(self):
        Logger.log('header_pg: click_on_administration_menu()')
        self.click_js(self.ADMINISTRATION_HTML_A_BY)
        # self.click_js_css(self.ADMINISTRATION_CSS_SELECTOR)
        # self.do_click(self.ADMINISTRATION_HTML_A)

    def is_administration_menu_selected(self):
        answer = self.is_visible(self.ADMINISTRATION_SELECTED_HTML_LI_BY)
        Logger.log('header_pg: is_administration_menu_selected >>> '+str(answer))
        return answer
