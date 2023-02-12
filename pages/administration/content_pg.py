from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger


class Content(BasePage):
    CONTAINER_BY = (By.ID, "content")
    PROJECTS_TITLE_BY = (By.CSS_SELECTOR, ".page_title")
    OTHER_PROJECTS_ITEMS = (By.CSS_SELECTOR, ".content-border .tab_rightsection tr")

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

    def get_project_number(self):
        _other_projects_number = self.get_number_of_elements(self.OTHER_PROJECTS_ITEMS)
        Logger.log('get_project_number() : "'+str(_other_projects_number)+'"')
        return _other_projects_number

    def get_projects_from_the_other_section(self):
        return self.get_elements(self.OTHER_PROJECTS_ITEMS)

    def click_on_projects_from_the_other_section_with_index(self, index):
        _project = self.get_projects_from_the_other_section()
        assert  index < len(_project)
        self.do_click_on_element(_project[index])