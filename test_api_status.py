import requests
import json
import zapis

def lkstatus():
    try:
        code_gruza = 'ККЛЮХАШ-1/2908'
        url_status = ('https://kabinet.pecom.ru/api/v1/cargos/status/')
        zapros = {
            'cargoCodes': code_gruza,
            'returnPosition': 'true'
        }
        headers = {'content-type': 'application/json'}
        r = requests.post(url_status, auth=('pec_test', 'BD81AB610DB6175B4FFF0AA401A1E8AA177B4F26'),
                          data=json.dumps(zapros), headers=headers)

        if r.status_code != 200:
         zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: Метод вернул не статус 200')
        else:
            otvet = r.json()
            if 'error' in otvet:
                zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: вернулось error')
            else:
                if otvet['cargos'] == None:
                    zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: не получен ответ от метода /cargos/status/ ')
                else:
                     if otvet['cargos'][0]['info'] == None:
                            zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: не получена информация о грузе')
                     else:
                        cargo_info = otvet['cargos'][0]['info']

                        if otvet['cargos'][0]['cargo'] == None:
                            zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: не получены параметры груза')
                        else:
                             if otvet['cargos'][0]['sender'] == None:
                                zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: данные отправителя не получены')
                             else:
                                if otvet['cargos'][0]['receiver']['branch'] == None:
                                    zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: не получен город получателя')
                                else:
                                    if otvet['cargos'][0]['services']['items'] == None:
                                        zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: не получены услуги')
                                    else:
                                        zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Скрипт отработал успешно')
    except requests.exceptions.Timeout as e:
        return zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + str(e))
    except requests.exceptions.TooManyRedirects as e:
        return zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + str(e))
    except requests.exceptions.RequestException as e:
        return zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + str(e))
    except json.JSONDecodeError as e:
        return zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + str(e))

