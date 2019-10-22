
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

#         test_status.test_status()  - не используеться так как блокирует каптча
#         test_line.test_line()- не используеться так как блокирует каптча


try:
    for cargos in MATS.get_cargo_list():
     if  test_delivery.delivery(cargos):
         break

    test_calc.calc()
    tarificator.tar()
    test_api_preregistration.prereg()
    test_api_status.lkstatus()
    MATS.cargo_network_request()
except Exception:
    zapis.log_read('||' + "Script: testsite" + '||'
                   + 'Необработанная ошибка: '
                   + sys.exc_info()[1].msg).replace('\n', ' ')