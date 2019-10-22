import time
import zapis
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def test_line():
        driver = webdriver.Chrome(executable_path = 'chromedriver.exe')  # chromedriver.exe должен находиться в той же папке, что и этот скрипт!
        driver.get("https://pecom.ru/contacts/feedback/")  # Перейти по ссылк
        select = driver.find_element_by_class_name('selectize-input.items.not-full.has-options').click() # нажимаем на класс
        time.sleep(1)
        select1 = driver.find_element_by_class_name('option.active').click()# еще один клик
        time.sleep(1)
        control = driver.find_element_by_id('form_text_37') # выбираем
        control.send_keys("МСВК02ДГЯ-1/1610")  # отправляем текст в строку поиска
        control.send_keys(Keys.RETURN)  # имитируем нажатие клавиши Enter
        time.sleep(10) # спати
        driver.find_element_by_id('form_text_38').click()# клик
        time.sleep(1)
        er = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div/div[1]/form/div[2]/div/div/div[3]/span').text.replace('\n', ' ')# замена
        time.sleep(1)
        if er == 'Груз не найден. Без указания груза вы не сможете отправить запрос.':# если равно то ошибка
           driver.close()
           zapis.log_read('||' + "https://pecom.ru/contacts/feedback/" + '||' + 'Ошибка: Груз не найден или поиск не отработал за 20 секунд.')
        elif  er != 'Груз не найден. Без указания груза вы не сможете отправить запрос.':# если не равно то идем далее
         zapis.log_read(
             '||' + "https://pecom.ru/contacts/feedback/" + '||' + 'Поиск груза в "Отзывы и предложения работает корректно')
         driver.close()
