# Сайт
import test_delivery
import test_line
import test_status
import test_calc
import tarificator
import test_api_status
import test_api_preregistration
import MATS
import sys
import zapis

try:
    for cargo in MATS.get_cargo_list():
        test_delivery.delivery(cargo)
    #test_calc.calc()
    #test_status.test_status()
    #test_line.test_line()
    #tarificator.tar()
    #test_api_preregistration.prereg()
    #test_api_status.lkstatus()
    #MATS.cargo_network_request()
except Exception:
    zapis.log_read('||' + "Script: testsite" + '||'
                   + 'Необработанная ошибка: '
                   + sys.exc_info()[1].msg)