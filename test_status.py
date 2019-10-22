import time
import zapis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#КДОРЦЗТ-21/2507
def test_status():
        driver = webdriver.Chrome(executable_path = 'chromedriver.exe')  # chromedriver.exe должен находиться в той же папке, что и этот скрипт!
        driver.get("https://pecom.ru/services-are/order-status/?code=")  # Перейти по ссылке
        elem = driver.find_element_by_name("code")  # найти элемент по
        elem.clear()  # очистить строку поиска перед печатанием
        elem.send_keys("КДОРЦЗТ-21/2507")  # отправляем текст в строку поиска
        elem.send_keys(Keys.RETURN)  # имитируем нажатие клавиши Enter
        assert "No results found." not in driver.page_source  # Проверяем, что по-нашему запросу ничего не найдено.
        time.sleep(5) # спать
        message = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]").text # получаем текст
        message1 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]").text # получаем текст
        driver.close()
        zapis.log_read('||' + "https://pecom.ru/services-are/order-status/?code=" + '||' + message + ' ' + message1)
