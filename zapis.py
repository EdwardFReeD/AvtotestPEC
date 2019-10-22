import datetime
import time


def log_read(zapis):
    a = datetime.datetime.now()
    my_file = open('log.txt', 'a', encoding='utf-8')
    my_file.write(str(str(a) + '' + zapis + '\n'))
    my_file.close()