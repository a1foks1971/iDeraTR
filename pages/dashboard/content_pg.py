from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger


class Content(BasePage):
    CONTAINER_BY = (By.ID, "content_container")
    PROJECTS_TITLE_BY = (By.CSS_SELECTOR, "h1.top")

    def __init__(self, driver):
        super().__init__(driver)

    def is_content_visible(self):
        _is_visible = self.is_visible(self.CONTAINER_BY)
        Logger.log('is_content_visible() : '+str(_is_visible))
        return _is_visible

    def get_content_title(self):
        _title = self.get_text(self.PROJECTS_TITLE_BY)
        Logger.log('get_content_title() : "'+_title+'"')
        return _title

    # def get_project_number(self):
    #     _title = self.get_text(self.PROJECTS_TITLE_BY)
    #     Logger.log('get_content_title() : "'+_title+'"')
    #     return _title

