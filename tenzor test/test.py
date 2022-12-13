from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

# Navigate to Url

driver.get("https://yandex.ru/")

# Get all the elements available with tag name 'p'

elements = driver.find_elements(By.TAG_NAME, 'a')
iframe = driver.find_element("css selector", 'iframe')
    driver.switch_to.frame(iframe)
for e in elements:
    print(e.text)
