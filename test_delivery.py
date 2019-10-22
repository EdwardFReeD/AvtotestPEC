import time
import zapis
from selenium import webdriver
import sys

from selenium.webdriver.common.keys import Keys


# КДОРЦЗТ-21/2507

def delivery(cargo):
    try:
        driver = webdriver.Chrome(
            executable_path='chromedriver.exe')  # chromedriver.exe должен находиться в той же папке, что и этот скрипт!
        # Перейти по ссылке

        driver.get("https://pecom.ru/services-are/delivery/")  # открытие страницы
        elem1 = driver.find_element_by_name("cargo_code")  # найти элемент по имени
        elem1.clear()  # очистить строку поиска перед печатанием
        elem1.send_keys(cargo)  # отправляем текст в строку поиска
        elem1.send_keys(Keys.RETURN)  # имитируем нажатие клавиши Enter
        time.sleep(20)  # спать 20 секунд
        if driver.find_element_by_class_name(
                'js-cargo-status-success-text').text != 'Заказ доставки доступен':  # если текст в классе не равен, тогда выдаем ошибку
            zapis.log_read(
                '||' + "https://pecom.ru/services-are/delivery/" + '||' 'Ошибка: Заказ доставки не доступен или груз не был найден за 20 секунд')
        elif driver.find_element_by_class_name(
                'js-cargo-status-success-text').text == 'Заказ доставки доступен':  # если заказ доставки доступен то идем далее
            elem2 = driver.find_element_by_class_name(
                "form-control.delivery-address-target.js-delivery-address")  # находим класс
            elem2.clear()  # очистить строку поиска перед печатанием
            elem2.send_keys("Россия, Москва, Сормовский проезд, 7Ак2")  # отправляем текст в строку поиска
            time.sleep(2)  # спать на 2 секунды
            elem3 = driver.find_element_by_class_name(
                "delivery-address-tip.js-delivery-address-tip").click()  # нажимаем на элемент
            time.sleep(5)  # спать
            message = driver.find_element_by_xpath(
                "/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[2]/div[3]/div[1]/label").text.replace(
                '\n', ' ')  # записываем текст и заменяем в нем enter
            message1 = driver.find_element_by_xpath(
                "/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[2]/div[3]/div[2]/div[1]/span[1]").text  # получаем текст
            time.sleep(5)  # спать
            elem4 = driver.find_element_by_xpath(
                "/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[3]").text  # получаем текст
            if driver.find_element_by_xpath(
                    "/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[3]/h3").text != 'Оплата':  # если текст элемента не равен "Оплата", тогда ошибка
                zapis.log_read(
                    '||' + "https://pecom.ru/services-are/delivery/" + '||' 'Ошибка:Не получена ориентировочная стоимость доставки: Предположительно не был получен адрес или не произвелся расчет стоимости')
            elif driver.find_element_by_xpath(
                    "/html/body/section[2]/div/div/div[2]/div/div/div[1]/form/div[3]/h3").text == 'Оплата':  # если равно оплата тогда гуд
                zapis.log_read(
                    '||' + "https://pecom.ru/services-are/delivery/" + '||' 'Заказ доставки: Сервис работает стабильно')
    except Exception:
        if 'element click intercepted' in sys.exc_info()[1].msg:
            zapis.log_read('||' + "https://pecom.ru/services-are/delivery/" + '||'
                           + 'Ошибка TimeOut страницы: '
                           + sys.exc_info()[1].msg)
        else:
            zapis.log_read('||' + "https://pecom.ru/services-are/delivery/" + '||'
                           + 'Необработанная ошибка: '
                           + sys.exc_info()[1].msg)
    finally:
        driver.close()