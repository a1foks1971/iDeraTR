from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger
from pages.header.top_pg import Top
from pages.dashboard.dashboard_pg import Dashboard
from pages.header.header_pg import Header

class TestRailBase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.Top = Top(self.driver)
        self.Header = Header(self.driver)
        self.Dashboard = Dashboard(self.driver)
