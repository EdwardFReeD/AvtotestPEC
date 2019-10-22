import time
import zapis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys
def test_line():
        driver = webdriver.Chrome(executable_path = 'chromedriver.exe')  # chromedriver.exe должен находиться в той же папке, что и этот скрипт!
        driver.get("https://pecom.ru/contacts/feedback/")  # Перейти по ссылк
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'selectize-input.items.not-full.has-options'))).click() # нажимаем на класс
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'option.active'))).click()# еще один клик

        control = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'form_text_37')))# выбираем
        control.send_keys("МСВК02ДГЯ-1/1610")  # отправляем текст в строку поиска
        control.send_keys(Keys.RETURN)  # имитируем нажатие клавиши Enter

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'form_text_38'))).click()# клик

        er =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div/div/div/div[1]/form/div[2]/div/div/div[3]/span'))).text.replace('\n', ' ')# замена

        if er == 'Груз не найден. Без указания груза вы не сможете отправить запрос.':# если равно то ошибка
           driver.close()
           zapis.log_read('||' + "https://pecom.ru/contacts/feedback/" + '||' + 'Ошибка: Груз не найден или поиск не отработал за 20 секунд.')
        elif  er != 'Груз не найден. Без указания груза вы не сможете отправить запрос.':# если не равно то идем далее
         zapis.log_read(
             '||' + "https://pecom.ru/contacts/feedback/" + '||' + 'Поиск груза в "Отзывы и предложения работает корректно')
         driver.close()
