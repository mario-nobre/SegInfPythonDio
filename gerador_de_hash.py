# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/ba422b20-a41c-4ec9-9016-d83270cc97b0

import hashlib

texto = input('Digite o texto a ser gerado a hash: ')

menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH ####
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print('A hash MD5 do texto: ', texto, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print('A hash SHA1 do texto: ', texto, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print('A hash SHA256 do texto: ', texto, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print('A hash SHA512 do texto: ', texto, 'é: ', resultado.hexdigest())
else:
    print('Algo de errado aconteceu, Tente novamente')
