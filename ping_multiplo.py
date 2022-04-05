# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/5958c88e-06e7-411e-84f3-3fa64db6a5ff
import os
import time

with open('hosts.txt') as file:
    dump = file.read().splitlines()

for ip in dump:
    print('verifando o ip: ', ip)
    print('-' * 60)
    os.system('ping -n 2 {}'.format(ip))
    print('-' * 60)
    time.sleep(5)
