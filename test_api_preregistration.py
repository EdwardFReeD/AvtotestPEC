import requests
import json
import zapis

def prereg():
  try:
    url_status = ('https://kabinet.pecom.ru/api/v1/PREREGISTRATION/SUBMIT/')
    zapros = {
      "sender": {
        "city": "Оренбург",
        "title": "PECOM_MONITORING",
        "phone": "+74951377572",
        "phoneAdditional": "",
        "person": "САПРОНОВ ВЛАДИМИР НИКОЛАЕВИЧ",
        "warehouseId": "328c63fd-d99d-11e7-80c9-00155d668927",
        "identityCard": {
          "type": 10,
          "series": "1010",
          "number": "101010",
          "date": "2003-04-22",
          "note": ""
        }
      },
      "cargos": [
        {
          "common": {
            "type": "3",
            "weight": 1,
            "volume": 1,
            "actualCost": 0,
            "includeTES": 'false',
            "accompanyingDocuments": 'false',
            "positionsCount": 1,
            "description": "мебель",
            "orderNumber": "000056646",
            "typeClientBarcode": "EAN13",
            "clientPriority": 1,
            "clientPositionsBarcode": []
          },
          "receiver": {
            "inn": "",
            "city": "Сургут",
            "title": "PECOM_MONITORING",
            "phone": "89227848747",
            "phoneAdditional": "",
            "comment": "",
            "addressStock": "Россия, г. Сургут, ул. Проспект Ленина, 34",
            "person": "Надымова Ольга Владимировна",
            "warehouseId": "",
            "identityCard": {
              "type": 10,
              "series": "1010",
              "number": "101010",
              "date": "2019-04-01",
              "note": ""
            }
          },
          "services": {
            "email": "",
            "transporting": {
              "payer": {
                "type": 3,
                "other": {
                  "title": "PECOM_MONITORING",
                  "phone": "+7(966)065-05-49",
                  "identityCard": {
                    "type": 10,
                    "series": "0000",
                    "number": "000000",
                    "date": "2019-04-01",
                    "note": ""
                  }
                },
                "paymentCity": "Москва Восток"
              }
            },
            "hardPacking": {
              "payer": {
                "type": 3,
                "other": {
                  "title": "PECOM_MONITORING",
                  "paymentCity": "Москва Восток",
                  "phone": "+7(966)065-05-49",
                  "identityCard": {
                    "type": 10,
                    "series": "0000",
                    "number": "000000",
                    "date": "2019-04-01",
                    "note": ""
                  }
                }
              },
              "enabled": 'true',
              "positionsCount": 1
            },
            "insurance": {
              "payer": {
                "type": 3,
                "other": {
                  "title": "PECOM_MONITORING",
                  "paymentCity": "Москва Восток",
                  "phone": "+7(966)065-05-49",
                  "identityCard": {
                    "type": 10,
                    "series": "0000",
                    "number": "000000",
                    "date": "2019-04-01",
                    "note": ""
                  }
                }
              },
              "enabled": 'true',
              "cost": 6600
            },
            "sealing": {
              "enabled": 'false'
            },
            "strapping": {
              "enabled": 'false'
            },
            "documentsReturning": {
              "payer": {
                "type": 3,
                "other": {
                  "title": "PECOM_MONITORING",
                  "paymentCity": "Москва Восток",
                  "phone": "+7(966)065-05-49",
                  "identityCard": {
                    "type": 10,
                    "series": "0000",
                    "number": "000000",
                    "date": "2019-04-01",
                    "note": ""
                  }
                }
              },
              "enabled": 'false'
            },
            "delivery": {
              "payer": {
                "type": 3,
                "other": {
                  "title": "PECOM_MONITORING",
                  "paymentCity": "Москва Восток",
                  "phone": "+7(966)065-05-49",
                  "identityCard": {
                    "type": 10,
                    "series": "0000",
                    "number": "000000",
                    "date": "2019-04-01",
                    "note": ""
                  }
                }
              },
              "enabled": 'true',
              "address": "Россия, г. Сургут, ул. Проспект Ленина, 34"
            },
            "storing": {
              "enabled": 'false'
            },
            "cashOnDelivery": {
              "enabled": 'false',
              "cashOnDeliverySum": 0,
              "actualCost": 0,
              "includeTES": False
            }
          }
        }
      ]
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url_status, auth=('pec_test', 'BD81AB610DB6175B4FFF0AA401A1E8AA177B4F26'),
                      data=json.dumps(zapros), headers=headers)

    if r.status_code != 200:
     zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: Метод вернул не статус 200')
    else:
        otvet = r.json()
        if 'error' in otvet:
            zapis.log_read(
                '||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + 'Ошибка: вернулось error')
        else:
            if otvet['cargos'] == None:
                zapis.log_read('||' + url_status + '||' + 'Status Code:'+str(r.status_code) + '||' + 'Ошибка: не получен ответ от метода /PREREGISTRATION/SUBMIT/')
            else:
                zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + 'Скрипт отработал успешно')
  except requests.exceptions.Timeout as e:
    return zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + str(e))
  except requests.exceptions.TooManyRedirects as e:
    return zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + str(e))
  except requests.exceptions.RequestException as e:
    return zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + str(e))
  except json.JSONDecodeError as e:
    return zapis.log_read('||' + url_status + '||' + 'Status Code:' + str(r.status_code) + '||' + str(e))