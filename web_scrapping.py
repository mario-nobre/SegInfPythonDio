# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/8c5f5686-8abb-47b0-8ffc-78b404207213

from bs4 import BeautifulSoup
import requests

endereco = 'https://www.climatempo.com.br'

site = requests.get(endereco).content

coleta = BeautifulSoup(site, 'html.parser')

print(coleta.prettify())
