import time
import zapis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def calc():
    try:
        driver = webdriver.Chrome(executable_path='chromedriver.exe')  # chromedriver.exe должен находиться в той же папке, что и этот скрипт!
        driver.get("https://pecom.ru/services-are/shipping-request/")  # Перейти по ссылк
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[2]').click()
        time.sleep(3)
        a = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[1]/textarea')
        a.send_keys("Россия, Оренбург, Малышевская улица, 28")  # отправляем текст в строку поиска
        time.sleep(3)
        a.send_keys(Keys.RETURN)
        time.sleep(3)

        zabor = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/label').click() # имитируем нажатие клавиши Enter
        time.sleep(3)

        dostav = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/label').click()
        time.sleep(5)

        b = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/textarea')
        b.clear()
        b.send_keys("Россия, Санкт-Петербург, Дворцовая площадь, 6-8")  # отправляем текст в строку поиска
        time.sleep(3)
        b.send_keys(Keys.RETURN)  # имитируем нажатие клавиши Enter  bid-btn btn btn-blue
        time.sleep(5)

        if driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/button').text != 'Оформить заявку':
            zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||' + 'Подача заявки: Не удалось перейти на шаг 2')
        else:
            driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/button').text == 'Оформить заявку'
            driver.find_element_by_class_name('bid-btn.btn.btn-blue').click()

      # характер гурза
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]').click()
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]').click()
        #time.sleep(5)

        # Отправитель
        driver.find_element_by_class_name('bid-agent-new__button').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]').click()
        phone = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[3]/div/div[2]/input')
        phone.send_keys('1111111111')
        fam = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[5]/div/input')
        fam.send_keys('Тест')
        name = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[7]/div/input')
        name.send_keys('Тест')



        doc = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[10]/div[2]/div/div/div[1]/input')
        doc.click()
        doc.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[10]/div[3]/div/div[1]/div[2]/div/input').send_keys('1111')
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/form/div[10]/div[3]/div/div[2]/div[2]/div/input').send_keys('111111')
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button').click()

        time.sleep(5)

        #zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||' + 'Подача заявки: Не удалось перейти на шаг 2')

        # получатель
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div').click()
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(5)

        #zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||' + 'Подача заявки: Не удалось перейти на шаг 2')

        # Плательщик
        com = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div[2]/div[5]/div/textarea')
        com.click()
        com.send_keys('PECOM_MONITORING')

        #zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||' + 'Подача заявки: Не удалось перейти на шаг 2')

        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div[3]/label/span').click()
        driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div[4]/div[1]/button[1]').click()
        time.sleep(5)
        zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||'+ 'Подача заявки:Заявка подана успешно, номер зявки ' + driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]').text)
    except Exception:
        if 'element click intercepted' in sys.exc_info()[1].msg:
            zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||'
                       + 'Ошибка TimeOut страницы: '
                       + sys.exc_info()[1].msg)
        else:
            zapis.log_read('||' + "https://pecom.ru/services-are/shipping-request/" + '||'
                           + 'Необработанная ошибка: '
                           + sys.exc_info()[1].msg)
    finally:
        driver.close()