import pytest
from steps.step_login.st_login import SLogin
from steps.dashboard.st_dashboard import SDashboard
from steps.administration.st_administration import SAdministration
from tests.test_base import BaseTest
from config.users import Users


class Test_Dashboard_Loading(BaseTest):

    def test_dashboard_after_user_logining(self):
        self.onLoginPage = SLogin(self.driver)
        self.onLoginPage.login_as(Users.get_user_email(), Users.get_user_password())
        self.onDashboardPage = SDashboard(self.driver)
        self.onDashboardPage.verify_dashboard_has_been_loaded()
        self.onDashboardPage.verify_current_user_full_name(Users.get_user_expected_full_name())
        self.onDashboardPage.verify_dashboard_menu_is_selected()
        # self.onDashboardPage.open_first_project()

        self.onDashboardPage.click_on_administration_menu()
        self.onAdministrationPage = SAdministration(self.driver)
        self.onAdministrationPage.verify_administration_has_been_loaded()
