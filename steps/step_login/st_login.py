from steps.BaseStep import StepBase


from pages.login.login_pg import LoginPage
class SLogin(StepBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.loginPage = LoginPage(self.driver)

    def login_as(self, user_email, user_password):
        self.loginPage.fill_email(user_email)
        self.loginPage.fill_password(user_password)
        self.loginPage.click_submit()

