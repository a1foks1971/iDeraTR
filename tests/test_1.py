from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("start-maximized")
# driver = webdriver.Chrome('./chromedriver/chromedriver')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('http://tutorialsninja.com/demo/')

elem = driver.find_element(By.NAME, "search")
elem.clear()
elem.send_keys("iphone")
elem.send_keys(Keys.RETURN)

elem.clear()
# elem1 = driver.find_element(By.NAME, "search")
