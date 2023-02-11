from pages.testrail_base_pg import TestRailBase
from pages.dashboard.dashboard_pg import Dashboard
from steps.BaseStep import StepBase

class SDashboard(StepBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.testRail = TestRailBase(self.driver)
        self.dashboard = Dashboard(self.driver)

    def verify_current_user_full_name(self, expected_user_full_name):
        actual_name = self.testRail.Header.get_user_full_name()
        assert expected_user_full_name == actual_name

    def verify_dashboard_has_been_loaded(self):
        is_content_visible = self.dashboard.Content.is_content_visible()
        assert is_content_visible

