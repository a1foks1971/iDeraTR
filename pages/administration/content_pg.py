from selenium.webdriver.common.by import By

from pages._base_pg import BasePage
from utils.logger import Logger


class Content(BasePage):
    CONTAINER_BY = (By.ID, "content")
    PROJECTS_TITLE_BY = (By.CSS_SELECTOR, ".page_title")
    OTHER_PROJECTS_ITEMS_BY = (By.CSS_SELECTOR, ".content-border .tab_rightsection tr")
    OTHER_PROJECTS_ITEMS_CSS_SELECTOR = ".content-border .tab_rightsection tr"

    def __init__(self, driver):
        super().__init__(driver)

    def _get_selector_for_other_project_with_index(self, index_from_zero):
        """
        index_from_zero + 2
        the first '+1' because nth-of-type() starts with 1
        the second because the first 'tr>' is a header
        """
        _css = self.OTHER_PROJECTS_ITEMS_CSS_SELECTOR \
               + ":nth-of-type(" + str(index_from_zero + 2) + ") td:first-of-type > a"
        Logger.log('administration/content_pg: _get_selector_for_other_project_with_index\n  >>> _css = '+_css)
        return _css

    def is_content_visible(self):
        Logger.log('administration/content_pg: is_content_visible')
        _is_visible = self.is_visible(self.CONTAINER_BY)
        Logger.log('is_content_visible() : '+str(_is_visible))
        return _is_visible

    def get_content_title(self):
        Logger.log('administration/content_pg: get_content_title')
        _title = self.get_text(self.PROJECTS_TITLE_BY)
        Logger.log('get_content_title() : "'+_title+'"')
        return _title

    def get_project_number(self):
        Logger.log('administration/content_pg: get_project_number')
        _other_projects_number = self.get_number_of_elements(self.OTHER_PROJECTS_ITEMS_BY)
        Logger.log('get_project_number() : "'+str(_other_projects_number)+'"')
        return _other_projects_number

    def get_projects_from_the_other_section(self):
        Logger.log('administration/content_pg: get_projects_from_the_other_section')
        return self.get_elements(self.OTHER_PROJECTS_ITEMS_BY)

    def click_on_projects_from_the_other_section_with_index(self, index):
        Logger.log('administration/content_pg: click_on_projects_from_the_other_section_with_index')
        locator_by = (By.CSS_SELECTOR, self._get_selector_for_other_project_with_index(index))
        self.click_js(locator_by)

        # _project = self.get_projects_from_the_other_section()
        # assert  index < len(_project)
        # self.do_click_on_element(_project[index])