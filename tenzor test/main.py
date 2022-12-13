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

    #get_attribute('value').encode('utf-8')


    driver.quit()

"""
    try:
        text = driver.find_element("class name", "dzen-search-arrow-common")
        text.click()
        time.sleep(2)
        print("поле ввода на месте")

        images_elem = driver.find_element(By.XPATH, "/html/body/form/div/div/div/div/ul/")

        #images_elem = driver.find_elements("class name", "desktop-services_js_inited")
        print(images_elem[0])
        #images = driver.find_element("xpath", "//a[@href='https://yandex.ru/images/?utm_source=main_stripe_big/']")
    except:
        print("отсутствует поле ввода")
"""







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



#test_text ()
test_images()
