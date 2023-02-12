from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import Logger
from utils.functions import sleep_sec


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click_js(self, by_locator):
        Logger.log('_base_pg.click_js(...) BEGIN')
        s = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        Logger.log('_base_pg.click_js(...) WebDriverWait() PASSED')
        self.driver.execute_script("arguments[0].click();", s)
        Logger.log('_base_pg.click_js(...) END')

    def click_js_css(self, css_selector):
        Logger.log('_base_pg.click_js_css("'+css_selector+'") BEGIN')
        by_locator = (By.CSS_SELECTOR, css_selector)
        s = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        Logger.log('_base_pg.click_js_css(css) WebDriverWait() PASSED')
        self.driver.execute_script("arguments[0].click();", s)
        Logger.log('_base_pg.click_js_css(css) END')

    def do_send_keys(self, by_locator, query):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(query)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_click_on_element(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element)).click()

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()

    def get_elements(self, by_locator):
        Logger.log('_base_pg.get_elements() BEGIN')
        elements = self.driver.find_elements(by_locator)
        elements_number = len(elements)
        Logger.log('_base_pg.get_elements() : elements_number = "'+str(elements_number)+'"')
        assert 0 < elements_number
        WebDriverWait(self.driver, 10).until(EC.visibility_of(elements[0]))
        return self.driver.find_elements(by_locator)

    def get_number_of_elements(self, by_locator):
        return  len(self.get_elements(by_locator))

    # def isDisplayed():
    #     try:
    #         browser.find_element_by_xpath("//*[text()='find text vwhis in page']")
    #     except NoSuchElementException:
    #         return False
    #     return True