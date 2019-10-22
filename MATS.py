# 18|10|2019
# Function return cargo list with no delivery and @TargetBranch@ МВ
def get_cargo_list():
    import pyodbc
    # SQL Connection string
    try:
        con_str = pyodbc.connect('Driver={SQL Server};'
                                 'Server=v-sql-kabinet;'
                                 'Database=kabinet2;'
                                 'UID=kabinet2;'
                                 'PWD=fgb2[vdt;')
        con_str.timeout = 2
        cursor = con_str.cursor()

        # Request to SQL
        cursor.execute("SELECT TOP 10 CargoCode FROM [kabinet2].[dbo].[Cargos] "
                       "WHERE CargoReceiverAddress = '' "
                       "and CargoReceiveDate >= (select DateAdd(MONTH, -1, cast(GetDate() as date))) "
                       "and CargoCode like 'МВ%' "
                       "and CargoNCargoStatus in ('1','2','3') "
                       "and CargoNCargoTypeOfIssue = '1' "
                       "and (select CargoCurrentStatusFromEvents.CargoStatus "
                       "FROM [kabinet2].[dbo].[CargoCurrentStatusFromEvents] "
                       "where CargoCurrentStatusFromEvents.CargoGUID = Cargos.CargoGUID) in (10,20,30,40,50,60,110,130);")

        # List of Cargo Index
        cargo_list = []
        for row in cursor:
            cargo_list.append(row[0])
        if cargo_list != None:
            return cargo_list
        else:
            return None
    except pyodbc.DatabaseError as e:
        return ('Ошибка связа с БД: {' + str(e) + '}')
    except pyodbc.DataError as e:
        return ('Ошибка связа с данными: {' + str(e) + '}')
    except pyodbc.ProgrammingError as e:
        return ('Программая ошибка: {' + str(e) + '}')
    except pyodbc.Error as e:
        return ('Ошибка: {' + str(e) + '}')
    except:
        return ('Неизвестная ошибка: {' + str(SystemError) + '}')
    finally:
        con_str.close()
#######################################################################################################################

# 18|10|2019
# Function return response from API /CARGOPICKUPNETWORK/SUBMIT/
def cargo_network_request():
    import requests
    import json
    from datetime import date

    try:

        url = ('https://kabinet.pecom.ru/api/v1/CARGOPICKUPNETWORK/SUBMIT/')
        request = {
            "common": {
                "applicationDate": str(date.today()),
                "responsiblePerson": "PECOM_MONITORING",
                "description": "Тестовый груз"
            },
            "sender": {
                "inn": "7716542310",
                "city": "Оренбург",
                "title": "PECOM_MONITORING",
                "person": "PECOM_MONITORING",
                "phone": "22-33-44",
                "email": "example@example.com",
                "addressOffice": "ул. Антонова, д. 2",
                "addressStock": "ул. Боровиковского, 17, строение 5",
                "workTimeFrom": "10:15",
                "workTimeTo": "18:00",
                "lunchBreakFrom": "14:00",
                "lunchBreakTo": "15:00"
            },
            "cargos": {
                "common": {
                    "cargoTotals": {
                        "volume": 10,
                        "weight": 200,
                        "maxDimension": 10,
                        "positionsCount": 5
                    },
                    "services": {
                        "pickUp": {
                            "payer": {
                                "type": 3,
                                "other": {
                                    "inn": "7716542310",
                                    "title": "PECOM_MONITORING",
                                    "paymentCity": "Оренбург",
                                    "phone": "22-33-44"
                                }
                            }
                        },
                        "transporting": {
                            "payer": {
                                "type": 1
                            }
                        },
                        "delivery": {
                            "payer": {
                                "type": 1
                            }
                        },
                        "insurance": {
                            "payer": {
                                "type": 1
                            }
                        }
                    },
                    "typeClientBarcode": "EAN13"
                },
                "items": [
                    {
                        "receiver": {
                            "inn": "7716542310",
                            "city": "Москва",
                            "title": "PECOM_MONITORING",
                            "person": "PECOM_MONITORING",
                            "phone": "33-44-55"
                        },
                        "cargo": {
                            "transporting": 1,
                            "description": "обувь",
                            "orderNumber": "№23434-АБ",
                            "weight": 2.5,
                            "volume": 0.1,
                            "width": 0.12,
                            "length": 0.3,
                            "height": 0.4,
                            "positionsCount": 2,
                            "clientPositionsBarcode": [
                                "123654789"
                            ]
                        },
                        "conditions": {
                            "isOpenCar": 'false',
                            "isSideLoad": 'true',
                            "isDayByDay": 'false',
                            "isSpecialEquipment": 'false',
                            "isUncovered": 'false',
                            "isFast": 'true',
                            "isLoading": 'false'
                        },
                        "services": {
                            "pickUp": {
                                "payer": {
                                    "type": 2
                                }
                            },
                            "transporting": {
                                "payer": {
                                    "type": 1
                                }
                            },
                            "delivery": {
                                "enabled": 'true',
                                "avisationDateTime": "2013-04-02",
                                "address": "Россия, Москва, Сормовский проезд, 7Ак2",
                                "payer": {
                                    "type": 1
                                }
                            },
                            "insurance": {
                                "enabled": 'true',
                                "cost": 20000.25,
                                "payer": {
                                    "type": 1
                                }
                            },
                            "documentsReturning": {
                                "enabled": 'true',
                                "payer": {
                                    "type": 1
                                }
                            },
                            "strapping": {
                                "enabled": 'false'
                            },
                            "sealing": {
                                "enabled": 'true',
                                "positionsCount": 12,
                                "payer": {
                                    "type": 3,
                                    "other": {
                                        "inn": "7716542310",
                                        "title": "PECOM_MONITORING",
                                        "phone": "22-33-44"
                                    }
                                }
                            },
                            "hardPacking": {
                                "enabled": 'true',
                                "positionsCount": 5,
                                "payer": {
                                    "type": 1
                                }
                            },
                            "cashOnDelivery": {
                                "enabled": 'false'
                            }
                        }
                    }
                ]
            }
        }
        headers = {'content-type': 'application/json'}

        response = requests.post(url, auth=('pec_test', 'BD81AB610DB6175B4FFF0AA401A1E8AA177B4F26'),
                                 data=json.dumps(request), headers=headers)
        return str(response.json()), response.status_code

    except requests.exceptions.Timeout as e:
        return e
    except requests.exceptions.TooManyRedirects as e:
        return e
    except requests.exceptions.RequestException as e:
        return e
    except json.JSONDecodeError as e:
        return ('Возникла ошибка: {' + str(e) + '} Связанная с URL - адресом!!!')
#######################################################################################################################