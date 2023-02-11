from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def do_send_keys(self, by_locator, query):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(query)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()

    # def isDisplayed():
    #     try:
    #         browser.find_element_by_xpath("//*[text()='find text vwhis in page']")
    #     except NoSuchElementException:
    #         return False
    #     return True