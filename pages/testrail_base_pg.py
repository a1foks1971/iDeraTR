from pages._base_pg import BasePage
from pages.header.top_pg import Top
from pages.header.header_pg import Header
from utils.functions import sleep_sec
from utils.logger import Logger

class TestRailBase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.Top = Top(self.driver)
        self.Header = Header(self.driver)
