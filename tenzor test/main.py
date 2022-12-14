from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



URL_TESTING = 'https://tensor.ru/'
TEXT_TESTING = "Тензор"
BROWSER = "explorer" #можно заменить на explorer, firefox
url="https://yandex.ru/images"

def test_images():
    driver = webdriver.Chrome()
    driver.get("https://yandex.ru/")

    """Нажимаем на поиск, чтобы открылась панель с сервисами"""
    text = driver.find_element("class name", "dzen-search-arrow-common")
    text.click()
    time.sleep(2)

    """Проверка наличия ссылки на картинки"""
    try:
        iframe = driver.find_element("css selector", 'iframe')
        driver.switch_to.frame(iframe)
        e = find_element(By.XPATH, "//a[@href='https://market.yandex.ru/?clid=505&utm_source=main_stripe_big&wprid=1670930605407763-13955599325398295785-vla1-4643-vla-l7-balancer-8080-BAL-5384&src_pof=505&icookie=rG3DxCbp9FOeFBsRSdAayNnNsOia2lHdeNYfKm9Z9KUTV293aC8Lg%2BSJHEVDmUPG3rCwmLS6BGNdxrEgHzyaq47rsjo%3D&utm_source_service=morda']")
        #e=find_element(By.XPATH, "//a[@href='https://yandex.ru/images/?utm_source=main_stripe_big']/span[@class='desktop-services__text']")
        print("ссылка на картинки на месте")
        e.click()
    except:
        print("не кликается")

    """ИЗМЕНИТЬ ДОБАВИТЬ НОРМ КЛИК ПО ССЫЛКЕ"""
    driver.get("https://yandex.ru/images/?utm_source=main_stripe_big")


    """Проверка верности ссылки"""
    if driver.current_url.find(url) != (-1):
        print("верная ссылка на картинки")
    else:
        print("не та ссылка")
        driver.quit()

    category = driver.find_element("class name", "PopularRequestList-Item_pos_0")
    link = category.find_element("xpath", ".//a")
    name_category = link.text
    link.click()
    time.sleep(2)

    """Проверка, что название категории отображается в поле поиска"""
    text_ = driver.find_element("name", "text")
    if text_.get_attribute('value') == name_category:
        print("название категории верно отображается в строке поиска")
    else:
        print("название категории неверно отображается в строке поиска")

    first_img = driver.find_element("class name", "serp-item")
    first_img.find_element("xpath",".//a").click()

    time.sleep(2)
    prev_img_src = driver.find_element("class name", "MMImage-Origin").get_attribute("src")

    driver.find_element("class name", "CircleButton_type_next").click()
    time.sleep(2)
    if (driver.find_element("class name", "MMImage-Origin").get_attribute("src") != prev_img_src):
        print("при нажатии вперед картинка сменилась")
    else:
        print("картинка не сменилась")

    driver.find_element("class name", "CircleButton_type_prev").click()
    time.sleep(2)
    print(driver.find_element("class name", "MMImage-Origin").get_attribute("src") == prev_img_src)


    driver.quit()







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



test_text()
test_images()
