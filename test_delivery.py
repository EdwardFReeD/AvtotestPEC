import time
import zapis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys


from selenium.webdriver.common.keys import Keys


# КДОРЦЗТ-21/2507

def delivery(cargos):
 try:
    driver = webdriver.Chrome(
        executable_path='chromedriver.exe')  # chromedriver.exe должен находиться в той же папке, что и этот скрипт!
    # Перейти по ссылке

    driver.get("https://pecom.ru/services-are/delivery/")  # открытие страницы
    elem1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"form-control"))) # найти элемент по имени
    elem1.clear()  # очистить строку поиска перед печатанием
    elem1.send_keys(cargos)  # отправляем текст в строку поиска
    elem1.send_keys(Keys.RETURN)  # имитируем нажатие клавиши Enter

    if WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME,
            'js-cargo-status-success-text'))).text != 'Заказ доставки доступен':  # если текст в классе не равен, тогда выдаем ошибку
        zapis.log_read('||' + "https://pecom.ru/services-are/delivery/" + '||' 'Ошибка: Заказ доставки не доступен или груз не был найден за 60 секунд')
        return False
    elif WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,
            'js-cargo-status-success-text'))).text == 'Заказ доставки доступен':  # если заказ доставки доступен то идем далее
        elem2 = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "form-control.delivery-address-target.js-delivery-address")))  # находим класс
        elem2.clear()  # очистить строку поиска перед печатанием
        elem2.send_keys("Россия, Москва, Сормовский проезд, 7Ак2")  # отправляем текст в строку поиска

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,
            "delivery-address-tip.js-delivery-address-tip"))).click()  # нажимаем на элемент

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[2]/div[3]/div[1]/label"))).text.replace('\n', ' ')  # записываем текст и заменяем в нем enter
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[2]/div[3]/div[2]/div[1]/span[1]"))).text  # получаем текст

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[3]"))).text  # получаем текст
        if WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[3]/h3"))).text != 'Оплата':  # если текст элемента не равен "Оплата", тогда ошибка
            zapis.log_read('||' + "https://pecom.ru/services-are/delivery/" + '||' 'Ошибка:Не получена ориентировочная стоимость доставки: Предположительно не был получен адрес или не произвелся расчет стоимости')
        elif WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[3]/h3"))).text == 'Оплата':  # если равно оплата тогда гуд
            zapis.log_read('||' + "https://pecom.ru/services-are/delivery/" + '||' 'Заказ доставки: Сервис работает стабильно')
            return True


 except Exception:

     if sys.exc_info() != None:
         zapis.log_read('||' + "https://pecom.ru/services-are/delivery/" + '||'
                        + 'Ошибка TimeOut страницы: '
                        + sys.exc_info()[1].msg)

     else: zapis.log_read('||' + "https://pecom.ru/services-are/delivery/" + '||'
                        + 'Необработанная ошибка: '
                        + TimeoutException.msg)
 finally:
     driver.close()