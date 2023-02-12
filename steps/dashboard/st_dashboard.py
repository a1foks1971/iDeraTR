from pages.testrail_base_pg import TestRailBase
from pages.dashboard.dashboard_pg import Dashboard
from steps.BaseStep import StepBase

class SDashboard(StepBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.testRail = TestRailBase(self.driver)
        self.dashboard = Dashboard(self.driver)

    def verify_current_user_full_name(self, expected_user_full_name):
        actual_name = self.testRail.Top.get_user_full_name()
        assert expected_user_full_name == actual_name

    def verify_dashboard_has_been_loaded(self):
        is_content_visible = self.dashboard.Content.is_content_visible()
        assert is_content_visible

    def verify_dashboard_menu_is_selected(self):
        selected_menu = self.testRail.Header.get_selected_menu_title()
        assert selected_menu == self.testRail.Header.EXPECTED_TITLES["DASHBOARD_MENU"]

    def click_on_administration_menu(self):
        self.testRail.Header.click_on_administration_menu()

    def open_first_project(self):
        self.dashboard.Content.click_on_project_with_index(0)
