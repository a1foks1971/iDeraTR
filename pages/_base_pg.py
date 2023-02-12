import js2py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import Logger

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click_js(self, css_selector):
        Logger.log('_base_pg.click_js("'+css_selector+'") BEGIN')
        by_locator = (By.CSS_SELECTOR, css_selector)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        js_function = "function f() {return document.querySelector('"+css_selector+"').click();}"
        js2py.eval_js(js_function)
        Logger.log('_base_pg.click_js(...) END')

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
        elements = self.driver.find_elements(by_locator)
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