from pages.testrail_base_pg import TestRailBase
from pages.administration.administration_pg import Administration
from steps.BaseStep import StepBase

class SAdministration(StepBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.testRail = TestRailBase(self.driver)
        self.administration = Administration(self.driver)

    def verify_administration_has_been_loaded(self):
        is_content_visible = self.administration.Content.is_content_visible()
        assert is_content_visible

