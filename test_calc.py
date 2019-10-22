import time
import zapis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys

def calc():
 try:

    driver = webdriver.Chrome(executable_path='chromedriver.exe')  # chromedriver.exe должен находиться в той же папке, что и этот скрипт!

    driver.get("https://pecom.ru/services-are/shipping-request/")  # Перейти по ссылк
    # Удаление адреса
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/a'))).click()

    # Удаление адреса
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[2]'))).click()
    # заполнение A
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[1]/textarea')))
    s = 'Россия, Оренбург, Малышевская улица, 28' # Костыль 22.10.2019 посмотрим сколько проработает
    a.send_keys(s)  # отправляем текст в строку поиска
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[3]')))
    a.send_keys(Keys.RETURN)
    #Забор
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/label'))).click()
    # заполняем B
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/textarea')))
    s = 'Россия, Санкт-Петербург, Дворцовая площадь, 6-8'# Костыль 22.10.2019 посмотрим сколько проработает
    b.send_keys(s)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[3]')))
    b.send_keys(Keys.RETURN)  # имитируем нажатие клавиши Enter  bid-btn btn btn-blue

     # Проверка на ошибку
    if WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/button'))).text != 'Оформить заявку':
        zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||' + 'Подача заявки: Не удалось перейти на шаг 2')
    else:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/button'))).text == 'Оформить заявку'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'bid-btn.btn.btn-blue'))).click()

    # характер гурза
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]'))).click()

    # Отправитель
    time.sleep(5)
    har = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'bid-agent-new__button')))
    har.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]'))).click()
    phone =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[3]/div/div[2]/input')))
    phone.send_keys('1111111111')
    fam =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[5]/div/input')))
    fam.send_keys('Тест')
    name =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[7]/div/input')))
    name.send_keys('Тест')

    doc = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[10]/div[2]/div/div/div[1]/input')))
    doc.click()
    doc.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[10]/div[3]/div/div[1]/div[2]/div/input'))).send_keys('1111')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[10]/div[3]/div/div[2]/div[2]/div/input'))).send_keys('111111')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button'))).click()

    # получатель
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/button'))).click()

    # Плательщик
    com = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div[2]/div[5]/div/textarea')))
    com.click()
    com.send_keys('PECOM_MONITORING')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div[3]/label/span'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div[4]/div[1]/button[1]'))).click()
    zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||'+ 'Подача заявки:Заявка подана успешно, номер зявки ' + WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]'))).text)
 except Exception:
        if sys.exc_info() != None:
            if 'element click intercepted' in sys.exc_info()[1].msg:
                zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||'
                           + 'Ошибка TimeOut страницы: '
                           + sys.exc_info()[1].msg).replace('\n', ' ')
            else:
                zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||'
                               + 'Необработанная ошибка: '
                               + sys.exc_info()[1].msg).replace('\n', ' ')
 finally:
        driver.close()