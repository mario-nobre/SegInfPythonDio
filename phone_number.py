# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/b170c7e8-9dd3-4f7b-a0e3-dee4f91dc3d3
import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone no formato +551140021234: ')
phone_numbers = phonenumbers.parse(phone)
print(geocoder.description_for_number(phone_numbers, 'pt-br'))
