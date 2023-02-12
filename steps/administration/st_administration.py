from pages.testrail_base_pg import TestRailBase
from pages.administration.administration_pg import Administration
from steps.BaseStep import StepBase
from utils.logger import Logger
from utils.functions import sleep_sec

class SAdministration(StepBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.testRail = TestRailBase(self.driver)
        self.administration = Administration(self.driver)

    def verify_administration_has_been_loaded(self):
        is_content_visible = self.administration.Content.is_content_visible()
        Logger.log('st_administration: verify_administration_has_been_loaded > '+str(is_content_visible))
        assert is_content_visible

    def verify_administration_menu_is_selected(self):
        selected_menu = self.testRail.Header.get_selected_menu_title()
        answer = selected_menu == self.testRail.Header.EXPECTED_TITLES["ADMINISTRATION_MENU"]
        Logger.log('st_administration: verify_administration_menu_is_selected > '+str(answer))
        assert answer

    def open_first_project(self):
        Logger.log('st_administration: open_first_project')
        self.administration.Content.click_on_projects_from_the_other_section_with_index(0)
