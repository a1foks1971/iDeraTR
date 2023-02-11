from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger
from pages.header.header_pg import Header
from pages.dashboard.dashboard_pg import Dashboard

class TestRailBase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.Header = Header(self.driver)
        self.Dashboard = Dashboard(self.driver)
