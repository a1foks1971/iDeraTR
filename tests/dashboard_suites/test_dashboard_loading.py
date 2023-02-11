import pytest
from steps.step_login.st_login import SLogin
from steps.dashboard.st_dashboard import SDashboard
from tests.test_base import BaseTest
from config.users import Users


class Test_Dashboard_Loading(BaseTest):

    def test_dashboard_after_user_logining(self):
        self.doOnLogin = SLogin(self.driver)
        self.doOnLogin.login_as(Users.get_user_email(), Users.get_user_password())
        self.doOnDashboard = SDashboard(self.driver)
        self.doOnDashboard.verify_dashboard_has_been_loaded()
        self.doOnDashboard.verify_current_user_full_name(Users.get_user_expected_full_name())
