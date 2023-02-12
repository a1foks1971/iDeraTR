from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger
from pages.dashboard.content_pg import Content


class Administration(BasePage):
    CONTAINER_BY = (By.CSS_SELECTOR, "#body-container")

    def __init__(self, driver):
        super().__init__(driver)
        self.Content = Content(self.driver)
