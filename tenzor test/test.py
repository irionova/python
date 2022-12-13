from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



URL_TESTING = 'https://tensor.ru/'
TEXT_TESTING = "Тензор"
BROWSER = "explorer" #можно заменить на explorer, firefox
url="https://yandex.ru/images"

def test_images():
    print(" \n Старт второго теста \n ")

    driver = webdriver.Chrome()
    driver.get("https://yandex.ru/")

    """Нажимаем на поиск, чтобы открылась панель с сервисами"""
    text = driver.find_element("class name", "dzen-search-arrow-common")
    text.click()
    time.sleep(2)

    try:
        iframe = driver.find_element("css selector", 'iframe')
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, "//a[@href='https://yandex.ru/images/?utm_source=main_stripe_big']").click()
    except:
        print("не кликается")

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    """Проверка верности ссылки"""
    if (driver.current_url.find(url) != -1):
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


    """Проверка, что картинка открылась"""
    try:
        prev_img_src = driver.find_element("class name", "MMImage-Origin").get_attribute("src")
        print("Картинка прогрузилась")
    except:
        print("Картинка не прогрузилась")

    driver.find_element("class name", "CircleButton_type_next").click()
    time.sleep(2)

    """Проверка, что картинка сменилась"""
    if (driver.find_element("class name", "MMImage-Origin").get_attribute("src") != prev_img_src):
        print("при нажатии вперед картинка сменилась")
    else:
        print("картинка не сменилась")

    driver.find_element("class name", "CircleButton_type_prev").click()
    time.sleep(2)

    """Проверка, что картинка та же"""
    print(driver.find_element("class name", "MMImage-Origin").get_attribute("src") == prev_img_src)


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

    print(" \n Старт первого теста \n ")

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
test_images()
