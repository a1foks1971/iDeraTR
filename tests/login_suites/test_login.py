import pytest

from steps.step_login.st_login import SLogin
from steps.dashboard.st_dashboard import SDashboard
from tests.test_base import BaseTest
from config.users import Users

class Test_Login(BaseTest):

    def test_login(self):
        self.doOnLogin = SLogin(self.driver)
        self.doOnLogin.login_as(Users.get_user_email(), Users.get_user_password())
        # self.doOnLogin.login_as("tomara@qarea.us", "Tf0r+_2023")
        self.doOnDashboard = SDashboard(self.driver)
        self.doOnDashboard.verify_current_user_full_name(Users.get_user_expected_full_name())
        # self.doOnDashboard.verify_current_user_full_name("Michael Tomara")
