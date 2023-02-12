from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

from pages._base_pg import BasePage
from utils.logger import Logger


class Content(BasePage):
    CONTAINER_BY = (By.ID, "content_container")
    PROJECTS_TITLE_BY = (By.CSS_SELECTOR, "h1.top")
    SUMMARY_PROJECT_TITLES_BY = (By.CSS_SELECTOR, "#content_container > .table.summary > .project > .flex-projects-2 .summary-title > a")

    _PROJECT_CSS = "#content_container > .table.summary > .project"

    def __init__(self, driver):
        super().__init__(driver)

    def _get_selector_for_project_with_index(self, index_from_zero):
        return self._PROJECT_CSS + ":nth-of-type(" + str(index_from_zero + 1) + ")"

    def _get_selector_for_title_of_project_with_index(self, index_from_zero):
        _css = self._get_selector_for_project_with_index(index_from_zero) + " > .flex-projects-2 .summary-title"
        # _css = self._get_selector_for_project_with_index(index_from_zero) + " > .flex-projects-2 .summary-title > a"
        Logger.log(_css)
        return _css

    def is_content_visible(self):
        _is_visible = self.is_visible(self.CONTAINER_BY)
        Logger.log('is_content_visible() : '+str(_is_visible))
        return _is_visible

    def get_content_title(self):
        _title = self.get_text(self.PROJECTS_TITLE_BY)
        Logger.log('get_content_title() : "'+_title+'"')
        return _title

    def get_all_projects(self):
        return self.get_elements(self.SUMMARY_PROJECT_TITLES_BY)

    def click_on_project_with_index(self, index):
        Logger.log(" *** click_on_project_with_index() *** AS 'COPWI'")
        _css = self._get_selector_for_title_of_project_with_index(index)
        Logger.log(" *** COPWI: _css = " + _css)
        _elm = self.driver.find_elements(By.CSS_SELECTOR, _css)
        Logger.log(" *** COPWI: _elmS.length = " + str(len(_elm)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of(_elm))
        Logger.log(" *** COPWI: WebDriverWait().until(EC.visibility_of())  == PASSED ==")
        _is_displayed = _elm.is_displayed()
        _is_displayed = _elm.is_displayed()
        Logger.log(" *** COPWI: _is_displayed = " + str(_is_displayed))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(_elm))
        Logger.log(" *** COPWI: WebDriverWait().until(EC.element_to_be_clickable())  == PASSED ==")
        _elm.click()
        Logger.log(" *** COPWI: _elm.click() == PASSED ==")

        # title_by = (By.CSS_SELECTOR, self._get_selector_for_title_of_project_with_index(index))
        # self.do_click(title_by)

    # def click_on_project_with_index(self, index):
    #     _project = self.get_all_projects()
    #     assert  index < len(_project)
    #     self.do_click_on_element(_project[index])

    # def get_project_number(self):
    #     _title = self.get_text(self.PROJECTS_TITLE_BY)
    #     Logger.log('get_content_title() : "'+_title+'"')
    #     return _title

