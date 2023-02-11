
class StepBase:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://gurock.testrail.com/')