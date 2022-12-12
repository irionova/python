from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL_TESTING = 'https://tensor.ru/'
TEXT_TESTING = "Тензор"


def test_text():

    driver = webdriver.Chrome()
    driver.get("https://ya.ru/")
    time.sleep(1.5)


    """ПРОВЕРКА наличия поля для ввода"""
    try:
        text = driver.find_element("name", "text")
        print("поле ввода на месте")
    except:
        print("отсутствует поле ввода")


    text.send_keys("Тензор")
    time.sleep(1.5)


    """ПРОВЕРКА наличия подсказок"""
    suggest =driver.find_element("class name",'mini-suggest__popup-content')
    inners=suggest.get_attribute('innerHTML')
    if inners:
        print("подсказки есть")
    else:
        print("отсутствует таблица с подсказками")


    text.send_keys(Keys.ENTER)
    time.sleep(1)


    """ПРОВЕРКА 1я ссылка ведет на сайт 'https://tensor.ru/'"""
    try:
        first_result = driver.find_element("xpath", "//li[@data-first-snippet]//div//div//a")
        tensor = driver.find_element("xpath", "//a[@href='https://tensor.ru/']")
        print(first_result == tensor)
    except:
        print("в результатах нет ссылки на ", 'https://tensor.ru/')

    driver.quit()



test_text ()

