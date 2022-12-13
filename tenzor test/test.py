from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

# Navigate to Url

driver.get("https://yandex.ru/")

# Get all the elements available with tag name 'p'

"""Нажимаем на поиск, чтобы открылась панель с сервисами"""
text = driver.find_element("class name", "dzen-search-arrow-common")
text.click()
time.sleep(2)

"""Проверка наличия ссылки на картинки"""
try:
    iframe = driver.find_element("css selector", 'iframe')
    driver.switch_to.frame(iframe)
    e = driver.find_element(By.XPATH, "//a[@href='https://yandex.ru/images/?utm_source=main_stripe_big']")#/span[@class='desktop-services__text']")
    print("ссылка на картинки на месте")
    e.click()
except:
    print("не кликается")

time.sleep(2)
