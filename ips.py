# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/28322528-2783-40c5-b137-870fe8e96392

import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco + 100)

ip2 = '192.168.0.1/24'

rede = ipaddress.ip_network(ip2, strict=False)  # endereco = ipaddress.ip_address(ip)

for ip in rede:
    print(ip)
