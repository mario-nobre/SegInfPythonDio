# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/9cbfab44-7f65-4e3d-bbc0-25c04c4eed0d

import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP Externo\n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg: {0}'.format(org, regiao, pais, cid, ip))
