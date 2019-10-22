import requests
import json
import zapis
def tar():
    url_status = ('http://v-dcr-tarif-lb/Tarif/hs/CalculatePricesNew')
    zapros = {
      "#ns": "http://collectdelivery.esb.ws.pecom.ru/containers",
      "#type": "PECCD_Request",
      "#value": {
        "sourceBranch": {
          "id": "КР"
        },
        "targetBranch": {
          "id": "ТП"
        },
        "dateOfCreation": "2019-09-19T10:26:00.9898524",
        "cargo": {},
        "intake": {
          "isEnabled": True,
          "addressForCar": {
            "latitude": "44.981763",
            "longitude": "38.896845"
          },
          "dateOfIntake": "2019-09-20T09:00:00",
          "payment": {
            "currency": {
              "code": "810"
            }
          }
        },
        "transportation": {
          "isEnabled": False
        },
        "insurance": {
          "isEnabled": False
        },
        "delivery": {
          "isEnabled": True,
          "addressForCar": {
            "latitude": "43.903712",
            "longitude": "39.444701"
            }
          },
        "cargoParametersFromRequest": {
          "weight": 24,
          "volume": 0.19,
          "maxLength": 0,
          "maxHeight": 0,
          "maxWidth": 0.95
        }
      }
    }

    headers = {'content-type': 'application/json'}
    r = requests.post(url_status, auth=('IUSR', 'oMNya5CoXkGUT5dnKfut'),
                      data=json.dumps(zapros), headers=headers)

    if r.status_code != 200:
     zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: Метод вернул не статус 200')
    else:
        otvet = r.json()
        if 'error' in otvet:
            zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + 'Ошибка: вернулось error')
            raise SystemExit(1)
        else:
             if otvet['#ns'] == None or otvet['#type'] == None or otvet['#value'] == None  :
                 zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: не получен ответ от CalculatePricesNew')
             else:
                  a = (str(otvet['#value']['noteCargo'])).replace('\n', ' ')
                  zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + 'Скрипт отработал успешно' + '||' + a)